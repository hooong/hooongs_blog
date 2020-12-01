# VS code 렉이 걸릴 때 해결법

> 어느 순간부터 vs code 내의 터미널과 에디터에서 입력 시 멈추는 것과 같은 렉이 발생을 하여 해결법을 찾아보았다.

<br>

## Renderer Type 변경

- `Code - Preferences - Setting` 또는 `cmd + ,` 으로 설정화면으로 이동한다.

<img width="614" alt="스크린샷 2020-12-01 오후 6 32 05" src="https://user-images.githubusercontent.com/37801041/100722109-95efd080-3403-11eb-9285-c4dd4c6b9bcf.png">

- `Renderer` 를 검색한다.
- 아마 `auto` 가 기본값으로 설정이 되어있을 것이다. 

<img width="365" alt="스크린샷 2020-12-01 오후 6 34 43" src="https://user-images.githubusercontent.com/37801041/100722368-e2d3a700-3403-11eb-8712-cf01c271f314.png">

- 이 값을 `dom`으로 변경하고 렉이 걸리는지 확인해본다.

<img width="397" alt="스크린샷 2020-12-01 오후 6 36 47" src="https://user-images.githubusercontent.com/37801041/100722653-2dedba00-3404-11eb-8e7e-c372f9d56692.png">

> canvas로 렌더링을 하는 과정에서 그래픽카드에 부하를 주는 경우가 발생한다고 한다.