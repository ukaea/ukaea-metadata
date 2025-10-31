. as $parent
| .diagnostics
| {
      "creationTime" : $parent.pulseStart,
      "type": "raw",
      "sourceFolder": "/mnt/HIVE/\($parent.experimentId)/\($parent.sampleId)/\($parent.pulseId)",
      "description": $parent.comment,
      "experimentId": $parent.experimentId,
      "diagnosticId": .,
      "additional": ($parent | del(.comment, .experimentId, .diagnostics))
  }