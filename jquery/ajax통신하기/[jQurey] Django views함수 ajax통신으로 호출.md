# [jQurey] Django views함수 ajax통신으로 호출

> Django에서 웹 개발을 하다보면 한 html화면에서 다른 app이나 다른 views의 함수를 비동기적으로 처리해야 할때가 있다. 지금 해보고자 하는 것이 바로 ajax를 활용하여 요청을 보내고 json형식으로 반환을 받아보는 것이다.



#### 동작순서

- html에서 입력을 준다.
- jquery가 입력값을 서버로 보낼 작업을 준비
- ajax를 통하여 서버로 요청
- views의 함수 실행 후 json형식으로 반환
- json형식으로 응답을 받아 html에서 보여준다.



#### html 코드

```html
<head>
	<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>

	<!-- test라는 함수를 쓰기위한 준비상태 -->
	<script type="text/javascript">
	$(document).ready(function() {
		test();
	});
	</script>
</head>

<body>
  <!-- 반환받은 결과를 띄우기위한 div -->
  <div id="test_view">
    <input type="hidden" id='test_value' value='1'>
  </div>
</body>

<script>
	// test() - ajax통신을 하는 함수
	function test(){
		var x = $("#test_value").val();		// x에 위에 '1'로 입력되는 값 저장
    // ajax 통신
    $.ajax({
      type: 'POST',
      url: '/ajax_test/',
      data: {number:x},					// x를 number라는 이름으로 views로 넘겨준다.
      dataType: 'json',
      // 통신 성공
      success: function(result){
        $('#test_view').html('<p>' + result[x] + '</p>');
      },
      // 통신 error
      error: function(e) { console.log('error:'+e.status);}
    });
	}
</script>
```



#### views.py 코드

```python
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# url이 '/ajax_test'로 되어있다고 가정
@csrf_exempt
def ajax_test(request):
    if 'number' in request.POST:
        num = request.POST['number']
    
    if num=='1':
      answer = {str(num):"1입니다."}				# json형식으로 넘겨줄 데이터를 만들어준다.
    else:
    	answer = {str(num):"1이 아닙니다."}

    return JsonResponse(answer)
```

- ajax통신시 POST로 요청을 하려면 csrf_token이 필요한데 위와 같이 사용하려는 views함수에 `@csrf_exempt` 를 붙여주면 된다.

####  

#### 결과

- `value='1'` 일때

  <img width="74" alt="Screen Shot 2019-11-11 at 6 25 27 PM" src="https://user-images.githubusercontent.com/37801041/68576705-e707ec00-04b1-11ea-9248-06d498ea5c4a.png">

- `value='2'` 일때

  <img width="106" alt="Screen Shot 2019-11-11 at 6 25 51 PM" src="https://user-images.githubusercontent.com/37801041/68576707-e8391900-04b1-11ea-9480-19490fac58b2.png">





____

이번 글에서는 jQuery의 ajax를 사용하는 방법에 대해 알아보았습니다. 읽어주셔서 감사합니다.