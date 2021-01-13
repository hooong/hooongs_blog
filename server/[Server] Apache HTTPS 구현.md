# [Server] Apache HTTPS 구현

이번 글에서는 HTTPS가 무엇이고, Apache에서 HTTPS를 구현하기 위해서 동작 과정과 인증서를 생성하고 설정하는 방법에 대하여 살펴보고자 합니다.

## HTTPS란?

`HTTPS`란, HTTP over TLS, HTTP over SSL, HTTP Secure라고 불리며, 기존 HTTP가 평문으로 전달되는 통신 과정에서 안전하지 못한 문제점을 HTTP의 데이터를 SSL/TLS로 암호화하여 안전한 통신을 보장하기 위해 사용되는 프로토콜입니다. 또한, HTTP의 경우 80번 포트를 사용하는반면 HTTPS는 443번 포트를 사용하게 됩니다. 

<br>

## HTTPS의 동작 원리

HTTPS가 이뤄지는 과정, 즉 SSL Handshake는 크게 3단계로 설명할 수 있습니다.

- Hello 교환
- 인증서 교환
- 키 교환

이 과정을 그림으로 표현해보면 아래와 같이 동작하게 됩니다.

<img align="center" src="https://user-images.githubusercontent.com/37801041/104122101-65963d00-5386-11eb-93a0-7483afb681de.png" width=500>

각 단계를 좀더 자세히 살펴보겠습니다.

### 1. Hello 교환

> - 클라이언트가 서버에게 서버가 SSL을 사용해 클라이언트와 연결하기 위해 필요한 모든 정보(암호화 알고리즘의 종류 및 지원이 가능한 SSL 버전 정보)가 담긴 ClientHello 메시지를 보냅니다.
> - Hello 메시지를 받은 서버는 비슷한 정보(암호화 알고리즘 및 SSL 버전 정보)가 담긴 ServerHello 메시지를 클라이언트에게 보냅니다.

### 2. 인증서 교환

> - Hello 교환 과정을 통해 서버와 클라이언트의 연결이 이루어지면 서버는 자신의 신분을 증명할 SSL 인증서를 클라이언트에게 보냅니다.
> - 인증서를 받은 클라이언트는 인증서가 신뢰할 만한지를 CA(Certificate Authorities)를 통해 검증이 되었는지를 검사합니다.
> - (참고) : 매우 보안에 민감한 애플리케이션의 경우 서버측에서도 클라이언트의 신분 증명을 위해 인증서를 요구할 수도 있음.

### 3. 키 교환

> - 인증서를 확인한 클라이언트는 DES나 AES와 같은 대칭 키 알고리즘을 통해 임의의 비밀 키를 생성하고, 해당 키를 2단계에서 받은 인증서에서 서버가 보내온 알고리즘과 공개 키를 사용해 암호화한 후 서버에게 보냅니다.
> - 서버는 자신의 개인 키를 이용해 클라이언트가 생성한 임의의 비밀 키를 복호화한 후 데이터 전송 시 해당 비밀키를 이용하여 암호화해 클라이언트에게 전달합니다.

마지막 키 교환 단계를 통해 서버와 클라이언트는 서로 같은 임의의 비밀 키를 가지게 되고, 이후부터는 해당 비밀 키를 사용해 데이터를 암호화하여 주고받을 수 있게됩니다.

<br>

## Apache 서버에서 인증서 생성

위에서 살펴본 HTTPS를 구현하기 위해서는 인증서가 필요하다는 것을 알 수 있었습니다. 인증서를 생성하는 방법을 살펴보겠습니다. 

인증서를 생성하는 방법도 크게 3단계로 나뉘게됩니다.

1. 개인 키 생성

```shell
# 개인 키를 생성할 디렉토리로 이동
$ cd /etc/pki/tls/certs

# RSA 알고리즘을 사용해 2048비트의 개인 키 생성
$ openssl genrsa -out test_private.key 2048
```

<br>

2. CSR 생성

```shell
# 개인 키를 이용해 CSR 파일 생성
$ openssl req -new -key test_private.key -out test.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:KR
State or Province Name (full name) []:Seoul
Locality Name (eg, city) [Default City]:Seoul
Organization Name (eg, company) [Default Company Ltd]:Hong Com
Organizational Unit Name (eg, section) []:
Common Name (eg, your name or your server's hostname) []:www.hong.com
Email Address []:test@hong.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```

<br>

3. 개인 키와 CSR을 이용해 인증서 생성

```shell
# CSR 파일과 개인 키를 이용해 365일짜리 인증서 CRT를 생성
$ openssl x509 -in test.csr -out test.crt -req -signkey test_private.key -days 365
Signature ok
subject=/C=KR/ST=Seoul/L=Seoul/O=Hong Com/CN=www.hong.com/emailAddress=test@hong.com
Getting Private key
```

<br>

## SSL 설정

위의 단계에서 인증서를 만들었으니 이 인증서를 이용해 Apache에서 SSL을 설정하는 방법에 대하여 살펴보겠습니다. Apache에서 HTTPS를 구현하기 위해서는 `mod_ssl`을 설치해주어야합니다. 그리고 설정 파일을 수정하고 해당 모듈을 사용하게끔 httpd를 재시작해주면 HTTPS로 접속이 가능하게 됩니다.

```shell
# mod_ssl 설치
$ yum install mod_ssl -y

# ssl 설정 파일 수정
$ vi /etc/httpd/conf.d/ssl.conf

5 Listen 192.168.56.105:443 https
59 DocumentRoot "/var/www/html"
60 ServerName www.hong.com:443
100 SSLCertificateFile /etc/pki/tls/certs/http.crt
107 SSLCertificateKeyFile /etc/pki/tls/certs/http.key
 
# apache 재시작
$ systemctl restart httpd

# netstat 명령어를 이용해 443번 포트가 LISTEN 중인지 확인
$ netstat -natlp | grep httpd
tcp        0      0 192.168.56.105:443      0.0.0.0:*               LISTEN      2344/httpd
```

<br>

## 테스트

이제 브라우저를 이용해 `https://<서버 IP 주소>`로 들어가보면 아래와 같이 "연결이 비공개로 설정되어 있지 않습니다."라는 에러를 확인해볼 수 있습니다. 

<img align="center" src="https://user-images.githubusercontent.com/37801041/104123326-fa506900-538d-11eb-8085-661c34fb19e9.png" width=500>

이는 크롬 브라우저에서 해당 인증서를 유효하지 않다고 판단을 하고 있기때문입니다. 주소창에 있는 `주의 요함` 버튼을 눌러 인증서에 대한 정보를 살펴보면 아래와 같이 위에서 인증서를 생성할때 설정한 정보들을 확인해볼 수 있습니다.

<img align="center" src="https://user-images.githubusercontent.com/37801041/104123419-78147480-538e-11eb-9b02-c66e7b9df3ba.png" width=500>

이 과정을 통해 SSL handshake 과정에서 정상적으로 서버로부터 인증서를 전달받았다는 것을 알 수 있었습니다.

<br>

## 정리하며...

최근에는 HTTPS를 장려하기 위해 `Let's Encrypt`에서 무료로 아주 쉽게 HTTPS를 적용시킬 수 있습니다. 이러한 과정을 통해 SSL의 원리를 모르고 그냥 되니까 사용할 수도 있겠지만, 직접 인증서를 만들어보고 SSL handshake 과정을 살펴보고 서버로부터 정상적으로 받은 인증서를 눈으로 확인을 해보는 과정을 통해 더욱 깊은 이해를 할 수 있었던 것 같네요.^^ 글을 읽어주신 분들께 감사드립니다!