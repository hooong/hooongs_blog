# [Django] 템플릿 언어 Documentation

> 템플릿 언어란, html상에서 context를 통해 넘겨받은 데이터들을 다루기 쉽게 해주는 하나의 언어라고 할 수 있으며, 형식은 python과 비슷 하지만 python도 아닌 html도 아닌 그러한 언어입니다.



#### 가장 많이 사용하게 되는 for, if

```html
<!-- for문 -->
{% for i in is %}
		(...)
{% endfor %}

<!-- if문 -->
{% if x == '1' %}
		(...)
{% endif %}
```



위와 같이 javascript를 사용하지 않고도 for문을 사용할 수 있게된다. 주의할 점은 python은 아니므로 python에서 지원하는 함수들은 사용할 수 없다. ( 필자는 이것을 깜빡하고 실수할때가 꽤 있었습니다.^^;; )



####  시간표기법을 활용하기

documentation을 들여다보다 발견한 것으로 model에 저장되어있는 datetimefield를 원하는 형식으로 html상에 표기를 하고싶을때 아주 유용하였습니다.

```html
{{ value|date:"Y년 m월 d일" }}

<!-- 출력결과 -->
2019년 11월 15일
```



#### 이러한 템플릿언어에 대한 Documentation 링크를 남겨드리겠습니다.

https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs



