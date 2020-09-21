# [Server] Spring Boot + Gradle + JPA + EC2 + RDS 배포

> 배포 환경
>
> AWS EC2 Ubuntu 16.04.6
>
> AWS RDS MySql
>
> Spring Boot 2.2.9
>
> Java 11
>
> ( 해당 글은 EC2와 RDS를 사용해봤다는 전제하에 작성함. )

<br>

### 1. DB 설정

- JPA와 MySql을 사용하기 위한 의존성 추가

  ```
  # build.gradle
  
  implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
  compile 'mysql:mysql-connector-java'
  ```

- `application.yml` 설정

  ```yml
  spring:
      datasource:
          driver-class-name: com.mysql.cj.jdbc.Driver
          url: jdbc:mysql://localhost:3306/{DBNAME}?useSSL=false&characterEncoding=UTF-8&serverTimezone=UTC
          username: {database ID}
          password: {database Password}
      jpa:
          database: mysql
          generate-ddl: true
          show-sql: true
  ```

- RDS에서 MySql의 DataBase 생성

  - 필자는 MySql WorkBench를 통해 DB에 접근하고 DataBase를 생성하였음.

    > RDS를 설정할 때 주의할 점은 퍼블릭 액세스 가능성을 '예'로 해주어야한다.

  - `application.yml`에서 `url` 부분의 `{DBNAME}`에는 여기서 생성한 DataBase의 이름을 넣어주어야 함.

<br>

### 2. Spring Boot 프로젝트 git clone

- 로컬에서 개발한 Spring Boot 프로젝트를 `clone` 한다.

<br>

### 3. jdk 설치

```
# java11을 사용하는 경우
$ sudo add-apt-repository ppa:openjdk-r/ppa
$ sudo apt-get update
$ sudo apt-get install openjdk-11-jdk

# java8을 사용하는 경우
$ sudo apt-get update
$ sudo apt-get install openjdk-8-jdk
```

<br>

### 4. Gradle를 사용한 빌드

- 위에서 `clone` 받은 프로젝트 폴더로 이동

- `./gradlew` 파일 권한 변경

  `$ sudo chmod 777 ./gradlew`

- Spring Boot 프로젝트 빌드

  `$ sudo ./gradlew build`

  > 필자는 빌드 시 test 부분에서 문제가 발생하여 다음 명렁어로 test를 제외하고 빌드를 해봤었음.
  >
  > `$ sudo ./gradlew build --exclude-task test`

- 빌드가 정상적으로 완료되었다면 `{프로젝트 폴더}/build/libs` 경로에 `~.jar` 파일이 생성된다.

<br>

### 5. 백그라운드에서 `.jar` 파일 실행하기

- `{프로젝트 폴더}/build/libs` 경로로 이동

- `nohup` 을 사용해 `.jar` 파일 실행

  `$ nohup java -jar {~.jar 파일} &`

  > 해당 명령어를 실행 후 명령창에 뜨는 문구를 통해 log가 적히는  `nohup.out`파일의 경로를 알 수 있음.