# [Linux] CentOS7 Hostname 변경

## 현재 hostname 확인

```shell
[root@localhost /]# hostname hostname
localhost.localdomain
```

초기 hostname은 `localhost`인 것을 확인할 수 있다.

<br>

## hostname 변경

```shell
# 일시적 변경 ( 재부팅 시 원상복구 )
[root@localhost /]# hostname server

[root@localhost /]# hostname
server

[root@localhost /]# reboot

[root@localhost ~]# hostname
localhost.localdomain
-----------------------------
# 영구적 변경
[root@localhost ~]# hostnamectl set-hostname server

[root@localhost ~]# hostname
server

[root@localhost /]# reboot

[root@server ~]#
```

hostname을 영구적으로 변경할 경우 시스템을 재시작하고나서부터는 `root@localhost`가 아닌 `root@server`로 바뀌어 표시되는 것도 확인할 수 있다.

