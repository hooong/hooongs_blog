# Servlet에 대하여

> 서블릿이라는 단어를 많이 접하게 되었지만 어렴풋이 어떤 일을 하는지만 알고 정확한 정의에 대하여 알지 못하였었다... 또한 Servlet과 Servlet Container등 용어들도 많아 헷갈리기도 일수였던 것 같다.. 자바로 백엔드를 공부하는 나로써 한번 제대로 정리를 해봐야겠다는 생각이 들었고 이번 기회에 Servlet에 대해 다시 한 번 정리해 보는 시간을 가지려한다.

<br>

### 서블릿에 대하여 알아보기 전에…

- CGI란?
	- CGI는 Common Gateway Interface의 약자로 웹서버와 외부 프로그램 사이에서 정보를 주고 받는 방법이나 규약들을 의미한다.
	- 쉽게말해, 사용자의 요청에 의한 서버의 응답이라고 할 수 있다.

- 왜 CGI가 필요한가요?
	- 초기 웹 서비스에서는 주로 웹사이트에 필요한 정보만을 원하는 측에서 받아가거나 참조하는 방식의 단방향으로 이루어졌지만, 단뱡향이 아닌 클라이언트와 서버 간의 의사 교환이나 정보 교환의 필요성이 생기면서 CGI도 필요하게 되었다.
	- 예를들어, 클라이언트가 로그인을 하기위해 아이디와 비밀번호를 입력하고 서버에 제출을 하게되면 서버는 입력받은 아이디와 비밀번호를 가지고 인증절차를 거친 후 가입되어있는 회원이라면 “~~님 반갑습니다.”와 같은 정보로 로그인에 성공했다고 응답을 클라이언트에게 보내주어야합니다. 이처럼 클라이언트와 서버간의 단방향이 아닌 양방향 의사소통이 필요할 때 CGI가 이 역할을 해주게됩니다.
	
	<br>

### Servlet이란?

- 자바로 구현된 CGI입니다.
- 즉, 웹 프로그래밍에서 클라이언트의 요청을 처리하고 그 결과를 다시 클라이언트에게 전송하는 Servlet 클래의 구현 규칙을 지킨 자바 프로그래밍 기술이라 할 수 있습니다.
- 클라이언트의 요청에 대하여 동적으로 동작하는 웹 애플리케이션 컴포넌트입니다.

<br>

### Servlet의 특징
- HTML을 사용하여 요청에 응답한다.
- Thread를 이용하여 동작
- MVC 패턴에서 Controller로 이용
- javax.servlet.http.HttpServlet 클래스를 상속받는다.
- UDP보다 속도가 느리다.

<br>

### Servlet의 동작 순서
<img width="501" alt="Screen Shot 2020-08-08 at 4 11 24 PM" src="https://user-images.githubusercontent.com/37801041/89704760-d9748980-d991-11ea-80ef-7a2e0a3a4c89.png">

1. 클라이언트가 해당 서버의 Servlet Container로 http request를 보낸다.
2. Servlet Container는 HttpServletRequest, HttpServletResponse 객체를 만든다.
3. Request를 분석해 `web.xml`에 있는 DD(Deployment Descriptor)를 참조하여 어느 서블릿에 대한 요청인지 탐색
4. Servlet Container가 service()를 호출
5. GET 또는 POST 여부에 따라 doGet() 또는 doPost()를 호출
6. doGet()과 doPost()는 동적인 html 페이지를 생성 후 HttpServletResponse 객체에 응답
7. 모두 완료되면 HttpServletRequest, HttpServletResponse 객체를 소멸

<br>

### Servlet의 생명주기
<img width="509" alt="Screen Shot 2020-08-08 at 4 25 41 PM" src="https://user-images.githubusercontent.com/37801041/89704938-d1b5e480-d993-11ea-92c1-2fba16600dab.png">

 - Servlet 객체 생성 : 처음 요청된 경우 메모리에 로딩하여 객체를 생성, 생성된 객체는 메모리에 계속 존재하므로 한 번 생성된 이후 요청이 들어오면 새로 생성이 되지않고 메모리에 존재하는 객체를 사용한다.
- init() : 객체가 생성될 시 최초 한 번만 호출
- service() : 클라이언트의 요청이 있을때 쓰레드를 생성하여 실행, GET과 POST의 여부에 따라 doGet(), doPost()를 실행
- destroy() : 서블릿이 더 이상 필요로 하지 않을 경우 destroy()를 실행하여 연결을 해지

<br>

### Servlet Container란?
- Servlet의 동작 순서의 그림에서 이미 나왔듯이 Servlet을 관리해주는  컨테이너이다.
- 클라이언트의 요청을 받고, 그에대한 응답을 할 수 있게 웹서버와 소켓을 만들어 통신한다.
- 예를들면, Servlet은 어떠한 역할을 수행하는 정의서라고 한다면, Servlet Container는 그 정의서를 보고 그대로 수행하는 것이라고 볼 수 있다.
- Tomcat(톰캣)이 대표적인 예이다.

<br>

### Servlet Container의 역할
- 웹 서버와의 통신 지원
	- 소켓을 만들고 listen, accept 등을 구현해야하지만 이러한 기능들을 API로 제공한다.
- 서블릿 생명주기 관리
- 멀티쓰레드 지원 및 관리
	- 요청이 들어올때마다 서비스 쓰레드를 자동으로 생성하고 역할을 다하면  죽게하여 쓰레드의 안정성에 대하여 걱정을 덜어준다.
- 선언적인 보안관리
	- xml 배포 서술자에 보안관리를 기록하므로 보안에 대한 수정할 일이 생겨도 자바 소스코드를 수정하여 다시 컴파일 하지 않아도 보안관리가 가능

<br>

### 참고 문서
- [1.CGI란무엇인가?](https://www.linux.co.kr/unixwebhosting/cgi/cgi01.htm)
- [JSP 서블릿(Servlet)이란? - MangKyu’s Diary](https://mangkyu.tistory.com/14)