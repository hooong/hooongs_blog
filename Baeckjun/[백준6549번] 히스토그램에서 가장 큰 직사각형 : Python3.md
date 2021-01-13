# [백준6549번] 히스토그램에서 가장 큰 직사각형 / Python3

## 문제

히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다. 각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다. 예를 들어, 왼쪽 그림은 높이가 2, 1, 4, 5, 1, 3, 3이고 너비가 1인 직사각형으로 이루어진 히스토그램이다.

![img](https://www.acmicpc.net/upload/images/histogram.png)

히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.

## 입력

입력은 테스트 케이스 여러 개로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, 직사각형의 수 n이 가장 처음으로 주어진다. (1 ≤ n ≤ 100,000) 그 다음 n개의 정수 h1, ..., hn (0 ≤ hi ≤ 1,000,000,000)가 주어진다. 이 숫자들은 히스토그램에 있는 직사각형의 높이이며, 왼쪽부터 오른쪽까지 순서대로 주어진다. 모든 직사각형의 너비는 1이고, 입력의 마지막 줄에는 0이 하나 주어진다.

## 출력

각 테스트 케이스에 대해서, 히스토그램에서 가장 넓이가 큰 직사각형의 넓이를 출력한다.

## 예제 입력 1

```
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0
```

## 예제 출력 1

```
8
4000
```

<br>

## 나의 풀이

> 이 문제는 스택을 이용하는 방법과 세그먼트 트리와 분할정복을 이용하는 방법이 존재하지만 이번 글에서는 스택을 이용하는 방법만 다뤄보겠습니다. 스택을 이용하는 방법이 시간복잡도도 O(N)에 가까우며 구현도 세그먼트 트리를 사용하는 방법보다 간단하다고 생각이 듭니다.
>
> 스택을 이용하는 방법의 원리는 간단합니다. 배열의 왼쪽에서부터 탐색을 시작해 스택에 최솟값에 대한 정보를 계속 유지해나가면서 스택의 가장 위의 값보다 작은 값이 나온다면 그 값들을 pop하면서 넓이들을 구해보며 넓이의 최댓값을 찾아나가는 것입니다. 아래 그림을 통해 설명을 해보겠습니다.
>
> <div align="center">
>
> <img src="https://user-images.githubusercontent.com/37801041/103910756-8d985d00-5148-11eb-9120-6aa9ced24a2f.jpeg" width=650>
>
> </div>
>
> 이와 같이 사각형의 높이가 주어졌다고 가정해보고 왼쪽(0번 index)부터 탐색을 시작하면서 스택의 변화를 살펴보겠습니다.
>
> <div align="center">
>
> <img src="https://user-images.githubusercontent.com/37801041/103911170-0d262c00-5149-11eb-82e4-d3167c8393dc.jpeg" width=400>
>
> </div>
>
> i가 0일때에는 스택이 비어있었으므로 스택에 0을 push해주고 넘어가게 됩니다.
>
> <div align="center">
>
> <img src="https://user-images.githubusercontent.com/37801041/103911684-a9503300-5149-11eb-9e88-4cb64ac3220e.jpeg" width=300>  <img src="https://user-images.githubusercontent.com/37801041/103911750-c1c04d80-5149-11eb-839b-d78e6af63725.jpeg" width=190>
>
> </div>
>
> 다음으로 i가 1일때를 살펴봅시다. 1번 인덱스의 사각형 높이는 1로 0번째의 사각형보다 작습니다. 따라서 현재 스택에 들어있는 0번을 pop하게 됩니다. pop을 한 뒤, 스택이 비게되는데 이는 곧 i번째까지 최소 높이라는 의미이므로 여기서의 높이는 `(1 * rec[0]) = 2`가 됩니다. 이후 스택이 비어있으므로 1을 push하고 다음으로 넘어가게 됩니다.
>
> <div align="center">
>
> <img src="https://user-images.githubusercontent.com/37801041/103912321-7ce8e680-514a-11eb-9774-fc4569c1d942.jpeg" width=200>  <img src="https://user-images.githubusercontent.com/37801041/103912389-95590100-514a-11eb-89ae-faa3fc9834ac.jpeg" width=200>     
>
> </div>
>
> i는 2와 3일때는 각각 4, 5의 높이를 가지므로 모두 그때의 스택의 가장 위의 값보다 크므로 push를 해주고 넘어가게 됩니다.
>
> <div align="center">
>
> <img src="https://user-images.githubusercontent.com/37801041/103912813-1a441a80-514b-11eb-97cc-c22ed1adfcd4.jpeg" width=400>  <img src="https://user-images.githubusercontent.com/37801041/103912963-55464e00-514b-11eb-8ba9-dc1dc9edb892.jpeg" width=205>
>
> </div>
>
> i는 4일때를 보면, 4번의 사각형의 높이는 1로 3번 사각형과 2번 사각형보다 작은 것을 알 수 있습니다. 이렇게 스택의 가장 위의 값이 현재 사각형의 높이보다 작다면 pop을 해야하는 것은 위에서도 살펴보았습니다. 그러나 위에서는 pop을 한 뒤, 스택이 비어있는 상태가 되어 i를 곱한 값이 그때까지의 직사각형 넓이였다면, 여기서는 스택이 비지 않기때문에 pop을 한 뒤 스택의 가장 위에 있는 인덱스 값을 이용해 직사각형의 width를 구해주어야 합니다. `i - stack[-1] - 1`이 width값이 되게 됩니다. 왜냐하면, pop이 되어진 index는 스택의 가장 위에 있는 인덱스까지의 최솟값이기 때문입니다. 따라서 3, 2를 같은 방식으로 pop을 한 뒤, 4를 push해주고 다음으로 넘어갑니다.
>
> <div align="center">
>
> <img src="https://user-images.githubusercontent.com/37801041/103913811-54fa8280-514c-11eb-9826-9387219edcfa.jpeg" width=200>  <img src="https://user-images.githubusercontent.com/37801041/103913828-5926a000-514c-11eb-9b32-357c0b26434a.jpeg" width=200> 
>
> </div>
>
> i가 5, 6일때에도 모두 push연산만 일어나게 됩니다. 이제 모든 사각형의 넓이를 탐색하게 되었습니다. 그러나 아직 스택이 비어있지 않으므로 이 남은 값들을 모두 처리해보며 가능한 직사각형의 넓이를 확인해보아야합니다. 
>
> <div align="center">
>
> <img src="https://user-images.githubusercontent.com/37801041/103914337-039ec300-514d-11eb-9bf2-38634d013787.jpeg" width=600>
>
> </div>
>
> 스택이 빌때까지 하나씩 차례대로 pop을 하며 앞서 width를 구하던 식에 i대신 n을 넣어 가능한 직사각형의 넓이를 확인해줍니다. 마지막 pop을 할때의 값은 전체 값 중 최소값으로 width는 n으로 계산이 됩니다.
>
> 이렇게 모든 가능한 직사각형의 최대 넓이들을 확인하며 가장 큰 값을 구하면 이 문제를 해결할 수 있습니다. 위의 그림을 아래 코드와 함께 비교해보면서 보시면 이해하기 더 수월할 수 있습니다.

<br>

## 코드

```python
# 6549번 히스토그램에서 가장 큰 직사각형
from collections import deque
import sys

while True:
    rec = list(map(int, sys.stdin.readline().split()))
    n = rec.pop(0)

    if n == 0:
        break

    stack = deque()
    answer = 0

    # 왼쪽부터 차례대로 탐색
    for i in range(n):
        while len(stack) != 0 and rec[stack[-1]] > rec[i]:
            tmp = stack.pop()

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            answer = max(answer, width * rec[tmp])
        stack.append(i)
		
    # 스택에 남아있는 것을 처리
    while len(stack) != 0:
        tmp = stack.pop()

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
        answer = max(answer, width * rec[tmp])

    print(answer)

```



