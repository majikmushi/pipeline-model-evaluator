---
schema_version: 1
model_id: example-pipeline
---
# Example pipeline

```yaml pipeline-definition
kind: artifact
id: DS-01
aliases: [raw_text]
schema_ref: plain-text
```

```yaml pipeline-definition
kind: artifact
id: DS-02
```

```yaml pipeline-definition
kind: capability
id: segmentation
```

## Segmenter

```yaml pipeline-definition
kind: processor
id: P01
consumes: [raw_text]
produces: [DS-02]
provides_capabilities: [segmentation]
implementation:
  state: conceptual
  deterministic: true
```
