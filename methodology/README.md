# Methodology

## Research question

Which acute accident patterns are documented across sport climbing, bouldering, traditional climbing and multi-pitch climbing, and which comparisons remain defensible across sources?

## Case definition

The primary unit is an acute event or acute trauma record explicitly attributable to climbing. Chronic, overuse, training and performance-related conditions are outside the primary scope.

## Source classes

| Layer | Typical unit | Valid use |
|---|---|---|
| Accident/report systems | report or event | descriptive composition and mechanisms |
| Emergency/hospital systems | visit, patient or injury | clinical profile; weighted estimates only within the same system |
| Severe-trauma registries | patient with a severity threshold | severe-trauma profile |
| Near-miss systems | incident without injury | prevention and barrier analysis |

## Harmonisation fields

Every source record should carry:

```text
source_id
country
period_start
period_end
modality
environment
unit_of_observation
case_definition
mechanism
severity
outcome
n
weighted_estimate
denominator
duplicate_risk
primary_source
limitations
```

## Aggregation rules

- Never sum reports, patients, injuries, emergency visits, rescues and near-misses as if they were the same unit.
- Never treat a GitHub fork or visualisation of AAC/ANAC as an independent sample.
- Use within-source proportions when the numerator and denominator belong to the same defined population.
- Use cross-source comparison descriptively unless definitions and denominators are demonstrably compatible.
- A global incidence estimate is not produced because no common exposure denominator is available.
- Overlapping mechanism tags are not a mutually exclusive partition; their percentages need not sum to 100%.

## Reproduction workflow

1. Inspect the source registry and verify the primary source URL.
2. Preserve the source period, country, modality and observation unit.
3. Apply the acute-accident inclusion gate.
4. Exclude overuse/performance records from the primary layer.
5. Trace derived repositories to their upstream source.
6. Deduplicate records that share AAC/ANAC lineage.
7. Calculate only the documented summary values.
8. Run `python3 scripts/validate_portfolio.py index.html`.
9. Open the resulting `index.html` in a browser and inspect the evidence section.

## Important limitations

- AAC/ANAC is a selected report archive, not a population denominator.
- NEISS is an emergency-department estimate and does not capture every accident.
- IATR is restricted to severe trauma and includes a broader mountain-accident frame.
- Country and modality coverage are uneven.
- The derived summary is reproducible as a presentation layer, not a replacement for the restricted/raw upstream datasets.
