# Climbing accidents portfolio

Reproducible, evidence-bounded portfolio on acute accidents in:

- sport climbing;
- bouldering;
- traditional climbing;
- multi-pitch climbing.

## Public portfolio

- [Português](index.html)
- [English](index-en.html)
- [Español](index-es.html)
- GitHub Pages: `https://eduardo-sagi.github.io/climbing-accidents-portfolio/`

The three pages use the same evidence scope and source boundary. The English and Spanish versions are editorial translations of the portfolio; they do not add new datasets or claims.

The portfolio is an editorial interface over a federated evidence inventory. It does **not** claim a worldwide incidence, prevalence, or total number of climbing accidents.

## Scope

Included: acute traumatic accidents, falls, impact, fractures, hospitalisation, severe trauma, fatality, rescue-related outcomes, and near-misses when the source identifies them.

Excluded from the main evidence layer: overuse, chronic conditions, performance/training injuries, mountaineering, high-altitude expeditions, ice/mixed climbing, avalanche, trekking, and records without an identifiable climbing modality.

## Reproducibility boundary

The repository publishes:

- the validated static portfolio;
- the methodological scope and harmonisation rules;
- a source registry with country, period, modality, unit, outcome and limitation;
- the cross-country source comparison;
- a derived summary dataset with counts used in the visual panels;
- a validation script for the public package;
- the Pages deployment workflow.

The repository does **not** redistribute the raw AAC/ANAC workbook or hospital microdata. Those materials remain linked to their original public publishers; the derived values are documented with source, period, unit and limitation. GitHub repositories derived from AAC/ANAC are treated as lineage, not independent databases.

## Evidence model

The sources are federated into compatible layers rather than added into one total:

1. accident/report systems — AAC/ANAC, SERAC, BMC and related systems;
2. emergency/hospital attendance — NEISS and hospital cohorts;
3. severe trauma — IATR (`ISS >= 16`);
4. near-misses — systems that explicitly collect incidents without injury.

Counts can be combined only after checking case definition, period, modality, environment, observation unit, outcome and duplication risk. A report is not automatically a patient, injury, emergency visit, rescue, or accident.

## Local validation

```bash
python3 scripts/validate_portfolio.py index.html
```

The validation checks the HTML structure, navigation anchors, forbidden overuse/performance vocabulary, source links and the presence of required evidence fields.

## Provenance

See:

- [`methodology/README.md`](methodology/README.md)
- [`methodology-source-comparison.md`](methodology-source-comparison.md)
- [`data/source_registry.csv`](data/source_registry.csv)
- [`data/accident_summary.csv`](data/accident_summary.csv)
- [`data/README.md`](data/README.md)

Retrieval and triage date for this release: 2026-10-28. Source periods vary by dataset and are shown beside each estimate.

## Licence and reuse

The portfolio code and derived documentation are released under the repository licence. Upstream sources retain their own licences, copyrights and redistribution conditions. Cite the original source before citing this derived presentation.
