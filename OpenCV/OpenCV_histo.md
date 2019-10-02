# OpenCV 이미지 전처리 - 히스토그램(Histogram)

> OCR(광학 문자 인식)을 사용하려고한다면 사진이 문자를 읽기 쉽게 만들어주어야한다. 그 방법 중 하나는  opencv라는 오픈소스를 활용하는 방법이다. 이번 글에서는 OpenCV를 사용해서 이미지를 전처리하는 여러가지 함수들에 대해 알아보려고 한다.



### 히스토그램 균등화(평활화)

> 히스토그램(histogram) 이란? 히스토그램은 본래 도수분포표로 x 축이 종류라면 y축이 그 종류의 개수를 나타내는 그래프를 나타낸다. 그런데 영상처리에서 히스토그램은 x축에는 0~255값, y축에는 영상에 있는 각 픽셀이 0~255사이의 값의 개수를 나타내게 된다. 일반적으로는 이미지의 밝기값 히스토그램을 사용하여 이미지의 콘트라스트를 조절하게 된다.



<img width="250" alt="Screen Shot 2019-10-03 at 1 26 22 AM" src="https://user-images.githubusercontent.com/37801041/66062834-1d7e4d00-e57d-11e9-8aa5-8208d8820fb8.png"><img width="300" alt="Screen Shot 2019-10-03 at 1 26 29 AM" src="https://user-images.githubusercontent.com/37801041/66062837-1eaf7a00-e57d-11e9-8903-c4275400fce7.png">

위의 사진을 보면 픽셀값들이 균등하지 않고 한쪽에 밀집되어있는 것을 확인할 수 있습니다.

여기서 히스토그램을 균등화를 시켜주면 더욱 대비가 심해져서 글자와 배경을 구분하기가 쉬워질것입니다.

- #### equalizeHist()

<img width="1131" alt="Screen Shot 2019-10-03 at 1 33 12 AM" src="https://user-images.githubusercontent.com/37801041/66063161-c9279d00-e57d-11e9-8741-14da4b903e06.png">

위의 사진은 ''왼쪽''이 본래 이미지 ''오른쪽''이 히스토그램 균등화를 시켜준 이미지로 contrast가 더욱 높아진 것을 확인할 수 있고 아래와 같이 히스토그램의 분포가 바뀌는 것을 확인할 수 있습니다. 

<img width="634" alt="Screen Shot 2019-10-03 at 1 35 57 AM" src="https://user-images.githubusercontent.com/37801041/66063359-2a4f7080-e57e-11e9-9c14-95986bb62f3b.png">

```python
import cv2
import numpy as np

img = cv2.imread('test.png',0)		# 이미지 읽기
equ = cv2.equalizeHist(img)				# 히스토그램 균일화
res = np.hstack((img,equ))				# 띄워줄 이미지 합치기

cv2.imshow('img', res)						# 이미지 보여주기
cv2.waitKey()
cv2.destroyAllWindows()						# esc를 누르면 창닫기
```

위의 코드와 같이 OpenCV의 `equalizeHist()` 함수를 사용하면 히스토그램을 균일화할 수 있다. 

하지만 위의 사진을 보면 균등화는 되었지만 낮은 값에 좀 많이 밀집되어 어두운 부분이 강조된 것을 볼 수 있는데 이것은 빛이 비춰진 정도에 따라 달라지게 된다. 그럼 이것을 보정하기 위해서는 어떻게 해야할까? 바로 이미지 전체를 가지고 균등화를 적용하는것이 아닌 일정한 영역들로 분리하여 영역별로 균등화를 시키는 것이다.

- #### CLAHE(Contrast Limited Adaptive Histogram Equalization)

이 함수는 위에서 언급한 것처럼 일정 영역으로 분리한 후 그 영역별로 균등화를 시켜주는 OpenCV의 함수이다.

바로 사용 결과를 확인해보자!

<img width="1132" alt="Screen Shot 2019-10-03 at 1 38 02 AM" src="https://user-images.githubusercontent.com/37801041/66063515-769ab080-e57e-11e9-95d5-ea88856ba145.png">

오른쪽의 함수를 적용한 결과를 보면 확실이 그냥 `equalizeHist()` 를 사용한 것보다 깔끔한것을 확인할 수 있다.

이 함수의 사용법은 아래와 같다.

```python
import cv2
import numpy as np
 
img = cv2.imread('test.png',0)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))	# 8*8의 크기로 영역을 나눔
cl1 = clahe.apply(img)
 
res = np.hstack((img,cl1)) 
 
cv2.imshow('img', res)
cv2.waitKey()
cv2.destroyAllWindows()
```

위의 코드는 영역을 8*8의 크기로 영역을 나누어 적용해보았다.

