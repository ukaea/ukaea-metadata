. as $parent
| .diagnostics[]
| {
      "creationTime" : $parent.pulseStart,
      "type": "raw",
<<<<<<< HEAD
      "sourceFolder": "/mnt/HIVE/\(.experimentID)/\(.sampleID)/\(.pulseID)",
      "description": $parent.comment,
      "experimentID": $parent.experimentID,
      "diagnosticID": .diagnosticID,
      "additional": (del($parent.comment, $parent.experimentID, $parent.diagnostics))
=======
      "sourceFolder": "/mnt/HIVE/\($parent.experimentId)/\($parent.sampleId)/\($parent.pulseId)",
      "description": $parent.comment,
      "experimentId": $parent.experimentId,
      "diagnosticId": .,
      "additional": (del($parent.comment, $parent.experimentId, $parent.diagnostics))
>>>>>>> develop
  }