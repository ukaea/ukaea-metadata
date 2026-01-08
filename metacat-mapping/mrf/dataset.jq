{
  "contactEmail": (.internalUser[0].email // .scientificSupport[0].email?),
  "creationTime" : .bookingStart,
  "type": "raw",
  "sourceFolder": "/mnt/MRF/\(.jobId)/\(.seid)/\(.sessionId)",
  "description": .notes,
  "experimentNumber": "\(.jobId)-\(.sessionId)",
  "instrument": [.seid],
  "additional": (. | del(.notes, .seid))
}