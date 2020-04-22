# [백준2529번] 부등호 / Python3

## 문제

두 종류의 부등호 기호 ‘<’와 ‘>’가 k개 나열된 순서열  A가 있다. 우리는 이 부등호 기호 앞뒤에 서로 다른 한 자릿수 숫자를 넣어서 모든 부등호 관계를 만족시키려고 한다. 예를 들어, 제시된 부등호 순서열 A가 다음과 같다고 하자. 

A =>  < < < > < < > < >

부등호 기호 앞뒤에 넣을 수 있는 숫자는 0부터 9까지의 정수이며 선택된 숫자는 모두 달라야 한다. 아래는 부등호 순서열 A를 만족시키는 한 예이다. 

**3 < 4 < 5 < 6 > 1 < 2 < 8 > 7 < 9 > 0**

이 상황에서 부등호 기호를 제거한 뒤, 숫자를 모두 붙이면 하나의 수를 만들 수 있는데 이 수를 주어진 부등호 관계를 만족시키는 정수라고 한다. 그런데 주어진 부등호 관계를 만족하는 정수는 하나 이상 존재한다. 예를 들어 3456128790 뿐만 아니라 5689023174도 아래와 같이 부등호 관계 A를 만족시킨다. 

**5 < 6 < 8 < 9 > 0 < 2 < 3 > 1 < 7 > 4**

여러분은 제시된 k개의 부등호 순서를 만족하는 (k+1)자리의 정수 중에서 최댓값과 최솟값을 찾아야 한다. 앞서 설명한 대로 각 부등호의 앞뒤에 들어가는 숫자는 { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }중에서 선택해야 하며 **선택된 숫자는 모두 달라야 한다**. 

## 입력

첫 줄에 부등호 문자의 개수를 나타내는 정수 k가 주어진다. 그 다음 줄에는 k개의 부등호 기호가 하나의 공백을 두고 한 줄에 모두 제시된다. k의 범위는 2 ≤ k ≤ 9 이다. 

## 출력

여러분은 제시된 부등호 관계를 만족하는 k+1 자리의 최대, 최소 정수를 첫째 줄과 둘째 줄에 각각 출력해야 한다. 단 아래 예(1)과 같이 첫 자리가 0인 경우도 정수에 포함되어야 한다. 모든 입력에 답은 항상 존재하며 출력 정수는 하나의 문자열이 되도록 해야 한다. 

## 예제 입력 1 

```
2
< > 
```

## 예제 출력 1 

```
897
021
```

<br>

## 나의 풀이

> 해당 문제는 그리디하게 DFS를 돌리면 되는 문제였다. 따라서 필자는 최댓값을 구하는 DFS와 최솟값을 구하는 DFS를 만들어 최댓값과 최솟값을 구하였다.
>
> <br>
>
> - 최솟값을 구하는 DFS
>   - 0부터 9를 순서대로 부등호 식에 넣는다.
>   - 만약 '>'를 만난다면 현재의 값보다 작은 범위의 값에서 반복을 하는데 이 범위에서 가장 작은 값부터 시작.
>     - `예를 들어, 현재값이 5라면 0부터 시작해서 4까지 반복`
>   - 반대로 '<'를 만난다면 현재의 값보다 큰 범위의 값에서 반복을 하는데 이 범위에서 가장 작은 값부서 시작.
>     - `예를 들어, 현재값이 5라면 6부터 시작해서 9까지 반복`
> - 최댓값을 구하는 DFS
>   - 9부터 0을 순서대로 부등호 식에 넣는다.
>   - 만약 '>'를 만난다면 현재의 값보다 작은 범위의 값에서 반복을 하는데 이 범위에서 가장 큰 값부터 시작.
>     - `예를 들어, 현재값이 5라면 4부터 시작해서 0까지 반복`
>   - 반대로 '<'를 만난다면 현재의 값보다 큰 범위의 값에서 반복을 하는데 이 범위에서 가장 큰 값부서 시작.
>     - `예를 들어, 현재값이 5라면 9부터 시작해서 6까지 반복`
>
> <br>
>
> 그리고 visited로 방문 여부를 따져주면서 숫자가 중복이 되는 경우를 방지해주어야한다.

<br>

## 코드

```python
# 2529번 부등호
import sys

# dfs
def min_dfs(answer, cur, cnt):
    global k, signs, min_int, visited

    if cnt == k:
        min_int = answer
        return True

    if signs[cnt] == '>':
        for i in range(cur):
            if not visited[i]:
                visited[i] = True
                if min_dfs(answer+str(i), i, cnt+1):
                    return True
                visited[i] = False
    else:
        for i in range(cur+1,10):
            if not visited[i]:
                visited[i] = True
                if min_dfs(answer+str(i), i, cnt+1):
                    return True
                visited[i] = False

def max_dfs(answer, cur, cnt):
    global k, signs, max_int, visited

    if cnt == k:
        max_int = answer
        return True

    if signs[cnt] == '>':
        for i in range(cur-1,-1,-1):
            if not visited[i]:
                visited[i] = True
                if max_dfs(answer+str(i), i, cnt+1):
                    return True
                visited[i] = False
    else:
        for i in range(9,cur,-1):
            if not visited[i]:
                visited[i] = True
                if max_dfs(answer+str(i), i, cnt+1):
                    return True
                visited[i] = False


# main
k = int(input())
signs = sys.stdin.readline().split()

min_int = ''
max_int = ''
visited = [False for _ in range(10)]
# 작은 값부터
for i in range(10):
    visited[i] = True
    if min_dfs(str(i), i, 0):
        break
    visited[i] = False

visited = [False for _ in range(10)]
# 큰 값부터
for i in range(9,-1,-1):
    visited[i] = True
    if max_dfs(str(i), i, 0):
        break
    visited[i] = False

for num in max_int:
    print(num, end='')
print()

for num in min_int:
    print(num, end='')
print()
```

