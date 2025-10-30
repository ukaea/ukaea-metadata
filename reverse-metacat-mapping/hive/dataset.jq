.[0] 
| {
    "pulseId": .sourceFolder | split("/")[-1],
    "pulseStart": .creationTime,
    "sampleId": .sourceFolder | split("/")[-2],
    "pulseDuration": .additional.pulseDuration,
    "dataCaptureStart": .additional.dataCaptureStart,
    "experimentId": .experimentId,
    "configurationId": .additional.configurationId,
    "pulseEnd": .additional.pulseEnd,
    "operator1": .operator1,
    "operator2": .operator2,
    "comment": .description,
    "pulseQuality": .additional.pulseQuality,
    "heatingInformation": .additional.heatingInformation,
    "coolantInformation": .additional.coolantInformation,
    "diagnostics": .diagnostics
  }
