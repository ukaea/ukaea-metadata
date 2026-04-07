{
  "contactEmail": (.internalUser[0].email // .scientificSupport[0].email?),
  "creationTime" : .bookingStart,
  "type": "raw",
  "sourceFolder": "/mnt/MRF/\(.jobId)/\(.seid)/\(.sessionId)",
  "description": .notes,
  "experimentNumber": "\(.jobId)-\(.sessionId)",
  "instrument": [.seid],
  "schemaVersion": (.schemaVersion // "1.0.0"),
  "ownerGroup": "MRF",
  "accessGroups": ["MRF"],
  "additional": (. | del(.notes, .seid, .bookingStart, .jobId, .sessionId))
}