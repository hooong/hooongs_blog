# 정규표현식

1. 정규표현식(regular expression) 이란?

   >특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어
   >
   >정규표현식은 특정 문자의 형식을 치환하거나 찾아내는데 사용할 수 있다.
   >
   >ex)  r'^\d{3}-\d{3,4}-\d{4}'   =>  핸드폰 번호 정규식

2. 메타 문자

   > 원래의 문자 뜻이 아닌 특별하 용도로 사용하는 문자로
   >
   >   `. ^ $ * + ? {} [] \ | ()`  이러한 것들이 있다.

   ```
    ' . ' :  개행문자 '\n'을 제외한 모든 문자와 매치된다.
   
     	ex) a.b => a + 모든문자(개행문자 제외) + b 
   
     						'aab', 'a.b', 'abb'...
     
   
   ​ ' ^ ' : 문자열의 시작을 나타낸다.
   
     	ex) ^a. => a로 시작하고 두 글자
   
     						'ab', 'aa' ...
     
   
   ​ ' $ ' : 문자열의 끝을 나타낸다.
   
     	ex) ing$  =>  'ing', 'sing', 'riding'...
     
   
   ​ ' * ' : 바로 앞에 있는 문자가 0부터 무한대까지 반복될 수 있다는 의미
   
     	ex) a*b => 'aaaaab', 'aab', 'ab' ...
     
   
   ​ ' + ' : *과 다르게 1부터 반복되는 의미
   
   
   ​ ' ? ' : 바로 앞의 문자가 있어도 되고 없어도 된다는 의미
   
    		ex) ab?c  =>  'ac', 'abc' 이 두개가 매치된다.
     
   
   ​ ' { } ' : 이것도 반복이지만 횟수를 지정할 수 있다.
   
     - {m} : m번 반복되어야한다.
   
       ex) a{3}b => 'aaab'
   
     - {m,n} : m~n번 반복되어야한다.
   
       ex) a{3,5}b => 'aaab', 'aaaab', 'aaaaab'
       
   
   ​ ' [ ] ' : 문자클래스로 []사이에는 어떤 문자도 들어갈 수 있다.
   
     	ex) [a-zA-Z] : 알파벳 대소문자, [0-9] : 숫자
   
     - 문자클래스는 자주 사용하는 클래스는 별도의 표기법으로 지정이 되어있다.
       * \d  -  숫자, [0-9]와 동일
       * \D  -  숫자가 아닌 것, `[^0-9]`와 동일
       * \s  -  공백, [ \t\n\r\f\v]와 동일 맨앞에 공백(space)이 들어가 있다
       * \S  -  공백이 아닌 것, `[^ \t\n\r\f\v]`와 동일
       * \w  -  문자+숫자, [a-zA-Z0-9]와 동일
       * \W  -  문자+숫자가 아닌 것, `[^a-zA-Z0-9]`와 동일
   
   ​ ' ( ) ' : 괄호안의 문자를 하나로 묶어서 다룰수있다.
   
   ​ ' | ' : or와 같은 의미이다.
   
   ​ ' \ ' : 메타문자의 성질을 없애서 문자로 사용하고 싶을때 붙인다.
   
   
   ```

3. 정규표현식 예제

   ```python
   # 이메일
   ^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$
   
   # 비밀번호 (특수문자 / 문자 / 숫자 포함 형태의 8~15자리 이내)
   ^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$
   
   # 비밀번호 ( 숫자, 문자를 포함하는 6~12자리 이내)
   ^[A-Za-z0-9]{6,12}$
   ```



### Python의 정규표현식 지원 모듈 're' 

----

> re 모듈을 사용하면 python에서 문자열에서 정규식 패턴에 해당하는 문자열을 손쉽게 다룰 수 있다.

- `compile()` : 특정 정규표현식을 패턴화 시킨다 ( *패턴* 이란 정규식을 컴파일한 결과 )

  ```python
  >>> import re
  >>> patt = re.compile('[0-9]*a')
  >>> patt
  re.compile('[0-9]*a')
  ```

- `match()` : 문자열의 처음부터 정규식과 매치되는지를 확인해준다.

  ```python
  >>> p = re.compile('[0-9]*a')
  >>> m = p.match('123a')
  >>> m		
  <re.Match object; span=(0, 4), match='123a'>	# 정규식과 일치하면 match객체가 반환된다.
  >>> m = p.match('123')
  >>> print(m)
  None																					# 일치하지 않다면 아무것도 반환되지 않는다.
  ```

- `search()` : match와 비슷하지만 문자열을 처음부터 검색하지않고 문자열 전체를 검색한다.

  ```python
  >>> p = re.compile('[a-z]+')
  >>> m = p.match('123 hooong')
  >>> print(m)
  None																				# 처음부터 검색하는 match는 객체가 반환되지 않는다.
  >>> m = p.search('123 hooong')
  >>> print(m)																# 전체를 검색하는 search는 객체가 반환된다.
  <re.Match object; span=(4, 10), match='hooong'>
  ```

- `findall()` : 문자열에 정규식과 일치하는 부분을 모두 찾아 list형태로 반환해준다.

  ```python
  >>> result = p.findall('hello python world!')
  >>> print(result)
  ['hello', 'python', 'world']
  ```



> re모듈에는 컴파일 옵션도 있고 또다른 method들도 있습니다. 추후에 업데이트를 더 할 예정입니다.
>
> 감사합니당~^^

