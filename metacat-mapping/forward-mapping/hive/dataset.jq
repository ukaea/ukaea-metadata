. as $parent
| .diagnostics[]
| {
      "creationTime" : $parent.pulseStartTimestamp,
      "schemaVersion": $parent.schemaVersion,
      "title": "($parent.experimentNumber)-($parent.sampleNumber)-($parent.pulseNumber)",
      "ownerGroup": "HIVE",
      "owner": "HIVE",
      "accessGroups": ["HIVE"],
      "type": "raw",
      "sourceFolder": "/mnt/HIVE/E-\($parent.experimentNumber)/S-\($parent.sampleNumber)/P-\($parent.pulseNumber)",
      "description": $parent.description,
      "experimentNumber": "\($parent.experimentNumber)",
      "instrument": .,
      "additional": ($parent | del(.description, .experimentNumber, .diagnostics, .schemaVersion, .pulseStartTimestamp))
  }