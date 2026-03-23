. as $parent
| .diagnostics[]
| {
      "creationTime" : $parent.pulseStartTimestamp,
      "schemaVersion": $parent.schemaVersion,
      "ownerGroup": "HIVE",
      "owner": "HIVE",
      "accessGroups": ["HIVE"],
      "type": "raw",
      "sourceFolder": "/mnt/HIVE/E-\($parent.experimentNumber)/S-\($parent.sampleNumber)/P-\($parent.pulseNumber)",
      "description": $parent.comment,
      "experimentNumber": $parent.experimentNumber,
      "instrument": .,
      "additional": ($parent | del(.comment, .experimentNumber, .diagnostics, .schemaVersion, .pulseStartTimestamp))
  }