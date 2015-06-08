library(jsonlite)

lines <- readLines("open-thesaurus/Thesaurus_es_ES.txt")
lines <- lines[9:length(lines)]

splitted <-  strsplit(lines, split=";", fixed=TRUE)

json <- toJSON(splitted)
write(json, file='sinonimos.json')
