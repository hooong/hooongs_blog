import json

disease = dict()

F09 = {"number": "1"}
F072 = {"number": "2"}
F000 = {"number": "3"}

disease["F09"] = F09
disease["F072"] = F072
disease["F000"] = F000

with open('./test2.json', 'w', encoding='utf-8') as mk_f:
    json.dump(disease, mk_f, indent='\t')

with open('./test2.json', 'r') as f:
    json_data = json.load(f)

print(json.dumps(json_data,indent='\t'))