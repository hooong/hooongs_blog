# [Server] Apache 웹 서버

### 웹 서버란?

웹 서비스는 서비스를 제공하는 서버 부분과 이를 이용하는 클라이언트로 구성이 된다. 사용자들이 이용하는 웹 브라우저가 대표적인 클라이언트 중 하나이다. 이에 반해 클라이언트에게 서비스를 제공하는 서버 프로그램을 웹 서버라고한다. 다시말해 클라이언트가 서버에게 특정 리소스를 요청하면 웹 서버는 요청에 따른 리소스를 반환해주게 된다. 대표적인 웹 서버 프로그램으로는 Apache, Nginx, IIS등이 있다.

<img width="555" alt="스크린샷 2020-12-21 오후 9 23 48" src="https://user-images.githubusercontent.com/37801041/102776855-d1facd80-43d2-11eb-8f19-43c2de8c8d9d.png">

<br>

### Apache란?

웹 서버 프로그램 중 하나로 아파치 소프트웨어 재단에서 제공하는 대표적인 오픈소스 HTTP 서버이다. Apache는 자체적으로 다양한 기능을 제공하지만, 다양한 종류의 서드파티 모듈 설치를 통해 여러 기능들을 사용자 환경에 맞게 언제든지 추가와 삭제가 가능하고, 그 업데이트 또한 매우 활발하게 이루어지고 있는 웹 서버 중 하나이다. 최근 Nginx의 점유율도 무섭게 치고 올라오고는 있지만 2020년 현재까지는 Apache의 점유율이 더 높다.

![960px-Apache_HTTP_server_logo_(2016) svg](https://user-images.githubusercontent.com/37801041/102775705-b42c6900-43d0-11eb-85d9-3ce93920219c.png)

<br>

### Apache 설치와 기본 설정

> 실습 환경
>
> - CentOS7
> - Apache v2.4.6

#### Apache 설치

```shell
$ yum install httpd -y
```

해당 명령어를 통해 Apache 패키지를 설치할 수 있다.

#### Apache 기본 설정

```shell
# Apache 서버의 설정 파일들이 위치한 디렉토리
$ ls /etc/httpd/
conf  conf.d  conf.modules.d  logs  modules  run

# Apache 서버가 브라우저 상에서 인식할 데이터가 저장될 디렉토리
$ ls /var/www
cgi-bin  html

# Apache 서버의 로그 파일이 저장되는 디렉토리
$ ls /var/log/httpd
access_log  error_log
```

Apache의 주요 디렉토리들을 살펴보았다. 다음으로 Apache의 기본 설정 파일을 알아보자.

```shell
$ vi /etc/httpd/conf/httpd.conf
31 ServerRoot "/etc/httpd"			# Apache 서버가 사용할 설정 파일들이 저장될 디렉토리 지정
42 Listen 80										# 어떤 IP주소로 클라이언트의 접속을 받아들일지 지정 (IP주소를 지정할수도 있고, 포트번호만 지정 시 해당 포트의 모든 주소를 사용한다는 의미이다.)
95 ServerName www.hong.com:80		# 서버가 사용할 이름과 포트 설정
119 DocumentRoot "/var/www/html" # 서버가 인식할 데이터들이 저장된 디렉토리 지정
164 DirectoryIndex index.html index.php	# 클라이언트가 웹 서버 접속 시 초기화면으로 보여줄 파일명 지정.
182 ErrorLog "logs/error_log" 	 # 에러를 기록할 파일 지정. (losg는 /etc/httpd/logs를 의미)
217 CustomLog "logs/access_log" combined # 웹 서버로의 일반적인 접속 정보를 기록할 로그파일 지정
```

#### Apache 서비스 시작과 작동 확인

이제 Apache를 설치하였고 기본적인 동작을 위한 설정에 대해서도 알아보았으니 본격적으로 웹 서버를 작동시키고 잘 작동하는지 확인해보자.

```shell
# httpd 데몬 실행
$ systemctl start httpd

# httpd 데몬을 서비스로 등록하여 부팅 이후 자동으로 시작하게 설정
$ systemctl enable httpd

# httpd가 정상 작동하는지 확인 (Active 상태)
$ systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: active (running) since 월 2020-12-21 05:03:20 EST; 2h 39min ago
     Docs: man:httpd(8)
           man:apachectl(8)
  Process: 3381 ExecStop=/bin/kill -WINCH ${MAINPID} (code=exited, status=0/SUCCESS)
 Main PID: 3385 (httpd)
   Status: "Total requests: 11; Current requests/sec: 0; Current traffic:   0 B/sec"
   CGroup: /system.slice/httpd.service
           ├─3385 /usr/sbin/httpd -DFOREGROUND
           ├─3386 /usr/sbin/httpd -DFOREGROUND
           ├─3387 /usr/sbin/httpd -DFOREGROUND
           ├─3388 /usr/sbin/httpd -DFOREGROUND
           ├─3389 /usr/sbin/httpd -DFOREGROUND
           ├─3390 /usr/sbin/httpd -DFOREGROUND
           └─3393 /usr/sbin/httpd -DFOREGROUND
           
# 포트 80번에 대하여 httpd가 http 서비스를 제공하고 있는지 확인
$ lsof -i tcp:80
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
httpd   3385   root    4u  IPv6  32296      0t0  TCP *:http (LISTEN)
httpd   3386 apache    4u  IPv6  32296      0t0  TCP *:http (LISTEN)
httpd   3387 apache    4u  IPv6  32296      0t0  TCP *:http (LISTEN)
httpd   3388 apache    4u  IPv6  32296      0t0  TCP *:http (LISTEN)
httpd   3389 apache    4u  IPv6  32296      0t0  TCP *:http (LISTEN)
httpd   3390 apache    4u  IPv6  32296      0t0  TCP *:http (LISTEN)
httpd   3393 apache    4u  IPv6  32296      0t0  TCP *:http (LISTEN)

# Apache 버전 확인
$ httpd -v
Server version: Apache/2.4.6 (CentOS)
Server built:   Nov 16 2020 16:18:20
```

이제 Apache의 실행은 모두 마쳤다. 그럼 웹 브라우저에서 해당 서버가 제대로 요청에 대하여 반환을 해주는지 알아보기 위해 php를 설치하고 추가적인 설정을 해보자.

#### PHP 설치 및 설정

```shell
# php 설치
$ yum install php php-pear- -y

# php 설정 파일에서 timezone 변경
$ vi /tec/php.ini
878 date.timezone = Asia/Seoul

# index.php 생성
$ vi /var/www/html/index.php
<?php
phpinfo();
?>
```

#### 방화벽 설정

```shell
# iptables 설정 -> 80번, 443번 포트를 목적지로 하는 패킷을 허용
$ iptables -A INPUT -m state --state NEW,ESTABLISHED -p tcp --dport 80 -j ACCEPT
$ iptables -A INPUT -m state --state NEW,ESTABLISHED -p tcp --dport 443 -j ACCEPT

# firewalld 방화벽 설정
$ firewall-cmd --permanent --add-service=http
$ firewall-cmd --permanent --add-service=https

# firewalld 재실행
$ firewall-cmd --reload

# firewalld 서비스에서 http, https 확인
$ firewall-cmd --list-services
dhcpv6-client http https ssh
```

이제 Apache를 사용하기 위한 기본적인 설정을 모두 마쳤다. 이제 웹 브라우저를 통해 해당 서버의 IP주소로 접속을 해보면 다음과 같이 우리가 만든 `index.php`의 화면을 확인할 수 있다.

<img width="1358" alt="스크린샷 2020-12-21 오후 9 57 57" src="https://user-images.githubusercontent.com/37801041/102779453-96aecd80-43d7-11eb-8df5-1e2e34d22d36.png">

<br>

### 정리하기

이번 글에서는 웹 서버가 무엇인지 파악하고 웹 서버 프로그램 중 대표적인 Apache를 설치하고 기본 설정 파일을 조금 살펴보았으며, 직접 실행을 해보고 php를 설치하여 정상적으로 작동하는지까지 확인을 해보았다.



