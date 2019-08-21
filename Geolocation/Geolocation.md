# Geolocation

<pre>
  프로젝트를 진행중 현재위치를 불러와야하는 기능이 필요해서 찾아 본 결과 Html5에서 geolocation이라는 api가 있었고 이 api를   
  사용하여 GPS, Wi-Fi, 휴대전화의 기지국, IP 등을 통해서 위치 정보를 알아낼 수 있었습니다.
        navigator.geolocation.getCurrentPosition() 
          - 사용자의 현재위치를 요청할 수 있고
        navigator.geolocation.watchPosition()
          - 사용자의 위치를 지속적으로 확인해서 위치가 변경될 때마다 지정된 콜백함수를 호출해줄 수 있고
        navigator.geolocation.clearWatch()
          - 위치 정보를 수집하는 작업을 중단할 수 있습니다.
</pre>

- 우선 아주 간단한 Geolocation 사용법을 살펴보겠습니다.

  ```html
  <button onclick="getLocation()">Try It</button>
  
  <p id="pos"></p>
  
  <script>
  var x = document.getElementById("pos");
  
  function getLocation() {
      navigator.geolocation.getCurrentPosition(showPosition);
  }
  
  function showPosition(position) {
    x.innerHTML = "Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude;
  }
  </script>
  ```

<img width="242" alt="Screen Shot 2019-08-21 at 7 04 54 PM" src="https://user-images.githubusercontent.com/37801041/63423184-b67e5c00-c446-11e9-8370-fdcc135e8e8d.png">

- 버튼을 누르게 되면 자신의 현재위치의 위도와 경도를 불러오는 것을 확인 할 수 있습니다.



- 아래는 프로젝트에서 제가 직접 사용한 코드입니다. ( init 함수를 실행해주는 코드가 필요합니다. )

<img width="807" alt="Screen Shot 2019-08-21 at 7 10 58 PM" src="https://user-images.githubusercontent.com/37801041/63428745-40342680-c453-11e9-97ed-d60dfba2ce77.png">

- 카카오 맵api에 현재위치의 위도와 경도를 받아와서 지도가 현재위치가 중심으로 표현되게 구현을 해보았습니다.

<img width="318" alt="Screen Shot 2019-08-21 at 8 40 25 PM" src="https://user-images.githubusercontent.com/37801041/63429042-f8fa6580-c453-11e9-8d8c-72bde31bed5f.png">

- 그럼 위처럼 위치정보를 허용할 것인지 경고창이 뜹니다. 허락을 눌러주면 현재위치를 불러오게됩니다.

- 사용해본 결과 위치를 찾아오는 시간이 조금 오래걸리는 경우도 있었습니다. 이것은 위치 정확도를 설정해서 타협을 볼 수 있다고 알고 있으며 필요하신 분은 구글에 검색을 해보시면 될 것 같습니다ㅎㅎ;;

  

  ### 그리고 아주 중요한 점이 하나 있습니다.

  <pre>
    최근에 개인정보에 대한 보안이 강화되어 대부분의 브라우저에서 일반 http 사이트에서는 위치정보를 수집할 수 없게되었다고 합니다. 그래서 geolocation도 http에서 위치를 수집 못 합니다. 저도 이 정보를 몰라서 프로젝트를 배포해보고 지도가 계속 안뜨는 에러로 고생을 많이 했던 기억이 납니다... 다행히 로컬에서는 문제 없이 잘 됩니다!! 
  혹시 배포를 하시고 geolocation을 사용하시려면 https로 적용을 시켜주시면 되겠습니다.
  </pre>

  

