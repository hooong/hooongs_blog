# [Django] 비로그인 시 접근을 막는 법



'마이페이지'와 같은 페이지를 만든다고 생각해보면 로그인이 되었을때만 로그인 되어있는 유저에 대한 정보를 보여주어야 한다. 그러나 html이나 views에서 따로 어떠한 방법으로든 로그인 여부를 확인해주지 않는다면 로그인을 하지 않아도 '마이페이지'에 접근이 가능할 것이다.



###  is_authenticated

> Is_authenticated는 django User model에 정의되어있는 attribute로 **AnonymousUser**가 들어올때에 False를 반환해줍니다.

이 속성을 사용하면 views, 또는 html의 template언어를 사용하여 현재 request를 통해 전달되어진 user정보가 로그인이 되어있는 유저인지 anonymous유저인지를 판단해줍니다.

코드를 보면 아래와 같습니다.

```html
{% if user.is_authenticated %}

	<!-- 로그인이 된 상태라면 실행할 코드 -->

{%else%}

	<!-- AnonymousUser가 들어온 상태 -->

{%endif%}
```

- 주의할 점

  이렇게 html상에서 user를 확일 할 경우, views에서 특정 user의 정보를 DB에서 filter를 해주고 render를 시켜주는 경우에는 views에서 따로 user를 확인해주지 않는다면 오류가 발생할 것이다. 따라서 이러한 경우에는 그냥 views에서 user를 확인하고 redirect를 하던가 render를 해주어야한다.



코드로 예를 보이자면,

```python
def mypage(request):
  user = User.objects.get(user=request.user)
  
  return render(request, "mypage.html", {'user':user})
```

```html
{% if user.is_authenticated %}
	{{user.id}}
{% else %}
	<!-- login 안됨. -->
{% endif %}
```

위와 같은 경우 Anonymous유저로 접근시 views에서 user라는 object를 찾지 못하기때문에 에러가 발생할 것이다.

따라서 이 문제는 아래 코드와 같이 해결할 수 있다.

```python
def mypage(request):
  # request로 넘어오는 user에 대한 정보를 cur_user에 담아준다.
  cur_user = request.user
  
  # anonymous user인지 확인
  if cur_user.is_authenticated:
  	user = User.objects.get(user=request.user)
  
  	return render(request, "mypage.html", {'user':user})
  else:
    return redirect('index')
```

로그인 유무 확인을 html이 아닌 views에서 해주므로 위에서 발생하던 문제는 발생하지 않게 된다.



### javascript를 사용하여 경고 창을 띄우고 redirect 시켜주기

html상에서 로그인이 안되었다면 로그인을 할 수 있는 로그인 페이지로 옮겨주고 싶을때 사용하면 된다.

코드는 아래와 같다.

```html
{% if user.is_authenticated %}
	<!-- 로그인이 되어있는 상태 -->
{%else%}
	<!-- javascript를 사용하여 처리 -->
  <script type=“text/javascript”>
      alert(‘먼저 로그인을 해주세요.’);
      window.location.href = ‘{%url “login” %}’; 	//'login' 페이지로 location해준다.
  </script>
{%endif%}
```





- 참고 : https://docs.djangoproject.com/en/2.2/ref/contrib/auth/