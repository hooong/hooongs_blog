#  [TOY_Project] 얼굴 인식으로 나이 확인하기
>  Kakao에서 제공하는 vision API는 사람 얼굴을 인식하고 남성 혹은 여성인지 나이는 어느정도인지를 예측해준다.
>
> 따라서 나는 이 API를 활용해서 사용자가 자신의 얼굴을 찍어올리고 실제 나이를 입력해주면 얼굴로 본 나이가 실제 나이와 얼마나 차이나는지, 남자인지 여자인지를 알려준다. 어디까지나 나이 인식은 아주 정확하지 않으므로 재미로 보기만 해야한다…ㅎㅎ



### kakao vision API

>  django로 개발을 했으며 API는 REST로 요청을 보내서 활용하였다.



```python
# 나이예측
def predictAge(request, filename):

   # 저장되어있는 사진의 경로를 변수에 저장
   faceImg = Face_img.objects.get(fileName=filename)
   faceImgfile = os.path.join(settings.BASE_DIR, ‘media/‘+str(faceImg.faceImg))
   realAge = faceImg.realAge

   # request를 보낼 정보들
   API_URL = ‘https://kapi.kakao.com/v1/vision/face/detect’
   APP_KEY = config_secret_common[‘django’][‘kakaokey’]
   headers = {‘Authorization’: ‘KakaoAK {}’.format(“app_key를 넣어줌.”)}
   file = { ‘file’ : open(faceImgfile, ‘rb’)}

   # requests를 통하여 api에 POST로 요청을 보냄
   result = requests.post(API_URL, headers=headers, files=file)

   # 저장되어있던 사진 model과 media파일을 삭제
   os.remove(faceImgfile)
   faceImg.delete()

	# response를 json형태로 변환
   faceInfo_all = result.json()

   # 만약 얼굴을 제대로 인식을 못한다면 ‘result’에는 ‘width’,’height’정보만 남음.
   if len(list(faceInfo_all[‘result’])) == 2:
       return redirect(‘error’)

   faceInfo = faceInfo_all[‘result’][‘faces’][0][‘facial_attributes’]
   gender = faceInfo[‘gender’]
   m = float(gender[‘male’])
   f = float(gender[‘female’])
   if m > f:
       gender = ‘m’
   else:
       gender = ‘f’

   age = faceInfo[‘age’]
   age = str(round(float(age))) # 나이 반올림 (재미이므로 정확 X)

   tmp_predict = Predict_age()
   tmp_predict.predictAge = age
   tmp_predict.realAge = realAge 
   tmp_predict.save()

   return redirect(‘/hoay/result/‘ + str(gender) + ‘/‘ + str(age) + ‘/‘ + str(realAge))
```

- [kakao Developers](https://developers.kakao.com/docs/restapi/vision) 에 나와있는 REST API 설명서를 기반으로 request요청을 보냈다.

- response를 받아 json형태를 확인하고 내가 필요한 ‘gender’, ‘age’ 정보만 빼냈다.

- 얼굴을 제대로 인식하지 못하였다면 error페이지로 redirect시킴.



### 얼굴 사진, 실제나이 입력 후 결과 확인

> 아직 프론트를 제대로 꾸미지 않았습니다...



- 나이와 사진 입력 화면

<img width="505" alt="Screen Shot 2020-01-08 at 5 54 02 PM" src="https://user-images.githubusercontent.com/37801041/71964129-5a26a800-3240-11ea-96a6-c3fd7f77e46b.png">



- 나이를 예측하고 실제 나이와 얼마나 차이나는지를 알려주는 결과 화면

<img width="412" alt="Screen Shot 2020-01-08 at 5 54 32 PM" src="https://user-images.githubusercontent.com/37801041/71964134-5b57d500-3240-11ea-97d2-790c4a57938f.png">



- 얼굴을 제대로 인식하지 못하였을 경우 알려주는 에러 화면. (Feat. 다시시도)

<img width="518" alt="Screen Shot 2020-01-08 at 5 56 35 PM" src="https://user-images.githubusercontent.com/37801041/71964136-5bf06b80-3240-11ea-8260-ed55a952fccc.png">



## 끝을 맺으며

일단 사진을 업로드 받으면 서버내에 저장을 거치고나서 api에 넘긴다음 삭제를 하는데 여기서 개인정보인 사진이 서버에 잠깐이라도 머문다는게 살짝 문제가 될 것 같다. 그래서 그냥 업로드를 바로 api쪽으로 해보고 싶었는데 이걸 아직 구현하지 못한 점이 너무 아쉬웠다...