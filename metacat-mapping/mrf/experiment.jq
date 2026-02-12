{
  "facility": "MRF",
  "facilityExperimentId": (.jobId) + "-" + (.sessionId),
  "startDate": .bookingStart,
  "endDate": .bookingEnd?,
  "description": .notes,
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