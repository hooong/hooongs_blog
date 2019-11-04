# [JQuery] modal 만들기

> 브라우저의 옵션을 이용해 사용하지 않을 수 있는 팝업창과는 다르게 모달창은 기능상 반드시 노출을 시켜야하는 경우에 사용할 수 있다는 점에서 장점이 있다.



#### jQuery를 사용하면 쉽게 modal을 만들어낼 수 있다.

----

#### 사용법

```html
<!-- include jQuery :) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.min.js"></script>

<!-- jQuery Modal -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-modal/0.9.1/jquery.modal.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery-modal/0.9.1/jquery.modal.min.css" />
```

> 위의 코드를 `<head></head>`사이에 넣어주면 jQuery와 jQuery의 modal을 사용할 준비가 끝난다.



- #### 같은 html상에 있는 코드를 modal에 띄우기

````html
<!-- modal에 띄우고자하는 코드 -->
<div id="test" class="modal">
  <p>떴다~ 떴다~ 모달창!</p>
  <a href="#" rel="modal:close"><button>닫기</button></a>    <!-- 닫기버튼 -->
</div>

<!-- href 속성값을 사용하여 modal을 띄워주는 링크 -->
<p><a href="#test" rel="modal:open"><button>모달창 띄우기</button></a></p>
````

<img width="496" alt="Screen Shot 2019-11-04 at 10 56 12 AM" src="https://user-images.githubusercontent.com/37801041/68096073-c9ef7e00-fef1-11e9-8412-7725eb010c8d.png">



- #### 외부의 html파일을 modal에 띄우기

```html
<!-- modal버튼이 있는 html -->
<a href="ex.html" rel="modal:open">
  <button>다른 html을 모달로!</button>
</a>
```

```html
<!-- ex.html -->
<p>이건 ex.html입니다~</p>
<a href="#" rel="modal:close"><button>닫기</button></a>
```

<img width="497" alt="Screen Shot 2019-11-04 at 11 01 26 AM" src="https://user-images.githubusercontent.com/37801041/68096198-7893be80-fef2-11e9-8809-99e2dc017589.png">



----

##### 참고자료

- [https://jquerymodal.com/?](https://jquerymodal.com/?)