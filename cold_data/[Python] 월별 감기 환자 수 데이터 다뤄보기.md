# [Python] 월별 감기 환자 수 데이터 다뤄보기

> 이번 글에서는 월별로 감기를 걸리는 환자 수의 데이터를 가지고 아주 간단히 데이터를 조작하여 그래프를 그려보고 감기를 자주 걸리는 월을 찾아보고자 합니다.



### 데이터 전처리하기

> [질병 세분류(4단 상병) 통계자료](http://opendata.hira.or.kr/op/opc/olap4thDsInfo.do)를 보면 질병에 따라 월별로 내원한 환자 수에 대한 정보를 얻을 수 있습니다.

저는 KCD코드가 'J00'인 '급성 비인두염' 즉, 감기라 불리는 질병에 대해 16년 1월 ~ 18년 12월까지 총 3년치의 데이터를 조회해보았습니다. (한번에 최대 3년치까지 조회가 가능하다고 합니다.)

<img width="946" alt="Screen Shot 2019-11-06 at 10 49 16 PM" src="https://user-images.githubusercontent.com/37801041/68303701-bd347b00-00e7-11ea-9358-e2bf03517be0.png">

조회를 하면 그래프들도 나오지만 밑에 보면 엑셀파일을 받을 수 있습니다. 그럼 엑셀 파일을 받아보겠습니다.

<img width="930" alt="Screen Shot 2019-11-06 at 10 52 05 PM" src="https://user-images.githubusercontent.com/37801041/68303880-11d7f600-00e8-11ea-9861-e32e16268f84.png">

여기서 원래는 날짜들이 '2017년 1월'과 같은 형식을로 나오지만 데이터를 건드리기 쉽게 '17_1'과 같은 형식으로 바꾸고 한글같은 경우에 인코딩문제가 발생할수도 있으므로 필요한 데이터를 영어로 바꿔주었습니다. 또한 숫자의 경우 형식이 숫자로 되어서 '1,000'과 같은 식으로 반점이 들어가는데 이것도 형식을 일반으로 바꾸어서 반점을 없애주었습니다.

수정을 다하고 '다른이름으로 저장'을 사용해 `.csv`파일 형식으로 저장을 해주었습니다.



### python 파일에서 csv파일 읽기

> 데이터를 가공할때는 jupyter Notebook를 활용하면 결과들을 바로 확인할 수 있어 편리합니다.

Jupyter Notebook을 사용하여 python파일 하나를 새로 만들어 줍니다.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

j00_data = pd.read_csv('./j00_1601_1812.csv')   # ''안에는 csv 파일의 위치를 써주면 됩니다.
print(j00_data)
```

<img width="712" alt="Screen Shot 2019-11-06 at 11 04 27 PM" src="https://user-images.githubusercontent.com/37801041/68304763-ca526980-00e9-11ea-80f1-33a700f7d874.png">

이렇게하면 csv파일을 읽어와서 pandas의 DataFrame으로 만들어지게 됩니다.

> Jupyter Notebook tip: `ctrl + enter` : 현재 지정 박스 실행, `shift + enter` : 현재 박스를 실행하고 밑으로 이동 (밑에 아무것도 없다면 새로 만들어지고 이동)



### 필요한 정보만 빼내기

> 환자 수의 데이터들만 필요하므로 환자 수의 데이터를 골라내고 같은 월별 환자수는 모두 더해줍니다.

```python
data_month = []					# 월별 총 환자 수를 담을 list

for i in range(1,13):		# 1월부터 12월까지 반복
    list_mon = []				
    for m in [16,17,18]:	
        list_mon.append(str(m)+'_'+str(i))		# '16_1'과 같이 년도별 월의 환자 수를 가져오기 위함

    data_mon = pd.DataFrame()									# 월별 환자 수만 저장하기 위한 DataFrame
    for j in list_mon:
        data_mon.loc[:,j] = j00_data[:22][j]
    
    data_mon = data_mon[1:].astype('int')			# 숫자들을 int type으로 변환
    data_month.append(data_mon.sum(axis=1)[1])	# 행을 더해서 월별 총 환자 수를 구함

	
data_month = np.array(data_month)						# numpy로 배열을 만들면 아래에서 처럼 전체값에 대한 연산이 가능해진다.			
data_mon_avg = (data_month // 3) // 10000   # 0~100까지의 값만 사용하기 위해 나눔

print(data_mon_avg)			# 월별 평균 환자 수 데이터 형성
```



- 코드의 설명을 보충하자면 

  ```python
  j00_data[:22]['16_1']
  ```

  위의 코드는 아래의 `j00_data`를 보면 네모박스 부분의 22행까지와 같다.

  <img width="627" alt="Screen Shot 2019-11-06 at 11 17 56 PM" src="https://user-images.githubusercontent.com/37801041/68305982-ff5fbb80-00eb-11ea-9a06-49f9b3ee62c5.png">

  

### matplotlib를 이용해 그래프 그리기

> matplotlib를 활용하면 데이터를 가지고 여려 종류의 그래프들을 그려볼 수 있다.

```python
month = ['01','02','03','04','05','06','07','08','09','10','11','12']
plt.plot(month,data_mon_avg,color='red',marker='o',linestyle='solid')		# plot을 생성
plt.title('Cold')		# 그래프의 이름
plt.xlabel('Month')					# x축의 이름
plt.ylabel('Avg_Patients')	# y축의 이름
plt.show()				# 그래프 보이기
```

<img width="717" alt="Screen Shot 2019-11-06 at 11 25 38 PM" src="https://user-images.githubusercontent.com/37801041/68306363-c2e08f80-00ec-11ea-9e0e-40889177f1d8.png">

3년치의 감기를 걸리는 월별 평균 환자 수는 위의 그래프와 같다.

<img width="580" alt="Screen Shot 2019-11-06 at 11 26 31 PM" src="https://user-images.githubusercontent.com/37801041/68306427-e3a8e500-00ec-11ea-88e8-35d3551295d3.png">

위의 그래프와 비교를 해보았다. 3년동안 그래프의 추이가 거의 다 비슷했고 이를 바탕으로 사람들은 11~3월정도까지 감기에 많이 걸리며 7~8월에는 아주 적게 감기에 걸린다는 정보를 유추해낼 수 있었다.

