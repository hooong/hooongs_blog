# [Server] Apache 웹 서버 인증 (Basic, Digest)

Apache는 특정 디렉토리에 접근할 때 사용자의 ID와 패스워드를 요구하도록 설정할 수 있는 기능을 제공합니다. 이러한 인증 기법에는 여러 가지가 있지만 이번 글에서는 `Basic`과 `Digest`를 다뤄보려고 합니다.

### Basic 인증

HTTP Basic Authentication이라고도 불리며, 일반적으로 사용자의 ID와 패스워드를 정의한 파일을 이용해 사용자 인증을 처리하게 됩니다. Basic 인증을 사용하기 위해서는 `mod_auth_basic`이라는 모듈이 필요하며, 이는 httpd 패키지를 설치하면 일반적으로 사용할 수 있습니다. 

Basic 인증은 클라이언트(ex)브라우저)가 보내는 인증에 대한 정보는 Base64로 인코딩이 되어 평문으로 전달되기때문에 안전하다고는 할 수 없다고 합니다. 

> Base64란? 
>
> 바이너리 데이터를 ASCII 텍스트 형식의 문자로 전송하기 위해 사용되는 인코딩 방법입니다. 만약, 바이너리 데이터를 일반적인 ASCII로 인코딩을 하여 전송하게 된다면, 시스템별로 해석을 잘 못하는 경우가 발생할 수 있습니다. 따라서 Base64는 ASCII 중 제어문자와 일부 특수문자를 제외한 64개의 안전한 출력 문자만을 사용해 인코딩하여 바이너리 데이터를 주고받는 과정에서 데이터에 손실이 발생하지 않게 해줍니다.

### Basic 인증 설정

```shell
# Basic 인증을 설정하기 위한 파일 생성
$ vi /etc/httpd/conf.d/auth_basic.conf
<Directory /var/www/html/basic>
        AuthType Basic
        AuthName "Basic Authentication Test"
        AuthUserFile /etc/httpd/.htpasswd
        Require valid-user
        Order deny,allow
        Deny from all
        Allow from 127.0.0.1 192.168.56
</Directory>
```

> - `<Directory /var/www/html/basic></Directory>` : Basic 인증을 사용할 디렉토리 지정
> - `AuthType` : 인증의 종류를 Basic으로 설정
> - `AuthUserFile` : 인증 사용자의 패스워드가 저장될 파일 지정
> - `Require valid-user` : 상기 지정된 패스워드 파일에 저장된 모든 유저를 허용	
>   - `Require user lee hong`와 같이 특정 사용자만 허용할 수도 있음
> - `Order` : deny, allow 순서로 규칙을 적용할지 설정
> - `Deny, Allow` : 특정 호스트명 또는 주소를 가지고 접근을 허용하거나 거부

이외에도 사용자들을 그룹으로 묶어 그룹에 속하는 사용자들만 특정 디렉토리에 접근을 허용하는 방법도 있습니다.

```shell
# Basic 인증 설정 파일
$ vi /etc/httpd/conf.d/auth_basic.conf
<Directory /var/www/html/basic>
        AuthType Basic
        AuthName "Basic Authentication Test"
        AuthUserFile /etc/httpd/.htpasswd
        AuthGroupFile /etc/httpd/groups				# group에 대한 정보를 저장한 파일 경로 지정
        Require group hong
        Order deny,allow
        Deny from all
        Allow from 127.0.0.1 192.168.56
</Directory>

# httpd 그룹 설정
$ vi /etc/httpd/groups
hong: hong root
```

이제 Apache에서 Basic 인증을 사용하기 위한 준비는 마쳤습니다. 이제 할 일은 httpd상에서 사용자의 패스워드를 설정하는 일입니다. 앞서 `/etc/httpd/.htpasswd`라는 파일을 지정했는데 이 파일에 사용자의 패스워드 정보가 생성되어야 합니다. 패스워드를 설정하는 방법은 아래와 같습니다.

```shell
# hong 사용자에 대한 패스워드 설정
$ htpasswd -c /etc/httpd/.htpasswd hong
New password:
Re-type new password:
Adding password for user hong

# .htpasswd 파일 확인
$ cat /etc/httpd/.htpasswd
hong:$apr1$2IIoaCCX$.g9jVg4n2WNeO3RZCMdCE.

# httpd 재실행
$ systemctl restart httpd

# Basic 인증을 사용할 디렉토리에 index.html 생성
$ vi /var/www/html/basic/index.html
<html>
  <head>
  	<title>www.hong.com</title>
  </head>
  <body>
    <div style="width: 100%; font-size: 80px; font-weight: bold; text-align: center;">
    	Basic Auth Test in www.hong.com
    </div>
  </body>
</html>
```

패스워드 설정도 마쳤으니 브라우저를 통해 `(웹서버 IP주소)/basic`으로 접속을 해봅니다.

![스크린샷 2020-12-24 오후 9 26 00](https://user-images.githubusercontent.com/37801041/103088594-a116d480-462e-11eb-92e5-ee7be4a31805.png)

접속을 해보니 사용자 이름과 비밀번호를 물어보는 창이 뜨게되네요!! 그럼 이제 위에서 설정한 사용자 이름과 패스워드를 정확이 기입해봅시다.

![스크린샷 2020-12-24 오후 9 26 58](https://user-images.githubusercontent.com/37801041/103088639-c4418400-462e-11eb-9cf0-3f8897712ad4.png)

사용자 인증에 성공을 한다면 `/var/www/html/basic`에 생성한 인덱스 페이지가 뜨는 것을 확인해볼 수 있습니다. 이렇게 Basic 인증에 대하여 알아보았습니다. 하지만 앞서 말했듯이 Basic 인증의 경우, Base64를 기반으로 인코딩을 하기때문에 보안 측면에서 안전하다고 볼 수 없습니다. 이보다 안전한 방법으로는 Digest 인증이 있습니다. 그럼 이제 Digest에 대하여 알아봅시다.

### Digest 인증

HTTP Digest Authentication이라고 하며, mod_auth_digest 모듈이 필요한 기능입니다. 이 모듈 또한 httpd 패키지를 설치하면 일반적으로 사용이 가능합니다. Digest 인증은 Basic 인증과 동일하게 사용자의 ID와 패스워드를 정의한 파일을 이용해 인증을 처리합니다. 그러나 Basic과는 다르게 사용자의 인증 정보를 MD5와 같은 해시 함수가 적용되어 암호화 된 후에 서버로 보내지기 때문에 Basic 인증보다는 안전하다고 합니다. (필자의 생각:MD5의 경우, Rainbow table이 있어 마냥 안전하다고는 볼 수 없을 것 같습니다. 검색 결과:MD5로 패스워드를 암호화하지 않음. Digest의 사상이 "비밀번호를 네트워크를 통해 절대 교환하지 않는다"라고 함.) 반면, Digest 인증의 경우 지원하지 않는 브라우저가 있다는 것이 단점입니다.

### Digest 설정

```shell
# Digest 설정 파일 생성
$ vi /etc/httpd/conf.d/auth_digest.conf
<Directory /var/www/html/digest>
        AuthType Digest									# Digest 인증 방식 설정
        AuthName "Private Area"					# Realm으로 사용되며, Realm은 사용자를 담는 장바구니 정도로 생각할 수 있음
        AuthDigestDomain http://www.hong.com/digest/		# Digest 인증이 적용되는 기본 URI
        AuthUserFile /etc/httpd/.htdigest				# 사용자 정보를 담는 파일 지정
        Require valid-user
        Order deny,allow
        Deny from all
        Allow from 127.0.0.1 192.168.56
</Directory>

# Digest 사용자 추가
$ htdigest -c /etc/httpd/.htdigest 'Private Area' hong		# Realm 지정
Adding password for hong in realm Private Area.
New password:
Re-type new password:

# 사용자 파일 확인
$ cat /etc/httpd/.htdigest
hong:Private Area:092e1bb3c112dc52d1adda1fe3c4dd6f

# httpd 재실행
$ systemctl restart httpd

# index.html 생성
$ mkdir /var/www/html/digest
$ vi /var/www/html/digest/index.html
<html>
  <head>
        <title>www.hong.com</title>
  </head>
  <body>
    <div style="width: 100%; font-size: 80px; font-weight: bold; text-align: center;">
        Digest Auth Test in www.hong.com
    </div>
  </body>
</html>
```

Digest 인증을 사용하기 위한 작업을 모두 마쳤습니다. 이제 Basic과 동일하게 브라우저를 통해 `(웹서버IP주소)/digest`로 접속을 해봅시다.

![스크린샷 2020-12-24 오후 9 43 42](https://user-images.githubusercontent.com/37801041/103089359-18e5fe80-4631-11eb-838a-58a317f3caf0.png)

![스크린샷 2020-12-24 오후 9 43 50](https://user-images.githubusercontent.com/37801041/103089365-1daab280-4631-11eb-9d71-f9336b521718.png)

사용자 인증 정보를 입력하고 유효한 사용자라면 해당 파일에 접근이 가능한 것을 확인해볼 수 있습니다.

<br>

## 정리하며...

이번 글에서는 Apache가 제공하는 mod_auth_basic, mod_auth_digest를 이용해 특정 디렉토리 접근 시 사용자 인증을 하는 두 가지 방법에 대하여 알아보았습니다. 이외에도 많은 인증 방식이 있으니 앞으로 차차 학습을 해나가면 좋을 것 같습니다. 글을 읽어주신 분들께 감사를 드리며 이번 글을 여기서 마쳐보겠습니다. 감사합니당^^

