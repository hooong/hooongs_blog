# [Spring Boot] Thymeleaf를 사용해 PathVariable 넘기는 방법

> CRUD에서 Create를 제외하고는 URL에 해당 객체의 id값을 넘겨주어서 구현을 해줄 수 있다. Spring Boot에서는 Controller에서 @PathVariable 어노테이션을 사용하여 URL의 인자값을 전달받을 수 있는데 그렇다면 Thymeleaf에서는 어떠한 방법으로 id값을 넘겨주어야 되는지에 대하여 알아보겠다.

<br>

<br>

- ### Controller에서 delete를 처리하는 메서드

  ```java
  @GetMapping("todoDelete/{id}")
  public String delete(@PathVariable Long id) {
    todoService.delTodo(id);
  
    return "redirect:/";
  }
  ```

  > URL에서 id값을 받아 해당 todo post를 지우는 간단한 코드입니다.

<br><br>

- ### todo를 보여주는 Html

  ```html
  <tbody>
    <tr th:each="todo : ${todos}">
      <td th:text="${todo.id}"></td>
      <td th:text="${todo.title}"></td>
      <td th:text="${todo.subtitle}"></td>
      <td><a th:href="@{/todoDelete/{id}(id = ${todo.id})}"><button>완료</button></a></td>
    </tr>
  </tbody>
  ```

  > 위의 코드는 thymeleaf의 `th:each` 를 사용하여 모든 todo를 띄워주고 있는 코드입니다. 각각의 id, title, subtitle를 보여주고 그 마지막으로 `th:href="@{/todoDelete/{id}(id = ${todo.id})}"` 의 태그를 사용하여 완료 (즉, todo를 삭제하는 버튼)을 만들어주었습니다. 무심코 `href="/todoDelete/${todo.id}"`로 써보았지만 안되어서 위와같은 방법을 찾아냈습니다.