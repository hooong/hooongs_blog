import json

with open('./test.json','r') as f:  	# 'r'은 읽기모드를 의미한다.
  json_data_before = json.load(f)

print(json.dumps(json_data_before,indent='\t'))
  
F000 = {"number": "3"}
json_data_before["F000"] = F000

with open('./test.json','w',encoding='utf-8') as mk_f:
    json.dump(json_data_before,mk_f,indent='\t')

with open('./test.json','r') as f:
  json_data_after = json.load(f)

print(json.dumps(json_data_after,indent='\t'))