.[] 
| {
    "pulseNumber": .sourceFolder | split("/")[-1],
    "pulseStart": .creationTime,
    "sampleNumber": .sourceFolder | split("/")[-2],
    "pulseDuration": .additional.pulseDuration,
    "dataCaptureStart": .additional.dataCaptureStart,
    "experimentNumber": .experimentNumber,
    "configurationUUID": .additional.configurationId,
    "pulseEnd": .additional.pulseEnd,
    "operator1": .additional.operator1,
    "operator2": .additional.operator2,
    "comment": .description,
    "pulseQuality": .additional.pulseQuality,
    "heatingInformation": .additional.heatingInformation,
    "coolantInformation": .additional.coolantInformation,
    "diagnostics": .diagnosticId,
    "thermocoupleInformation": .additional.thermocoupleInformation
  }
