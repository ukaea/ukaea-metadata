. as $parent
| .diagnostics[]
| {
      "creationTime" : $parent.pulseStart,
      "type": "raw",
      "sourceFolder": "/mnt/HIVE/\($parent.experimentNumber)/\($parent.sampleNumber)/\($parent.pulseNumber)",
      "description": $parent.comment,
      "experimentNumber": $parent.experimentNumber,
      "instrument": .?,
      "additional": ($parent | del(.comment, .experimentNumber, .diagnostics))
  }