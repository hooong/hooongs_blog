# Kakao REST API (feat.Django 카카오 로그인)

<pre>
  API(Application programming Interface)란?
  응용프로그램에서 사용할 수 있도록, 운영체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스이다.
  즉, 쉽게말해 누군가가 미리 개발해서 남들이 문서를 보고 따라할 수 있게끔 만들어놓은 것이다.  
</pre>

<pre>
  REST API란?
  Representational State Transfer API로 '대표적인 상태 전달'로 해석할 수 있으며 어떠한 자원들을 직접적으로 
  접근하는 것이 아니라 대표적으로 만들어 놓은 (JSON, XML, HTML)같은 데이터 자원의 위치를 URI로 HTTP상에서의 
  요청을 통해 접근할 수 있도록 만들어 놓은 것이다.
</pre>



- #### KakaoDevelopers 앱 생성

  - [https://developers.kakao.com](https://developers.kakao.com/)로 접속 후 카카오 계정으로 로그인하기

  - api를 사용하기 위해서는 '앱 만들기'를 통해서 앱을 생성해야한다.

    <img width="207" alt="Screen Shot 2019-08-14 at 1 00 15 AM" src="https://user-images.githubusercontent.com/37801041/62957969-c7b8de80-be30-11e9-86e1-787ae5fd7d81.png">

  - 앱의 이름과 회사명을 써주고 앱을 만들어준다.

    <img width="643" alt="Screen Shot 2019-08-14 at 12 59 52 AM" src="https://user-images.githubusercontent.com/37801041/62958110-077fc600-be31-11e9-985e-51e9d3c5e15e.png">

    (회사명은 테스트용으로 쓴다면 아무거나 써주어도 무방한 것 같습니다. ㅎㅎ)

  - 앱을 만드셨다면 아래와 같이 각종 키들이 생성된 것을 확인하실 수 있습니다. 이제 이 키들을 이용하여 api 서버와 연결을 할 것이니 남들에게 막 유출되면 안됩니다!! (저는 사용하고 바로 지울거라 상관없어요!ㅋㅋㅋ)

    <img width="443" alt="Screen Shot 2019-08-14 at 1 18 07 AM" src="https://user-images.githubusercontent.com/37801041/62958399-968cde00-be31-11e9-9c13-3c02b58a27dd.png">

  - '개발가이드' 버튼 아래에 있는 `설정` 을 눌러서 일반 설정으로 이동해줍니다.

    <img width="769" alt="Screen Shot 2019-08-14 at 1 30 06 AM" src="https://user-images.githubusercontent.com/37801041/62959188-2a12de80-be33-11e9-8332-eaef2cb81a16.png">

    <img width="476" alt="Screen Shot 2019-08-14 at 1 40 23 AM" src="https://user-images.githubusercontent.com/37801041/62959939-9215f480-be34-11e9-94fd-26a2120a31aa.png">

  - '플랫폼 추가'에서 `웹` 을 선택하고 `http://127.0.0.1:8000` 을 입력해주고 추가를 눌러줍니다. ( django로컬에서 테스트를 해보는 것이니 로컬 주소를 입력해줍니다. 만약 다른 도메인을 사용한다면 그 도메인을 입력해주시면 됩니다. )

  - 좌측메뉴에 있는 '사용자 관리' 메뉴를 클릭해주면 아래와 같은 화면이 나옵니다.

    <img width="773" alt="Screen Shot 2019-08-14 at 1 35 22 AM" src="https://user-images.githubusercontent.com/37801041/62959482-da80e280-be33-11e9-8b78-c7247731870f.png">

    <img width="766" alt="Screen Shot 2019-08-14 at 1 35 41 AM" src="https://user-images.githubusercontent.com/37801041/62959485-dc4aa600-be33-11e9-9b09-fe52831c92d8.png">

  -  사용자관리를 on으로 바꿔주시고 수집목적에는 말 그대로 수집하려는 목적을 적어 줍니다. 그리고나서 하단에 있는 저장을 눌러줍니다.  (카카오계정, 성별, 연령대 등등 필요하시면 on으로 하시면 됩니다.)

    <img width="768" alt="Screen Shot 2019-08-14 at 1 39 49 AM" src="https://user-images.githubusercontent.com/37801041/62960708-377d9800-be36-11e9-93ac-91b43b7911c6.png">

  - 바로 밑에 '로그인 Redirect URI' 설정에서 위와 같이 `http://127.0.0.1:8000/oauth` 를 입력해주시고 저장버튼을 눌러줍니다. ( 카카오 로그인을 사용하기위한 Redirect URI를 설정해주는 겁니당. )
  - 이렇게 해주시면 앱 생성과 설정까지는 완료되었습니다.

- #### 카카오 로그인 ( 앱 연결하기 )

  ```
  OAuth란?
  비밀번호를 제공하지 않고 다른 웹사이트 상의 자신들의 정보에 대해 접근 권한을 부여할 수 있는 공통적인 수단으로서 사용되는 접근 위임을 위한 개방형표준이다. 쉽게 말해서는 카카오가 아닌 다른 애플리케이션에서 카카오의 회원정보를 가져오기 위한 인증?방식이라고 할 수 있을 것 같다.
  자세한정보는 https://ko.wikipedia.org/wiki/OAuth에서 볼 수 있다.
  ```

  - 카카오 REST API는 oauth 2.0을 지원한다고 한다.

  - 간략히 카카오 로그인 절차를 설명하자면 

    ```
    code요청 -> code를 사용하여 token을 요청 -> token을 이용하여 앱 연결, 정보가져오기 등이 가능
    ```

  - 그럼 이제부터 본격적으로 REST API를 사용하여 Django에서 카카오 로그인을 만들어 보겠습니다.

  - #### 코드받기

    <img width="767" alt="Screen Shot 2019-08-14 at 2 49 57 AM" src="https://user-images.githubusercontent.com/37801041/62964578-3cdee080-be3e-11e9-842c-c4bda51bf112.png">

  - 카카오 REST API 개발가이드를 보면 위와 같이 설명이 되어있습니다.

    알기쉽게 다시 설명을 해드리면 GET 으로 `/oauth/authorize?client_id={app_key}&redirect_uri={redirect_uri}&response_type=code` 와 같은 요청을 보내면 kakao에서 client_id를 확인 후 code와 함께

    적어주는 redirect_uri ( 위의 설정에서 로그인 Redirect URI에서 설정한 uri )로 redirect를 시켜준다는 뜻입니다. ( 지금은 잘 이해가 안가셔도 코드를 따라 쳐보시면 쉽게 이해가 가실수도 있습니다. )

  - 우선, Django에서 `accounts` 앱을 만들어주고 `blog_project/urls.py` 에 url설정을 해줍니다.

    ```python
    from django.contrib import admin
    from django.urls import path, include
    import accounts.views
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', accounts.views.index, name='index'),
        path('accounts/', include('accounts.urls')),
    ]
    ```

  - 참고) 저의 프로젝트 폴더 구조입니다. ( 본인 구조에 맞춰 비교하시면서 따라하시면 됩니다. )

    ```
    .
    ├── accounts
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── templates
    │   ├── tests.py
    │   └── views.py
    ├── blog_project
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
    ```

  - Redirect URI를 `/oauth` 로 설정을 해주었으니 `accounts/views.py` 에 `oauth` 함수를 작성해줍니다.

    ```python
    from django.shortcuts import render, redirect
    
    def oauth(request):
        return redirect('index')
    ```

  - `blog_project/urls.py`에도 url을 추가해줍니다.

    ```python
    path('oauth/', accounts.views.oauth, name='oauth'),
    ```

  - 이제  code를 받아오기 위한 함수를 `accounts/views.py` 에 만들어줍니다.

    ```python
    def kakao_login(request):
        login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'
    
        client_id = '96de9a57cc579cc6b842a8f1d4bd8620'
        redirect_uri = 'http://127.0.0.1:8000/oauth'
    
        login_request_uri += 'client_id=' + client_id
        login_request_uri += '&redirect_uri=' + redirect_uri
        login_request_uri += '&response_type=code'
    
        return redirect(login_request_uri)
    ```

    - client_id : REST API 키를 입력해줍니다.
    - redirect_uri : 설정에서 '로그인 Redirect uri'에 설정해준 uri를 입력해줍니다.

  - 제대로 요청이 된다면 code를 얻어오게 됩니다.

    <img width="761" alt="Screen Shot 2019-08-14 at 11 38 41 PM" src="https://user-images.githubusercontent.com/37801041/63030066-aae1e100-beec-11e9-800c-6c10b25cc782.png">

  - 위에서 만들어놓은 `oauth` 함수에서 code를 불러와서 띄워보도록 하겠습니다.

    ```python
    def oauth(request):
        code = request.GET['code']
        print('code = ' + str(code))
    
        return redirect('index')
    ```

  - 테스트를 위하여 `index.html`에 버튼을 하나 만들겠습니다.

    ```python
    <a href="{% url 'kakao_login' %}"><button>카카오 로그인</button></a>
    ```

  - `runserver` 를 실행하고 브라우저로 접속을 한 뒤 버튼을 눌러봅니다.

    <img width="483" alt="Screen Shot 2019-08-14 at 11 59 30 PM" src="https://user-images.githubusercontent.com/37801041/63031832-a8cd5180-beef-11e9-87f2-c84d191668c3.png">

    <img width="828" alt="Screen Shot 2019-08-14 at 11 59 55 PM" src="https://user-images.githubusercontent.com/37801041/63031834-a9fe7e80-beef-11e9-845c-e37029398ee3.png">

    <img width="701" alt="Screen Shot 2019-08-15 at 12 00 05 AM" src="https://user-images.githubusercontent.com/37801041/63031837-ab2fab80-beef-11e9-9100-6b2414a86cd0.png">

  - 성곡적으로 로그인을 하고 동의를 하신 다음 '동의하고 계속하기'를 누르면 다시 index페이지로 가지는 것을 확인 하실 수 있습니다.

    <img width="1004" alt="Screen Shot 2019-08-15 at 12 03 13 AM" src="https://user-images.githubusercontent.com/37801041/63032093-1d07f500-bef0-11e9-9577-49222a9e7ab1.png">

  - 터미널창에서 확인해보시면  `code = G7jz...` 으로 제대로 코드를 받아오시는 것도 확인해볼 수 있습니다.

  - #### 토큰 받기

  - code를 받아왔으니 이제는 code를 사용해서 토큰을 받아와야 사용자 정보들을 요청할 수 있습니다.

  - 토큰에는 'Access_token'과 'Refresh_token'이 있는데 우선 'Access_token'만 얻어와 보겠습니다.

    <img width="769" alt="Screen Shot 2019-08-15 at 12 13 15 AM" src="https://user-images.githubusercontent.com/37801041/63032803-7d4b6680-bef1-11e9-9c23-3035a661118f.png">

  - 위와 같이 POST로 요청을 하면 아래와 같이 JSON 객체로 응답을 해줍니다.

    <img width="761" alt="Screen Shot 2019-08-15 at 12 14 38 AM" src="https://user-images.githubusercontent.com/37801041/63032907-ae2b9b80-bef1-11e9-93e3-75389ba353d4.png">

  - 그럼 이제 django에서 요청을 해보겠습니다.

    ```python
    def oauth(request):
        code = request.GET['code']
        print('code = ' + str(code))
    
        client_id = '96de9a57cc579cc6b842a8f1d4bd8620'
        redirect_uri = 'http://127.0.0.1:8000/oauth'
    
        access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"
    
        access_token_request_uri += "client_id=" + client_id
        access_token_request_uri += "&redirect_uri=" + redirect_uri
        access_token_request_uri += "&code=" + code
    
        print(access_token_request_uri)
    
        return redirect('index')
    ```

  - 위와 같이 `oauth` 함수에 추가를 해줍니다. 그리고 브라우저에서 카카오 로그인을 다시 해줍니다.

    <img width="586" alt="Screen Shot 2019-08-15 at 12 19 01 AM" src="https://user-images.githubusercontent.com/37801041/63033350-72450600-bef2-11e9-92e2-18a75ae7551e.png">

  - `access_token_request_uri` 가 print되는 것을 확인하실 수 있습니다. 이 uri를 띄워보면 아래와 같이 'access_token', 'refresh_token'등 각종 정보들이 json형태로 뜨는 것을 확인하실 수 있습니다.

    <img width="837" alt="Screen Shot 2019-08-15 at 12 19 49 AM" src="https://user-images.githubusercontent.com/37801041/63033334-6a856180-bef2-11e9-81ed-82bb93d1a742.png">

  - `accounts/views.py`에 있는 `oauth` 함수에 밑에 내용을 추가해줍니다.

    ```python
    import requests
    
    def oauth(request):
      ...
      access_token_request_uri_data = requests.get(access_token_request_uri)
      json_data = access_token_request_uri_data.json()
      access_token = json_data['access_token']
    
      print(access_token)
      
      return redirect('index')
    ```

    - requests.get()을 통해 access_token_request_uri에서 json객체를 받아와 줍니다.
      - requests를 사용하기 위해서는 `pip install requests` 를 통해 설치를 해주셔야합니다.
    - .json() 함수를 사용하여 json객체를 읽을 수 있게 변환해줍니다.
    - access_token에 json객체안의 'access_token'을 넣어줍니다.
    - 그리고 print를 해주면 아래와 같이 토큰을 불러오는 것을 확인할 수 있습니다.

    <img width="586" alt="Screen Shot 2019-08-15 at 12 53 17 AM" src="https://user-images.githubusercontent.com/37801041/63035960-1df05500-bef7-11e9-97b6-6bd5643347c3.png">

  - 이렇게 토큰까지 불러오는데 성공한겁니다!!!

- ### 카카오 프로필 정보 가져오기

  - 이제 앱에 연결해서 토큰까지 받아오는데 성공했습니다. 그럼 이제는 토큰을 이용하여 사용자 프로필 정보를 불러와 보도록 하겠습니다.

    <img width="768" alt="Screen Shot 2019-08-15 at 12 29 24 AM" src="https://user-images.githubusercontent.com/37801041/63034167-c1d80180-bef3-11e9-8ade-6740949eb4df.png">

  - 위와 같이 요청을 하면 사용자 프로필을 json형태로 반환을 해주게 됩니다.

    <img width="764" alt="Screen Shot 2019-08-15 at 12 31 17 AM" src="https://user-images.githubusercontent.com/37801041/63034291-02d01600-bef4-11e9-9c51-78eeecbcdb19.png">

  - 이제 django에서 프로필을 불러와보겠습니다.

  - `accounts/views.py` 에 있는 `oauth` 함수에 아래 내용을 추가해줍니다.

    ```python
    def oauth(request):
      ...
      user_profile_info_uri = "https://kapi.kakao.com/v2/user/me?access_token="
      user_profile_info_uri += str(access_token)
      print(user_profile_info_uri)
      
      return redirect('index')
    ```

  - 다시 로그인을 하고 터미널을 확인합니다.

    <img width="588" alt="Screen Shot 2019-08-15 at 12 57 57 AM" src="https://user-images.githubusercontent.com/37801041/63036336-d0c0b300-bef7-11e9-8b13-9533e2a38318.png">

  - 요청을 하려는 uri를 print해주고 print된 빨간줄의 uri를 눌러주면 아래와 같이 json 형태로 프로필 정보를 불러오는 것을 확인할 수 있습니다.

    <img width="535" alt="Screen Shot 2019-08-15 at 12 57 40 AM" src="https://user-images.githubusercontent.com/37801041/63036340-d3230d00-bef7-11e9-8b83-3a29d8f00dd2.png">

  - 이제 json 객체로 반환을 받았으니 이것을 이용해서 홈페이지에 nickname을 띄워보겠습니다.

  - `oauth` 함수에 아래 내용을 추가해줍니다.

    ```python
    def oauth(request):
      ...
      user_profile_info_uri_data = requests.get(user_profile_info_uri)
      user_json_data = user_profile_info_uri_data.json()
      user_nickname = user_json_data['properties']['nickname']
      print(user_nickname)
      
      return redirect('index')
    ```

    - `user_json_data['properties']['nickname']` 으로 nickname을 받아올 수 있습니다.

      <img width="585" alt="Screen Shot 2019-08-15 at 1 10 35 AM" src="https://user-images.githubusercontent.com/37801041/63037706-91e02c80-befa-11e9-8cf5-753acb6fedc6.png">

      - 위의 빨간줄을 보시면 닉네임을 제대로 불러온 것을 확인해보실 수 있습니다.

    - 사용자 관리 설정에서 프로필이미지나 생일, 연령 등을 허용하시면 nickname 말고도 프로필 정보들을 받아올 수 있습니다.

----

- 이렇게 카카오 REST API를 사용해서 앱에 연결하고 프로필 정보를 불러오는 것까지 해보았는데 이정도 따라하시면 REST API를 어떻게 사용하면 되는지 대충은 이해가 가실꺼라고 생각이 듭니다. 그럼 이제는 카카오디벨로퍼 사이트에서 개발가이드를 보시고도 충분히 따라하실수가 있을겁니다!!!!ㅎㅎ
- 토큰을 이용해서 프로필뿐만 아니라 나에게 메시지 보내기도 가능하고 최근에는 앱에 연결된 카카오톡 친구에게도 메시지를 보낼수도 있다고 합니다. 앱 연결해제 같은것도 혼자서 사용해보시면 좋을 것 같습니다!

