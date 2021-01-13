# [Algorithm] KMP 알고리즘 with Python

### KMP(Knuth-Morris-Pratt)은 무엇인가?

KMP는 대표적인 문자열 매칭 알고리즘으로, 문자열과 패턴이 주어질 때 문자열 안에서 주어진 패턴을 찾아내는 알고리즘이다. 만약, 길이가 1,000,000인 문자열과 길이가 10,000인 패턴이 주어졌을 때 단순하게 모든 문자열의 경우의 수를 확인한다면 시간 복잡도는 `1,000,000 * 10,000`이 될 것이다. 즉, `O(N^2)`이 된다. 그러나 KMP 알고리즘을 사용한다면 사실상 `O(N)`으로 시간 복잡도를 줄일 수 있다. 이렇게 시간 복잡도를 줄일 수 있는 이유는 접두사, 접미사를 이용하여 불필요하게 반복되는 연산을 줄이기 때문이다.

<br>

## 접두사, 접미사 최대 개수를 담은 table 생성

앞서 말한 과정에서 미리 계산해 둔 접두사, 접미사 정보를 활용한다고 나온다. 이에 해당하는 정보는 패턴의 `0 ~ i`부분에서 접두사와 접미사가 같은 최대 개수를 활용하는 것이다.

패턴이 `abcdabc`로 주어질 때, 접두사와 접미사가 같은 최대 수는 다음과 같다.

![IMG_212ED7091794-1](https://user-images.githubusercontent.com/37801041/102799590-15b2fe80-43f6-11eb-8485-0a7e9164f159.jpeg)

이에 대한 정보를 리스트에 저장을 해주어야한다. 이를 만드는 알고리즘은 다음과 같다.

`j`는 0번부터 `i`는 1번부터 시작한다.

![IMG_5506FCF60492-1](https://user-images.githubusercontent.com/37801041/102799754-45620680-43f6-11eb-86e4-f6b88d2b698f.jpeg)

`j`와 `i`가 같이 않다면 `i`를 증가시킨다.

![IMG_11CCF0E1B1FD-1](/Users/hooong/Downloads/IMG_11CCF0E1B1FD-1.jpeg)

만약, `i`와 `j`가 같다면 `j`를 1만큼 증가시킨 후 `table[i]`에 저장한다. 이후 `i`를 증가시킨다.

![IMG_C6D93BBC39A3-1](https://user-images.githubusercontent.com/37801041/102800174-d802a580-43f6-11eb-8db2-99f869811b6e.jpeg)

여기서는 `i`와 `j`가 같지 않고 `j`가 0보다 큰 상태이다. 이때는 `j`가 0이거나 `i`와 `j`가 같을때까지 `j`의 값을 `table[j-1]`의 값으로 바꾸어준다. 여기서는 이 과정을 한번만 거치기 때문에 `j`가 0이 되고 `i`를 증가시킨다.

![IMG_215D7C08D500-1](https://user-images.githubusercontent.com/37801041/102800561-637c3680-43f7-11eb-8a74-6cc877531820.jpeg)

이후부터는 `i`와 `j`가 계속 일치하여 모두 증가하게되고 문자열이 끝나 해당 알고리즘이 종료된다. 결과적으로 해당 알고리즘을 코드로 짜면 다음과 같이 짤 수 있다.

```python
def make_table(p):
    global table

    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:	# j가 0이거나 i와 j 문자가 같을때까지 반복
            j = table[j-1]

        if p[i] == p[j]:	# i와 j의 문자가 같다면 j를 증가
            j += 1
            table[i] = j	# i번째 요소에는 j를 저장

            
if __name__ == "__main__":
    pattern = "abacaba"

    table = [0] * len(pattern)
    
    make_table(pattern)
```

<br>

### KMP 함수 작성

최대 일치하는 접두사와 접미사를 구했다면 이제 이를 활용하여 KMP 알고리즘을 완성시켜야한다. 우선 크게 `i`인덱스로 문자열을 `j`인덱스로 패턴을 탐색하게 된다. 탐색을 하면서 문자열의 `i`번째 문자와 패턴의 `j`번째 문자가 같다면 두 인덱스를 모두 증가시키며 탐색을 이어가되 `j`와 `패턴 문자열의 크기-1`이 같을 때 매칭에 성공한 것으로 판단을 해주어야한다.

이제 문제는 문자열의 `i`번째 문자와 패턴의 `j`번째 문자가 다를 경우이다. 

![IMG_18C570CC8053-1](https://user-images.githubusercontent.com/37801041/102801886-316bd400-43f9-11eb-862f-d99663ffa8a5.jpeg)

위의 예시를 보면 `aba`까지는 같지만 `b`와 `c`가 다르다. 하지만 문자열에서 뒤쪽의 `ab`는 패턴의 처음 `ab`와 같아 만약 또 확인을 하게 된다면 불필요한 반복이 발생하게 된다. 이를 방지하고자 위에서 구한 최대 접두사와 접미사 table을 활용하게 된다. 위와 같이 불일치가 발생하게 되면 `j`를 0이거나 문자열의 `i`번째 문자와 같을때까지 `j`를  `table[j-1]`의 값으로 업데이트 해준다. 

위의 예에서는 `c`와 `b`가 일치하지 않으니 `j`는 `table[j-1]`인 `table[2]`의 값으로 업데이트되는데 이는 1로써 `j`는 `b`를 가리키게 된다. 여기서 문자열의 `i`번째 문자인 `b`와 같기때문에 반복을 멈추고 `j`와 `i`를 증가시키고 다음 문자들을 확인하게된다.

아래는 KMP 알고리즘의 전체 코드이다.

```python
def KMP(s, p):
    global table

    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]

        if s[i] == p[j]:
            if j == len(p)-1:
                print("find", end='')
                print(i - len(p) + 2)
                j = table[j]
            else:
                j += 1


def make_table(p):
    global table

    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]

        if p[i] == p[j]:
            j += 1
            table[i] = j


if __name__ == "__main__":
    string = "abacdabacaabacaaba"
    pattern = "abacaaba"

    table = [0] * len(pattern)
    make_table(pattern)

    KMP(string, pattern)

```

<br>

### 정리하며...

이번 글에서는 문자열 매칭 알고리즘인 KMP 알고리즘에 대하여 알아보았습니다. 처음 KMP 알고리즘이라는 이름을 보고 아주 이해하기 어려울줄만 알았지만, 직접 예제를 그림으로 과정을 그려보며 알고리즘을 공부해보니 생각보다는 쉽게 이해를 했던 것 같습니다. 해당 글이 설명이 부족할 수도 있지만 이 알고리즘을 검색해서 찾아보았다면 충분히 코드를 읽어보고 차근차근 예제를 그림으로 직접 그려본다면 쉽게 이해할 수 있을거라고 예상합니다. 부족한 글 읽어주신 점 감사드립니다^^