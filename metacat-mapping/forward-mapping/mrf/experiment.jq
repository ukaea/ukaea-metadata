{
  "facility": "MRF",
  "facilityExperimentId": (.jobId) + "-" + (.sessionId),
  "startDate": .bookingStart,
  "endDate": .bookingEnd?,
  "description": .notes,
  "schemaVersion": (.schemaVersion // "1.0.0"),
  "ownerGroup": "MRF",
  "accessGroups": ["MRF"],
  "leadInvestigator": (.internalUser[0] // .scientificSupport[0])
  +
  ( if (.institution and .externalUser) then
        { customer: {
            organisation: .institution,
            contactPerson: .externalUser[0]
        }}
    else
        {}
    end
  )
}