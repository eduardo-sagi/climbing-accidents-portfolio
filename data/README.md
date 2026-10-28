# Data notes

`accident_summary.csv` is a derived, presentation-level summary. It is not a raw accident database and must not be interpreted as an incidence table.

Each row preserves:

- source and provenance;
- country and period;
- modality and environment;
- observation unit;
- numerator/estimate;
- metric;
- principal limitation.

The `aac_anac_ecaroom` rows derive from the public ecaroom/AAC/ANAC lineage and are not independent of the AAC archive. Mechanism tags can overlap, so they are not mutually exclusive categories.

Raw upstream files are intentionally not redistributed here. Rebuilds should start from the source URLs in `source_registry.csv`, respecting each source's licence and access conditions.
