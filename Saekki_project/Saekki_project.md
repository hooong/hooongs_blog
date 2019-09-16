# 약속에 늦지않는 새끼(Toy_Project)

>친구들이랑 약속을 하면 약속시간이 되어서야 침대에서 일어나는 친구들이 있다.
>
>이러한 친구들에게 따끔한 맛을 보여주기 위해 약속을 지키게 만드는 서비스를 만들자 생각을 했다.
>
>메인 기능으로는 친구들과 약속을 만들고 위치를 확인하여 시간안에 지정된 장소안에 도착해야 한다.
>
>또 약속을 만들때 벌금을 설정하거나 엽사를 걸게끔 설정이 가능하여 약속에 늦으면 벌금을 물거나
>
>'수배자 메뉴'에 엽사가 전체 공개가 되어버린다.



- 데스크탑 모드

<img width="1302" alt="Screen Shot 2019-09-15 at 6 27 45 PM" src="https://user-images.githubusercontent.com/37801041/64919515-b0ca2b00-d7e6-11e9-9a6e-90429293cee8.png">

- 반응형으로 만든 모바일모드

<img width="500" alt="Screen Shot 2019-09-15 at 6 28 01 PM" src="https://user-images.githubusercontent.com/37801041/64919520-bfb0dd80-d7e6-11e9-830e-5d343b4847c9.png">



# 개발환경

- Django / Python3
- Html / Css / Js
- AWS - EC2(Ubuntu 16.04.6) : 서버
- AWS - RDS(PostgreSQL) : DB
- AWS - S3 : static파일과 media파일들을 관리해준다.



## 카카오 로그인

- 카카오의 REST API를 사용

<img width="400" alt="Screen Shot 2019-09-16 at 1 48 45 PM" src="https://user-images.githubusercontent.com/37801041/64934939-e162a100-d888-11e9-8c2b-635c4188603c.png">

> 원래는 카카오로그인 외에도 기존 회원가입과 로그인을 넣으려 했지만 카카오 로그인으로만 하면 관리도 쉽고 다른 로그인의 필요성을 많이 느끼지 못해서 카카오 로그인만 남겼다.

<img width="929" alt="Screen Shot 2019-09-16 at 1 57 40 PM" src="https://user-images.githubusercontent.com/37801041/64935103-f7249600-d889-11e9-8a61-9f66b46303d6.png">

> 카카오 로그인을 하게되면 uid에 카카오서버에서 넘어오는 고유의 id값을 넣어주고 name에는 이름을 지정해준다. 
>
> *** Django Auth는 처음에 username이 고유필드인데 이 필드에 카카오에서 넘어오는 이름을 사용하면 동명이인이 카카오로그인을 할 시 문제가 생길 수 있다.  ***
>
> 이외에도 카카오서버에서 프로필 사진과 썸네일을 받아오며 상태메시지는 초기값을 남겨두고 추후에 마이페이지에서 수정할 수 있게끔 만들어놓았다.
>
> <img width="750" alt="Screen Shot 2019-09-15 at 6 27 25 PM" src="https://user-images.githubusercontent.com/37801041/64935172-95186080-d88a-11e9-8f86-9734a3bc85ad.png">



## 친구 검색 / 신청 / 수락

- 친구 검색 메뉴

<img width="1023" alt="1Screen Shot 2019-09-16 at 2 06 02 PM copy" src="https://user-images.githubusercontent.com/37801041/64935486-8d59bb80-d88c-11e9-85f5-05767b1dc8cc.png">

> 검색이 없을때는 모든 유저들이 뜨며 친구신청을 할 수 있게 버튼을 만들어 놓았다.

- 친구 검색

<img width="1013" alt="Screen Shot 2019-09-16 at 2 09 32 PM" src="https://user-images.githubusercontent.com/37801041/64935526-c1cd7780-d88c-11e9-97ae-f4ec6e3452f1.png">

> 이름으로 검색이 가능하고 `filter(name__icontains=q)` models에 있는 filter를 이와 같이 씀으로 q가 포함되어있으면 필터링을 해주는 것을 이용해 검색을 구현하였다. 예를들면 '홍석준'을 찾으려면 '홍'만 검색해도 뜨게끔했다.

- 친구 신청

<img width="1012" alt="Screen Shot 2019-09-16 at 2 09 41 PM" src="https://user-images.githubusercontent.com/37801041/64935611-28eb2c00-d88d-11e9-96fc-db10ddb6bf33.png">

> 친구신청버튼을 누르면 요청중으로 바뀌며 상대방이 수락을 할때까지는 친구가 될 수 없다.

- 친구 신청 알림

<img width="310" alt="Screen Shot 2019-09-16 at 2 09 57 PM" src="https://user-images.githubusercontent.com/37801041/64935626-43bda080-d88d-11e9-829d-ec6bbf6c8061.png">

> 친구 신청이 오게되면 알림창에 수락/거절이 있는 알림이 뜨게되고 비로소 수락을 누르면 친구가 되고 거절을 누르면 요청이 삭제가 된다.



##약속 만들기

1. **약속의 제목과 약속에 대한 간략 설명을 작성 --> 같이 약속한 친구 선택**

   > 여기서 같이 약속한 친구들을 고르게 되는데 여기선 모든 유저가 뜨는게 아니고 친구인 상태인 유저들만 나타나고 약속에 친구들을 초대하게되면 친구들은 약속에 초대 알림을 받게되고 수락을 누르면 약속에 참여가 된다.

<img width="810" alt="Screen Shot 2019-09-15 at 6 24 37 PM" src="https://user-images.githubusercontent.com/37801041/64919621-05ba7100-d7e8-11e9-9040-330bae508aba.png">

2. **약속 날짜 및 시간 설정하기**

<img width="810" alt="Screen Shot 2019-09-15 at 6 25 03 PM" src="https://user-images.githubusercontent.com/37801041/64919644-369aa600-d7e8-11e9-8c01-ab0de3c5349b.png">

3. **약소 장소 설정하기**

<img width="810" alt="Screen Shot 2019-09-15 at 6 25 38 PM" src="https://user-images.githubusercontent.com/37801041/64919659-6b0e6200-d7e8-11e9-8830-12d92a6dd7c5.png">

4. **벌칙 설정하기**

   - 벌금

     <img width="810" alt="Screen Shot 2019-09-15 at 6 25 55 PM" src="https://user-images.githubusercontent.com/37801041/64919681-a6a92c00-d7e8-11e9-85b3-d01b0928f558.png">

     - 시간당

       <img width="810" alt="Screen Shot 2019-09-15 at 6 25 59 PM" src="https://user-images.githubusercontent.com/37801041/64919685-ac9f0d00-d7e8-11e9-8881-749947370fca.png">

     - 1회성 벌금

       <img width="810" alt="Screen Shot 2019-09-15 at 6 26 06 PM" src="https://user-images.githubusercontent.com/37801041/64919755-980f4480-d7e9-11e9-9c8a-14e2a9ebcf39.png">

   - 엽사 공개

     >글을 쓰는 사람은 글쓰기에서 엽사를 등록하고 참여인원으로 선택된 사람들은 약속에 초대되는 순가 알림이 가게 되고 그 알림에서 약속 수락을 하게되면 자동으로 엽사를 올려야하는 창으로 가게되고 엽사를 올려야만 약속수락을 할 수 있게끔 만들었다.

     <img width="810" alt="Screen Shot 2019-09-15 at 6 26 17 PM" src="https://user-images.githubusercontent.com/37801041/64919763-b412e600-d7e9-11e9-97c9-301303def6bc.png">

- 약속이 잘 만들어졌다.

<img width="799" alt="Screen Shot 2019-09-15 at 6 51 51 PM" src="https://user-images.githubusercontent.com/37801041/64919787-e886a200-d7e9-11e9-975b-9050811a2765.png">

> 약속은 django의 apscheduler라는 모듈을 사용해서 1분단위로 계속 확인하며 지정해 놓은 약속시간이 지나면 '진행중인 약속'에서 '시간이 지난 약속'으로 업데이트가 된다. 또 진행중인 약속들중에 내가 도착을 했는지 안했는지의 여부를 알려주기위해 오른쪽 상단에 도착과 미도착을 알려준다.



## 약속 도착

<img width="1136" alt="Screen Shot 2019-09-16 at 2 26 56 PM" src="https://user-images.githubusercontent.com/37801041/64935804-20dfbc00-d88e-11e9-91b6-e38a370653b3.png">

> '도착하셨으면 여기를 눌러주세요!'를 누르면 현재위치를 찾고 지정된 장소 50m안에 있다면 도착이 완료된다.
>
> *** html5의 위치를 불러오는 api인 Geolocation을 사용하는데 https를 사용하지않으면 사용할 수 없고 정확도에 따라 속도가 달라져 조금 느린경우가 꽤 있었다... ***

<img width="1135" alt="Screen Shot 2019-09-16 at 2 27 06 PM" src="https://user-images.githubusercontent.com/37801041/64935864-48368900-d88e-11e9-808b-78fbcd6b2323.png">

----

<img width="1123" alt="Screen Shot 2019-09-16 at 2 27 18 PM" src="https://user-images.githubusercontent.com/37801041/64935917-68664800-d88e-11e9-8d09-4c6ce89088e8.png">

> 도착을 성공한다면 버튼에 '도착을 하셨습니다!'가 나오고 약속들에도 미도착이 도착으로 바뀌게된다.



# 약속을 못 지켰을 경우...

- **벌금부과**

<img width="312" alt="Screen Shot 2019-09-16 at 2 39 00 PM" src="https://user-images.githubusercontent.com/37801041/64936216-c182ab80-d88f-11e9-95cb-97e29f945343.png">

> 약속시간이 지나도 도착을 하지않으면 벌금이 계속 증가하며 알림으로 벌금이 얼마인지 알려주게 된다.
>
> 원래는 포인트나 실제로 돈을 중계로 받아서 나눠가지는 방식을 하고 싶었지만 아직은 한계가 있었다...

- 엽사 공개

<img width="1128" alt="Screen Shot 2019-09-16 at 2 38 49 PM" src="https://user-images.githubusercontent.com/37801041/64936307-28a06000-d890-11e9-9145-66f1e8564865.png">

> 이 화면은 '수배자'메뉴이다.  벌칙이 엽사공개인 약속은 약속을 지키지 못했을 경우 올려놓은 사진이 공개되며 시간이 늦어도 도착을 하게되면 삭제를 시키는 방식으로 만들었다.



# 아쉬웠던 점

- 결제시스템을 만들어서 벌금을 실제로 걷고 우리는 중계를 해서 약속이 끝나면 나눠주는 방식을 채용하고 싶었지만 현실적으로 아직은 불가능한것 같아 구현하지 못하였다.
- app도 세분화해서 나누지 않고 하나에 때려박는 식으로 프로젝트를 구현한것같다. 따라서 코드 가독성이 떨어지는 것 같고 복잡했다...

