. as $parent
| .diagnostics[]
| {
      "creationTime" : $parent.pulseStart,
      "type": "raw",
      "sourceFolder": "/mnt/HIVE/\(.experimentID)/\(.sampleID)/\(.pulseID)",
      "description": $parent.comment,
      "experimentID": $parent.experimentID,
      "diagnosticID": .diagnosticID,
      "additional": (del($parent.comment, $parent.experimentID, $parent.diagnostics))
  }