# BOJ(백준) 채점 중 '시간초과'가 뜬다면? 

<br>

<br>

>  vscode나 파이참 같은 다른 IDE에서는 문제없이 돌아가는데 BOJ에 제출만 하면 시간초과 또는 런타임에러가 발생할 경우가 은근히 많은데.... 이런 에러가 나는 대표적인 이유에 대하여 간단하게 팁을 써보겠습니다.

<br>

<br>

- ### 런타임에러

  필자의 경우 런타임 에러의 경우 배열의 인덱스 오류가 아주 유력하다고 생각한다. 예제로 주어지는 것들은 잘돌아가는데 채점에서 쓰이는 테스트 경우들은 index error가 발생할 수도 있으니 잘 생각해보고 다시 문제를 풀어보는 것을 추천한다.

<br>

- ### 시간초과

  이 글의 제목처럼 이 부분을 말하기 위해서 글을 쓰게 되었다. 물론 시간초과는 알고리즘의 시간복잡도가 제일 큰 영향을 끼칠수도 있다. 그러나 시간복잡도가 충분히 낮은 알고리즘이나 자료구조를 사용했는데도 시간초과가 뜨는 경우가 있다. 이러한 경우가 의심이 된다면 python의 경우 `input()` 대신 `sys.stdin.readline()`으로 바꾸면 시간초과가 나지 않을수도 있다. 또한 java의 경우 `Scanner` 대신 `BufferReader의 readLine()`을 사용하면 해결되는 경우도 있다.

  <br>

  - #### python

    ```python
    import sys
    
    # 한 개의 정수를 입력
    n = int(sys.stdin.readline())
    
    # 띄어쓰기로 구분된 두 개의 정수를 입력
    a, b = [int(x) for x in sys.stdin.readline().split()]
    
    # 띄어쓰기로 두 문자열 입력
    c, d = sys.stdin.readline().split()
    
    # 띄어쓰기로 구분되어 있는 배열을 입력
    arr = [int(x) for x in sys.stdin.readline().split()]
    ```

    <br>

  - ####java

    ```java
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    // 한 개의 정수 입력
    n = Integer.parseInt(br.readLine());
    
    // 띄어쓰기로 구분된 정수 입력
    StringTokenizer st = new StrinfTokenizer(br.readLine());
    for (int i=0; i<n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }
    ```

<br>

### 끝마치며...

> 혹시나 저와 같은 시간초과나 런타임에러가 나서 골머리를 앓으면서 검색을 이래저래 하시는 분들이 도움이 되셨으면 하는 바람으로 이렇게 글을 써보았습니다.ㅎㅎ