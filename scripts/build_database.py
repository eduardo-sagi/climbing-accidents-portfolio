#!/usr/bin/env python3
"""Build the federated climbing-accidents SQLite database from derived public inputs.

Private WhatsApp material is optional and must be supplied explicitly with --whatsapp-ledger;
it is never copied into a public CSV export by default.
"""
from __future__ import annotations

import argparse
import csv
import json
import sqlite3
from pathlib import Path

SCHEMA = """
PRAGMA foreign_keys=ON;
CREATE TABLE sources (
  source_id TEXT PRIMARY KEY, title TEXT NOT NULL, source_class TEXT NOT NULL,
  lineage_source_id TEXT, country TEXT, period TEXT, modality TEXT, environment TEXT,
  unit TEXT, role TEXT, url TEXT, limitation TEXT, license_status TEXT
);
CREATE TABLE repositories (
  repository_id TEXT PRIMARY KEY, url TEXT NOT NULL, title TEXT NOT NULL,
  upstream_source_id TEXT, independent_database INTEGER NOT NULL,
  coverage TEXT, analysis_role TEXT, license_status TEXT, notes TEXT,
  FOREIGN KEY(upstream_source_id) REFERENCES sources(source_id)
);
CREATE TABLE metrics (
  metric_id INTEGER PRIMARY KEY AUTOINCREMENT, dataset_id TEXT NOT NULL,
  source_id TEXT NOT NULL, country TEXT, period TEXT, modality TEXT,
  environment TEXT, observation_unit TEXT, numerator REAL, denominator REAL,
  value REAL, value_type TEXT NOT NULL, metric TEXT NOT NULL, unit TEXT,
  estimate_type TEXT, uncertainty_low REAL, uncertainty_high REAL, limitation TEXT,
  FOREIGN KEY(source_id) REFERENCES sources(source_id)
);
CREATE TABLE qualitative_events (
  qualitative_id TEXT PRIMARY KEY, source_id TEXT NOT NULL, reported_period TEXT,
  topic TEXT NOT NULL, modality TEXT, environment TEXT, event_type TEXT,
  mechanism TEXT, barrier TEXT, reported_outcome TEXT, evidence_status TEXT NOT NULL,
  possible_duplicate TEXT, notes TEXT,
  FOREIGN KEY(source_id) REFERENCES sources(source_id)
);
CREATE TABLE mechanisms (
  mechanism_id INTEGER PRIMARY KEY AUTOINCREMENT, qualitative_id TEXT,
  mechanism TEXT NOT NULL, role TEXT, evidence_status TEXT,
  FOREIGN KEY(qualitative_id) REFERENCES qualitative_events(qualitative_id)
);
"""


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def as_float(value: str | None) -> float | None:
    if value in (None, "", "unknown"):
        return None
    return float(value.replace(",", "."))


def build_sources(conn: sqlite3.Connection, rows: list[dict[str, str]]) -> None:
    for r in rows:
        conn.execute(
            "INSERT OR REPLACE INTO sources VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (r["source_id"], r["title"], "public_source", None, r["country"],
             r["period"], r["modality"], r["environment"], r["unit"], r["role"],
             r["url"], r["limitation"], "not_assessed"),
        )


def build_repositories(conn: sqlite3.Connection, rows: list[dict[str, str]]) -> None:
    for r in rows:
        conn.execute(
            "INSERT OR REPLACE INTO repositories VALUES (?,?,?,?,?,?,?,?,?)",
            (r["repository_id"], r["url"], r["title"], r["upstream_source_id"],
             int(r["independent_database"]), r["coverage"], r["analysis_role"],
             r["license_status"], r["notes"]),
        )


def build_metrics(conn: sqlite3.Connection, rows: list[dict[str, str]]) -> None:
    source_alias = {
        "iatr_2020": "IATR_2020",
        "germany_boulder": "germany_boulder_2022",
        "dav_klever": "DAV_KLEVER_2025",
        "dav_klever_2025": "DAV_KLEVER_2025",
    }
    for i, r in enumerate(rows, 1):
        value = as_float(r["value"])
        metric = r["metric"]
        value_type = "proportion" if metric.endswith("_share") else "count"
        source_id = source_alias.get(r["source_id"], r["source_id"])
        conn.execute(
            """INSERT INTO metrics
            (metric_id,dataset_id,source_id,country,period,modality,environment,
             observation_unit,numerator,denominator,value,value_type,metric,unit,
             estimate_type,uncertainty_low,uncertainty_high,limitation)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (i, r["dataset_id"], source_id, r["country"], r["period"],
             r["modality"], r["environment"], r["unit"], None, None, value,
             value_type, metric, "%" if value_type == "proportion" else "records",
             "derived_summary", None, None, r["limitation"]),
        )


def build_qualitative(conn: sqlite3.Connection, ledger: Path) -> None:
    data = json.loads(ledger.read_text(encoding="utf-8"))
    for i, r in enumerate(data, 1):
        qid = f"WA-{i:04d}"
        conn.execute(
            """INSERT INTO qualitative_events VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (qid, "whatsapp_climbing_accidents_2026", r["period"], r["topic"],
             "unknown", "mixed", "near_miss" if "quase" in r["topic"].lower() else "safety_discussion",
             r["signals"], "double_check_or_procedure", r["status"],
             "reported_unverified", "not_assessed",
             "Private source; do not publish raw text or participant identifiers."),
        )
        conn.execute(
            "INSERT INTO mechanisms (qualitative_id,mechanism,role,evidence_status) VALUES (?,?,?,?)",
            (qid, r["topic"], "reported_topic", "reported_unverified"),
        )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--whatsapp-ledger", type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    repo = args.repo.resolve()
    output = args.output or repo / "data" / "climbing_accidents.sqlite"
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()
    conn = sqlite3.connect(output)
    conn.executescript(SCHEMA)
    source_rows = read_csv(repo / "data" / "source_registry.csv")
    repository_rows = read_csv(repo / "data" / "repositories.csv")
    metric_rows = read_csv(repo / "data" / "accident_summary.csv")
    build_sources(conn, source_rows)
    build_repositories(conn, repository_rows)
    build_metrics(conn, metric_rows)
    if args.whatsapp_ledger:
        conn.execute("INSERT INTO sources VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (
            "whatsapp_climbing_accidents_2026", "Private WhatsApp climbing-accident conversation",
            "private_message_capture", None, "BR", "18/08/2025–10/11/2026", "mixed",
            "mixed", "qualitative_report", "qualitative safety layer", "", "No denominator; author reports and hypotheses",
            "private_not_for_public_export"))
        build_qualitative(conn, args.whatsapp_ledger)
    conn.commit()
    counts = {table: conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
              for table in ("sources", "repositories", "metrics", "qualitative_events", "mechanisms")}
    print(json.dumps({"database": str(output), "counts": counts}, ensure_ascii=False))
    conn.close()


if __name__ == "__main__":
    main()
