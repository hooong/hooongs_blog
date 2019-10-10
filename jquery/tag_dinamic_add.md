# [JQuery] 동적으로 버튼을 누르면 html에 태그 추가 및 삭제

>저의 경우 기존의 input tag들이 있는데 상황에 따라 input tag가 더 필요한 경우 추가를 해야하는 경우를 만들어야 했다. 그래서 검색을 통해 JQuery를 이용하여 html에 tag를 동적으로 추가할 수 있는 방법을 찾았다.

```html
<script src="http://code.jquery.com/jquery-latest.min.js"></script>

<form action="" method='POST'>
    <div class='addInput'>

    </div>

    <button type='button' class="btnAdd">tag추가하기</button>
    <input type="submit">
</form>

<script type="text/javascript">
    $(document).ready (function () {                
        $('.btnAdd').click (function () {                                        
            $('.addInput').append (                        
                '<input type="type" name="test" value="">\
                <button type="button" class="btnRemove">tag삭제하기</button><br>'                    
            );    // input taf 추가                     
            $('.btnRemove').on('click', function () { 
              															// 여기서 this는 '.btnRemove'
                $(this).prev().remove();		// .prev()로 input tag를 가리키고 remove()한다.
                $(this).next().remove();		// <br> 삭제
                $(this).remove();						// 버튼삭제
            });
        });                                      
    });
</script>
```

위의 코드를 활용하면 원하는대로 원하는 div에 html상에 tag를 동적으로 만들 수 있다.

- ex)



<img width="150" alt="Screen Shot 2019-10-10 at 10 40 17 AM" src="https://user-images.githubusercontent.com/37801041/66532510-974ca280-eb4a-11e9-9f0c-43c378d87d22.png">



----



<img width="218" alt="Screen Shot 2019-10-10 at 10 40 30 AM" src="https://user-images.githubusercontent.com/37801041/66532508-974ca280-eb4a-11e9-8104-1d21fd6f08b9.png">

