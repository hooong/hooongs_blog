# OpenCV-python

python에서 OpenCV를 사용하는 방법을 알아보자!

`pip install opencv-python`

위의 명령어를 통해서 opencv를 install할 수 있다.

그 후 코드에서 사용하려면

`import cv2` 를 써주면 된다.



아래는 OpenCV의 사용 예이다.

```python
import cv2

img = cv2.imread('파일경로', cv2.IMREAD_GRAYSCALE) # '파일경로'의 이미지를 grayscale로 읽어온다.

cv2.imshow('image', img)		# 'image'라는 타이틀을 가지고 윈도우에 img를 띄워준다.
cv2.waitkey(0)							# 0값을 넣어주면 key입력이 있을때까지 무한대기.
cv2.destroyAllWindows()			# 모든 윈도우를 종료.

cv2.imwrite('mod.png', img)	# 'mod.png'라는 이름으로 img를 새로 저장한다.
```



