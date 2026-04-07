{
  "contactEmail": (.scientificSupport[0].email // .internalUser[0].email?),
  "creationTime" : .bookingStart,
  "type": "raw",
  "sourceFolder": "/mnt/MRF/\(.jobId)/\(.seId)/\(.sessionId)",
  "description": "",
  "experimentNumber": "\(.jobId)-\(.sessionId)",
  "instrument": [.seId],
  "schemaVersion": (.schemaVersion // "1.0.0"),
  "ownerGroup": "MRF",
  "accessGroups": ["MRF"],
  "additional": (. | del(.seId, .bookingStart, .jobId, .sessionId, .schemaVersion))
}