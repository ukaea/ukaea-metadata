{
    "creationTime" : .pulseStart,
    "type": "raw",
    "sourceFolder": "/mnt/HIVE/\(.experimentID)/\(.sampleID)/\(.pulseID)",
    "description": .comment,
    "experimentID": .experimentID,
    "additional": (del(.comment, .experimentID))
}