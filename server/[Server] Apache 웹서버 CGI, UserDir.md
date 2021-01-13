# [Server] Apache 웹서버 CGI, UserDir

이번 글에서는 Apache 웹서버가 제공하는 CGI와 UserDir에 대해서 살펴보고자 합니다.

### CGI란?

CGI는 Common Gateway Interface의 약자로 서버 사이드 스크립트와 웹 서버가 서로 통신하는 방법을 정의한 것입니다. 만약 사용자가 정적인 콘텐츠(HTML같은 콘텐츠)가 아닌 동적인 콘텐츠를 요청한다면, 웹 서버는 이러한 요청을 처리하기 위해서 서버 사이드 스크립트(Python, node.JS, Perl, php 등)를 사용해 처리해야한다. 문제는 웹 서버가 바로 서버 사이드 스크립트를 사용할 수 없다는 것이다. 즉, 웹 서버와 서버 사이드 스크립트를 이어주는 다리가 필요한 셈이다. 여기서 '다리'가 바로 CGI인 것이다. 

예를들어, 웹 페이지에서 사용자가 로그인을 하려고 한다고 해보자. 사용자는 ID와 PW를 입력하고 로그인 버튼을 누를 것이다. 그럼 웹 서버는 사용자의 ID와 PW를 어떻게 확인할 것인가? 바로 서버 사이드 스크립트를 사용해 DB와 통신하여 회원정보와 비교를 해봐야할 것이다. 여기서 웹 서버와 서버 사이드 스크립트간에 통신이 필요하고 여기에 통신하는 방법을 정의한 것이 CGI인 것이다.

<br>

### Python을 사용해 CGI 사용해보기

우선 Python을 사용하기 위해 Python을 설치해야합니다.

```shell
$ yum install python3
```

또한, CGI를 사용하기 위해서는 Apache 서버 설정을 살짝 변경해주어야합니다.

```shell
$ vi /etc/httpd/conf/httpd.conf
247 ScriptAlias /cgi-bin/ "/var/www/cgi-bin"	# cgi를 사용할 파일의 경로를 지정
255 <Directory "/var/www/cgi-bin">
256     AllowOverride None
257     Options +ExecCGI							# Options에 `+ExecCGI`를 추가해줌으로써 CGI 실행을 허용
258     Require all granted
259 </Directory>
294 AddHandler cgi-script .cgi .py		# `.py`를 추가해 python파일을 인식하도록 설정

$ systemctl restart httpd 					# 설정을 마쳤으니 apache 재실행
```

CGI를 사용하기 위한 설정은 우선 완료했다. 그럼 이제 웹 서버에서 python 스크립트 파일을 실행하고 그 결과값을 브라우저에 띄워보겠다. 그러기 위해서 python 스크립트 파일을 아래와 같이 작성해줍니다.

```shell
$ vi /var/www/cgi-bin/first.py			# 설정에서 지정해준 `/var/www/cgi-bin` 폴더에 생성

#!/usr/bin/env python3
a = 1
b = 2
print('Content-type: text/html')
print()
print('<html>')
print('<body>')
print('<div style=\"width: 100%; font-size: 80px; font-weight: bold; text-align: center;\">')
print('Python3 Test Page <br>')
print('a + b = ', a + b)
print('</div>')
print('</body>')
print('</html>')
```

간단히 스크립트에 대해 설명하면 html 메시지를 만들어주는 코드이다. 따라서 `Content-type: text/html`이라는 헤더를 두고 한줄의 빈 여백을 두고 body를 만들어줍니다. 여기서 python3가 동적으로 돌아간다는 것을 보여주기 위해서 a, b라는 변수에 1, 2를 초기화해주고 메시지안에 `a+b`와 같이 계산식도 넣어보았습니다.

이렇게 스크립트 파일 작성도 마쳤다면, 브라우저에서 `(웹 서버 IP주소)/cgi-bin/first.py`를 접속해보면 아래와 같이 나오면 성공입니다.

![스크린샷 2020-12-23 오후 7 09 26](https://user-images.githubusercontent.com/37801041/102985457-8bcc7800-4552-11eb-9b95-d180dc181d2a.png)

<br>

### UserDir 사용

UserDir은 리눅스 시스템에 존재하는 사용자별로 웹사이트를 제공하는 기능으로 `(IP주소)/~{username}`으로 접속시 각 사용자별 디렉토리에서 리소스를 제공할 수 있다.

그럼 UserDir의 설정에 대해 간략히 알아봅시다.

```shell
$ vi /etc/httpd/conf.d/userdir.conf
11 <IfModule mod_userdir.c>
				...
24     UserDir public_html			# 모든 사용자에게 UserDir을 허용하는 경우 다음과 같이 설정
25 </IfModule>
31 <Directory "/home/*/public_html">		# 위에서 설정한 모든 user에 대하여 `public_html`폴더를 지정
32     AllowOverride FileInfo AuthConfig Limit Indexes
33     Options MultiViews Indexes SymLinksIfOwnerMatch IncludesNoExec
36     Require method GET POST OPTIONS
37 </Directory>

$ systemctl restart httpd				# 설정을 마치면 항상 재실행
```

참고로 위에서는 `public_html`이라는 것으로 모든 사용자에게 Userdir을 허용하였지만 아래와 같이 설정하는 방법도 존재합니다.

```shell
# 소수 사용자에게 UserDir을 허용
UserDir disabled
UserDir enabled kim lee park

# 대부분의 사용자에게 허용하고 일부만 거부하는 경우
UserDir enabled
UserDir disabled root lee
```

이제 설정을 마쳤으니 User를 생성하고 UserDir을 사용해봅시다.

```shell
# 'hong'이라는 유저 생성
$ useradd hong			

# 'hong'으로 유저 전환
$ su hong

# public_html 폴더 생성
$ mkdir /home/hong/public_html

# 해당 유저에서 제공할 index.html 작성
$ cd /home/hong/pulic_html
$ vi index.html
<html>
  <body>
    hong's Web Site!
  </body>
</html>

# 웹에서 해당 폴더를 접근할 수 있도록 권한을 조정
$ chmod 755 -R /home/hong

# 아파치가 home dirs에 접근할 수 있게끔 설정
$ setsebool -P httpd_enable_homedirs true
```

이제 `(웹서버 IP주소)/~hong`로 접속을 해보면 아래와 같이 나온다면 성공입니다.

![스크린샷 2020-12-23 오후 7 43 44](https://user-images.githubusercontent.com/37801041/102988383-2d55c880-4557-11eb-93a9-ada0b387309d.png)

<br>

### 정리하며...

이번 글에서는 CGI에 대해서 그리고 Apache에서 어떻게 CGI를 사용하는지를 알아보았고 이를 직접 Python을 사용해 실습을 해보았습니다. 그리고나서 UserDir마다 웹사이트를 제공할 수 있게해주는 기능에 대해 알아보고 사용하는 방법에 대하여 알아보았습니다.

감사합니다!

