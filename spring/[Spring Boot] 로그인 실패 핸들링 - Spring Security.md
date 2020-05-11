# [Spring Boot] 로그인 실패 핸들링 - Spring Security

> 입력된 아이디가 없다거나 비밀번호가 틀리다면 로그인을 실패를 할 것이다. 이번 글에서는 로그인이 실패를 했을 경우 어떠한 핸들러를 가지고 처리를 해줄 수 있는지에 대하여 간단한 예제로 살펴보겠습니다.

<br>

<br>

- ### AuthenticationFailureHandler

  `Spring Security에 정의되어 있는 Interface로 이 핸들러를 구현해주고 SecurityConfig에서 설정을 해주면 자동으로 핸들러로 등록이 된다. `

  <br>

- ### onAuthenticationFailure(...)

  `위의 AuthenticationFailureHandler에 정의되어 있는 메서드이다. 매개변수로는 HttpServletRequest(request의 정보를 가지고 있다.), HttpServletResponse(response에 대한 설정을 할 수 있는 변수이다.), AuthenticationException(로그인 실패시 예외에 대한 정보를 가지고 있다.)`

<br>

#### 핸들러에 대해 알아보았으니 이제 코드로 어떻게 작성해야 하는지를 예로 들어보겠습니다.

#### 1. AuthFailureHandler

```java
@Configuration
public class AuthFailureHandler implements AuthenticationFailureHandler {

    @Override
    public void onAuthenticationFailure(HttpServletRequest request, HttpServletResponse response, AuthenticationException exception) throws IOException, ServletException {
        String username = request.getParameter("username");		// request에서 getParameter를 사용하여 "username"에 대한 정보를 가져올 수 있다.
      
      	// 로그인 실패 시 처리할 내용을 작성하여 확장할 수 있다.

        response.sendRedirect("/members/failLogin"); 	// 응답으로 리다이렉트를 보낸다.
      	// 이 예제에서는 간단히 failLogin.html로 리다이렉션을 해주었다.
    }
}
```

<br><br>

### 2. SecurityConfig

```java
@Configuration
@EnableWebSecurity
@AllArgsConstructor
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    private MemberService memberService;
    private AuthFailureHandler authFailureHandler;

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Override
    public void configure(WebSecurity web) throws Exception {
        web.ignoring().antMatchers("/css/**", "/js/**", "/img/**", "/lib/**");
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
                    .antMatchers("/members/signup").permitAll()
                    .antMatchers("/members/failLogin").permitAll()
                    .antMatchers("/**").hasRole("MEMBER")
                    .and()
                .formLogin()
                    .loginPage("/members/login")
                    .failureHandler(authFailureHandler)		// formLogin()의 failureHandler()를 사용해서 위에서 만든 핸들러를 등록해준다. 
                    .permitAll()
                    .and()
                .logout()
                    .logoutRequestMatcher(new AntPathRequestMatcher("/members/logout"))
                    .logoutSuccessUrl("/")
                    .invalidateHttpSession(true)
                    .and()
                .exceptionHandling().accessDeniedPage("/user/denied");
    }

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.userDetailsService(memberService).passwordEncoder(passwordEncoder());
    }
}
```

> `formLogin()` 의 `failureHandler(authFailureHandler)` 로 핸들러를 등록할 수 있다. 주의할 점은 `loginPage()`로 커스텀 로그인 화면을 사용하는 경우 순서에 신경써주어야 한다는 점이다. 핸들러를 `loginPage()`보다 앞에 등록을 해주게되면 커스텀 로그인 화면이 아닌 스프링 시큐리티의 기본 로그인 화면을 사용하게 된다.

<br>

<br>

- ### 실행 화면

  ![Screen Shot 2020-05-11 at 11 32 06 PM](https://user-images.githubusercontent.com/37801041/81573636-b280d880-93df-11ea-8ae8-f502d6becd1f.png)

  <br>

  ![Screen Shot 2020-05-11 at 11 32 15 PM](https://user-images.githubusercontent.com/37801041/81573644-b44a9c00-93df-11ea-8c9d-58da5479b801.png)