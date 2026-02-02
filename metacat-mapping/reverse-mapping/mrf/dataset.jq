{
  "labLocation": .additional.labLocation,
  "seid": .instrument[0],
  "seidDescription": .additional.seidDescription,
  "jobId": (.experimentNumber | split("-")[0]),
  "sessionId": (.experimentNumber | split("-")[1]),
  "sampleId": .additional.sampleId,
  "bookingStart": .creationTime,
  "bookingEnd": .additional.bookingEnd,
  "internalUser": .additional.internalUser
  "externalUser": .additional.externalUser,
  "institution": .additional.institution,
  "scientificSupport": .additional.scientificSupport,
  "notes": .description,
  "workCategory": .additional.workCategory,
  "sampleSplit": .additional.sampleSplit,
  "splitSampleId": .additional.splitSampleId,
  "tritium": .additional.tritium,
  "beryllium": .additional.beryllium,
  "betaGamma": .additional.betaGamma
}