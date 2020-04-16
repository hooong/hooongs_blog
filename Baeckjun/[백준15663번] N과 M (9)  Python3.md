# [백준15663번] N과 M (9) / Python3

## 문제

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- N개의 자연수 중에서 M개를 고른 수열

## 입력

첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

## 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제 입력 1 

```
3 1
4 4 2
```

## 예제 출력 1 

```
2
4
```

## 예제 입력 2 

```
4 2
9 7 9 1
```

## 예제 출력 2 

```
1 7
1 9
7 1
7 9
9 1
9 7
9 9
```

## 예제 입력 3 

```
4 4
1 1 1 1
```

## 예제 출력 3 

```
1 1 1 1
```

<br>

## 나의 풀이

> 해당 문제는 단순하게 방문 여부에 대해서만 따져주면 안되는 문제였다. 따라서 입력되는 배열에서 중복되는 것을 제외하고 visited리스트에는 사용가능한 수를 넣어주고 방문마다 하나씩 감소를 시켜주면 되었다. 이렇게 해주어야 중복되는 수열의 출력을 막을 수 있다. 물론 중복된 것을 없애지 않고 모든 수열을 탐색하면서 하나의 리스트를 두어 이미 있는 경우에는 넣지 않고 마지막에 이 리스트를 출력해주는 방법이 있지만 이 방법은 시간초과가 나온다. 따라서 필자는 처음에 입력받는 arr을 set()으로 중복을 없애주고 원래의 arr에 각 요소의 개수를 visited에 저장을해서 DFS로 모든 경우를 탐색하여야한다. 코드를 보면 더 쉽게 이해를 할 수 있을 것이다.

<br>

## 코드

```python
# 15663번 N과 M (9)
import sys

# printS
def printS(s):
    for i in s:
        print(i, end=' ')
    print()

# dfs
def dfs(cur, cnt, s):
    global arr_s, n, m

    if cnt == m:
        printS(s)
        return

    for i in range(len(arr_s)):
        if not visited[i] == 0:
            visited[i] -= 1
            s.append(arr_s[i])
            dfs(i, cnt+1, s)
            visited[i] += 1
            s.pop()

# main
n, m = map(int, input().split())
arr = [int(x) for x in sys.stdin.readline().split()]
arr_s = list(set(arr))

arr_s.sort()
visited = [0 for _ in range(len(arr_s))]
for i in range(len(arr_s)):
    visited[i] = arr.count(arr_s[i])

for i in range(len(arr_s)):
    visited[i] -= 1
    dfs(i,1,[arr_s[i]])
    visited[i] += 1

```

