# Climbing accidents data contract v2

## Design rule

The database is a federated evidence inventory, not one pooled accident count. A record is never comparable merely because it contains the word `accident`.

## Evidence layers

- `accident_report`: published or voluntary event report (AAC/ANAC, SERAC, etc.).
- `emergency_visit`: emergency-department encounter or weighted estimate (NEISS).
- `hospital_cohort`: patients/injuries from a clinical cohort.
- `severe_trauma_patient`: patient meeting a severity threshold (IATR).
- `near_miss`: incident without confirmed injury.
- `qualitative_report`: private/public narrative, hypothesis or safety discussion.
- `aggregate_metric`: published/derived summary value without one row per event.

## Core entities

### `sources`

`source_id`, `title`, `source_class`, `lineage_source_id`, `country`, `period`, `modality`, `environment`, `unit`, `role`, `url`, `limitation`, `license_status`.

`lineage_source_id` is mandatory for GitHub-derived data when the repository is not independent from AAC/ANAC or another upstream source.

### `events`

One row per identifiable event only when the source supports event-level identity:

`event_id`, `source_id`, `upstream_record_id`, `event_date`, `publication_date`, `country`, `region`, `location`, `modality`, `environment`, `event_type`, `observation_unit`, `severity_class`, `fatality`, `hospitalization`, `rescue_involved`, `evidence_status`, `confidence`, `duplicate_group_id`, `notes`.

### `metrics`

For aggregated studies and current portfolio panels:

`metric_id`, `dataset_id`, `source_id`, `country`, `period`, `modality`, `environment`, `observation_unit`, `numerator`, `denominator`, `value`, `value_type`, `metric`, `unit`, `estimate_type`, `uncertainty_low`, `uncertainty_high`, `limitation`.

Never put patients, injuries, reports and emergency visits into an undifferentiated `n_or_estimate` field.

### `mechanisms`

Many-to-many relation between events and mechanisms:

`event_id`, `mechanism`, `role`, `evidence_status`, `source_note`.

### `qualitative_events`

Private or narrative layer; not part of public pooled totals:

`qualitative_id`, `source_id`, `reported_period`, `topic`, `modality`, `environment`, `event_type`, `mechanism`, `barrier`, `reported_outcome`, `evidence_status`, `possible_duplicate`, `notes`.

### `repositories`

`repository_id`, `url`, `title`, `upstream_source_id`, `independent_database`, `coverage`, `analysis_role`, `license_status`, `notes`.

## Controlled values

- `event_type`: `accident`, `incident`, `near_miss`, `rescue`, `safety_discussion`.
- `modality`: `sport_climbing`, `bouldering`, `traditional`, `multi_pitch`, `mixed_climbing`, `unknown`.
- `environment`: `indoor`, `outdoor`, `urban_hospital`, `mountain_remote`, `mixed`, `unknown`.
- `evidence_status`: `published`, `primary_register`, `derived_dataset`, `reported_unverified`, `hypothesis`, `context_only`.
- `confidence`: `high`, `medium`, `low`, `not_assessed`.
- `value_type`: `count`, `proportion`, `rate`, `estimate`.

## Public/private boundary

Raw WhatsApp exports, participant identifiers, message text and private event-level details remain outside the public repository. A public safety layer may contain only generalized, non-identifying barrier categories after Eduardo explicitly authorizes publication of private-source-derived material.
