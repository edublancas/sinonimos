import json
ls = {}
with open('sinonimos.json', encoding="utf-8") as json_file:
    data = json.load(json_file)
    for list in data:
      list = [x.strip().lower() for x in list]
      key = list.pop(0).lower()
      ls[key] = list

# write ls to disk 
with open('sinonimos2.json', 'w', encoding="utf-8") as outfile:
    json.dump(ls, outfile, indent=2, ensure_ascii=False)
