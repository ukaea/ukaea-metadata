. as $parent
| .diagnostics[]
| ("E\($parent.experimentNumber)S\($parent.sampleNumber)P\($parent.pulseNumber)") as $pulsePath
| ( sort | .[0]) as $instrument
| {
      "creationTime" : $parent.pulseStart,
      "type": "raw",
      "sourceFolder": "/mnt/HIVE/E-\($parent.experimentNumber)/S-\($parent.sampleNumber)/P-\($parent.pulseNumber)",
      "description": $parent.comment,
      "experimentNumber": $parent.experimentNumber,
      "instrument": .,
      "additional": 
            ( $parent 
                | del(.comment, .experimentNumber, .diagnostics)
                | .datasetId = "\($pulsePath)\($instrument)"
            )
  }