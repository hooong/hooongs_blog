# [Python] Json파일 다루기

> 프로젝트를 진행중에 데이터를 json형식으로 다루어야 될 일이 생겼다.
>
> json이란, JavaScript Object Notation의 약자로, 데이터 교환 포맷 중 하나입니다. xml에 비해 경량화되어 있다는게 특징입니다.



#### python에서 json파일 열어서 읽기

- 아래와 같은 json파일이 './test.json'의 경로에 있다고 해보자.

  ```json
  {
      "F09": {
        "number": "1"
      },
      "F072": {
        "number": "2"
      }
  }
  ```



- python코드에서 아래와 같이 작성하면 json파일을 읽어올 수 있다.

   ```python
  import json
  
  with open('./test.json','r') as f:  	# 'r'은 읽기모드를 의미한다.
    json_data = json.load(f)
    
   print(json.dumps(json_data, indent='\t'))
   ```

  - 출력

  ```
  {
          "F09": {
                  "number": "1"
          },
          "F072": {
                  "number": "2"
          }
  }
  ```

  

- 특정 속성의 값을 가져오기 위해서는 아래와 같이 하면된다.

  >python의 dictionary와 같은 방식으로 접근이 가능하다.

  ```python
  print(json_data['F09'])
  print(json_data['F09']['number'])
  ```

  - 출력

  ```
  {'number': '1'}
  1
  ```



#### python에서 json파일 쓰기

- 위에와 같은 json파일을 `test2.json`로 만드는 코드는 아래와 같다.

  ```python
  import json
  
  disease = dict()
  
  F09 = {"number": "1"}
  F072 = {"number": "2"}
  
  disease["F09"] = F09
  disease["F072"] = F072
  
  # 쓰기모드로 파일을 연 뒤 dictionary를 써준다.
  with open('./test2.json', 'w', encoding='utf-8') as mk_f:
      json.dump(disease, mk_f, indent='\t')
  
  # 파일을 읽어본다.
  with open('./test2.json', 'r') as f:
      json_data = json.load(f)
  
  print(json.dumps(json_data,indent='\t'))
  ```

  - 출력

  ```
  {
          "F09": {
                  "number": "1"
          },
          "F072": {
                  "number": "2"
          }
  }
  ```

  

#### json파일 수정하기

- 다른 방법이 있을수도 있지만 저의 경우에는 아래와 같이 진행했습니다.

  1. 원래 파일을 읽는다.
  2. 원래 파일의 내용을 변수에 저장한다.
  3. 변수의 내용을 가지고 수정을 한다.
  4. 위에서 파일 쓰기를 다시 해준다.

  ```python
  import json
  
  with open('./test.json','r') as f:
    json_data_before = json.load(f)
  
  print(json.dumps(json_data_before,indent='\t'))
    
  F000 = {"number": "3"}
  json_data_before["F000"] = F000
  
  with open('./test.json','w',encoding='utf-8') as mk_f:
      json.dump(json_data_before,mk_f,indent='\t')
  
  with open('./test.json','r') as f:
    json_data_after = json.load(f)
  
  print(json.dumps(json_data_after,indent='\t'))
  ```

  - 출력

  ```
  - 변경 전 읽은 파일
  {
          "F09": {
                  "number": "1"
          },
          "F072": {
                  "number": "2"
          }
  }
  
  - 변경 후 읽은 파일
  {
          "F09": {
                  "number": "1"
          },
          "F072": {
                  "number": "2"
          },
          "F000": {
                  "number": "3"
          }
  }
  ```



----

##### 이렇게 python에서 json파일을 읽고, 쓰고, 수정하는 방법에 대해 정리를 해보았다.