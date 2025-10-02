. as $parent
| .diagnostics[]
| {
      "creationTime" : $parent.pulseStart,
      "type": "raw",
      "sourceFolder": "/mnt/HIVE/\(.experimentId)/\(.sampleId)/\(.pulseId)",
      "description": $parent.comment,
      "experimentID": $parent.experimentId,
      "diagnosticID": .diagnosticId,
      "additional": (del($parent.comment, $parent.experimentId, $parent.diagnostics))
  }