# [JQuery] 여러 input값을 배열로 view로 넘기기

```html
{% for test in tests %}
	<input type="text" name='test1' value="{{test}}"><br>
{% endfor %}
```

위와 같은 상황에서는 test1이라는 input이 몇개가 될지 모른다. 그런데 이것들을 django의 view로 넘겨서 배열로 처리를 하고싶어 알아보니 jquery를 사용해 배열로 만들고 그 배열을 hidden으로 넘겨주는 방법을 생각해냈다.

따라서 아래와 같은 코드로 해결을 했다.

```html
<form action="{% url 'blabla' %}" method='POST'>
    {% csrf_token %}
    {% for test in tests %}
        <input type="text" name='test1' value="{{test}}"><br>
    {% endfor %}
    <input type="hidden" name='test[]' id='test_list' value=''>
    <input type="submit" onclick='getlist()'>
</form>

<script src="http://code.jquery.com/jquery-latest.min.js"></script>
<script type="text/javascript">
    function getlist() {
        var list = new Array();
        $("input[name=test1]").each(function(index, item){
          	list.push($(item).val());						<!-- input의 value들을 배열 list에 넣는다. -->
        });
        $("#test_list").val(list);							<!-- hidden type에 value값으로 넣어준다. -->
    }
</script>
```

위의 코드를 간략히 설명하면 onclick 옵션을 사용하여 form에서 submit이 눌렸을때 list라는 배열을 만들어 name이 'test1'인 input타입들의 value들을 list에 넣어주고 hidden타입의 input태그의 value값에 list를 넣어주는 코드이다.

그후 views에서는 아래와 같이 받아주면 된다.

```python
def blabla(request):
    if request.method == 'POST':
        test = request.POST['test[]']		# hidden타입인 input tag의 name를 통해 가져온다.
        print(type(test))                     # test의 타입은 str이 나온다.
```

