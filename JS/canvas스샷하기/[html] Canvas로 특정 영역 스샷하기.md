# [html] Canvas로 특정 영역 스샷하기

> html파일이 render가 된 상태인 브라우저에서 보이는 화면을 캡쳐를 해야해는 경우가 있어 알아본 결과. 
>
> html2canvas를 사용하여 특정 div나 canvas (html에서 그림을 그릴 수 있게 해주는) 태그에 id를 달아놓고 div나 canvas를 스크린샷하여 이미지로 저장을 할 수 있는 방법이 있었습니다.



## 일단 바로 예제코드

```html
<!-- 스샷할 영역 -->
<div id='screenshot' style="padding: 10px; background: #00c3ff">
    <h1>Screen!</h1>
</div>

<!-- 스샷 버튼 -->
<button type="button" id="save">스샷!</button>

<!-- 스샷한 이미지를 띄우기위한 div -->
<div id="img"></div>


<!-- 필요한 js cdn --> 
<script src="https://code.jquery.com/jquery-2.2.1.min.js"></script>
<script src="http://html2canvas.hertzen.com/dist/html2canvas.js"></script>
<script>
    $(function(){
        $("#save").click(function() { 
            html2canvas($('#screenshot').get(0)).then( function (canvas) {
                document.getElementById('img').appendChild(canvas)
            });
        });
    });
</script>
```



## 실행결과

- 스샷 버튼을 누르기 전

<img width="759" alt="Screen Shot 2020-01-14 at 7 00 55 PM" src="https://user-images.githubusercontent.com/37801041/72334246-555e6a00-3700-11ea-8e6e-561ae01ae533.png">

- 스샷 버튼을 한번 눌렀을때

<img width="758" alt="Screen Shot 2020-01-14 at 7 01 06 PM" src="https://user-images.githubusercontent.com/37801041/72334254-57282d80-3700-11ea-8cf5-572cbeb5ff4a.png">

> 위에서 볼 수 있듯이 스샷! 버튼을 한번 누르면 아래 'img'라는 id가 달린 div에 위의 Screen!이 쓰여 있는 div를 스샷해서 이미지로 띄워주는 것을 확인할 수 있습니다.



## 마무리하며

일단은 이렇게 html상의 특정영역을 스크린샷을 하고 이것을 이미지로 html상에 띄워주는 방법에 대하여 알아보았습니다. 다음 글에서는 이 이미지를 django 서버상에서 png파일로 저장을 하는 방법에 대하여 알아보도록 하겠습니다.