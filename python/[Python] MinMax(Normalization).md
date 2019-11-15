# [Python] MinMax(Normalization)

>  데이터를 처리하면서 각기 다른 데이터들이 범위가 다른 경우가 존재한다. 이러한 경우 정규화,표준화 등 데이터 전처리 과정을 통하여 범위를 같게 만들어서 처리해주는 방법이 있다.



이번 글에서는 이러한 전처리 과정들 중 MinMax에 대하여 정리해보려한다.



### MinMax

MinMax는 데이터를 일정한 범위로 오게끔 scaling을 해주는 방법이다.  대표적으로는 0과1로 변환을 하여  [0,1]을 많이 사용한다고 한다.

- MinMax 공식

  <img width="191" alt="Screen Shot 2019-11-15 at 2 49 07 PM" src="https://user-images.githubusercontent.com/37801041/68919980-318daf00-07b7-11ea-9552-061d5dcab021.png">

원래의 값에 최솟값을 뺀 후 최댓값과 최솟값의 차이로 나눠준다. 이렇게 하면 모든 값들이 0 또는 1의 값을 가지게 된다.

python코드로 보면 아래와 같다.

```python
import numpy as np

Xs = [12, 34, 55, 1, 100]

# min과 max를 구하는 과정
X = np.array(Xs)
X_min = X.min()
X_max = X.max()
X_denom = X_max - X_min

for i in range(len(X)):
  X[i] = (X[i] - X_min) // X_denom

print(X)			# [0 0 0 0 1]
```



여기서 저의 경우 0,1의 값이 아닌 0 ~ 100 사이의 값을 가지게 만들고 싶어서 아래와 같이 코드를 짰었습니다.

```python
import numpy as np

Xs = [12, 34, 55, 1, 100, 1000, 500, 380]

# min과 max를 구하는 과정
X = np.array(Xs)
X_min = X.min()
X_max = X.max()
X_denom = X_max - X_min

for i in range(len(X)):
  X[i] = (float(X[i] - X_min) / float(X_denom)) * 100
          
print(X)  		# [  1   3   5   0   9 100  49  37]
```

이렇게 0 ~ 100까지의 값으로 모든 데이터를 정규화시키니까 어떠한 범위의 값들이 들어와도 비교를 하기 쉬워졌었습니다. 