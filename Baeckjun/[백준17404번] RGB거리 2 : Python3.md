# [백준17404번] RGB거리 2 / Python3

## 문제

RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

- 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
- N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
- i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

## 입력

첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

## 출력

첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

## 예제 입력 1

```
3
26 40 83
49 60 57
13 89 99
```

## 예제 출력 1

```
110
```

<br>

## 나의 풀이

> 해당 문제는 [1149번 RGB거리](https://www.acmicpc.net/problem/1149) 문제에서 1번 집과 마지막 집이 같은 색이면 안되는 조건이 추가되는 문제였다. 
>
> 문제를 해결하는 방법은 첫번째 집의 색을 R, G, B로 각각 지정하고 DP배열을 만들어 최솟값을 구하고 전체적인 최솟값을 찾아내는 것이다. 예를들면, 3개의 집을 색칠할 때 첫번째 집을 R로 지정을 한다면 `dp[1][R]`은 실제 R을 칠하는데 드는 비용을 넣어주고 나머지 `dp[1][G], dp[1][B]`는 `INF`을 넣어주어 2번 집에 칠할 색을 고를 때에 무조건 R의 값만 사용할 수 있도록 만들어줄 수 있다. 이후 `dp[3]`이 완성이 되었다면, `dp[3][R]`을 제외하고 `dp[3][G], dp[3][B]`와 전체 비용의 최솟값과 비교하여 업데이트를 하는 방식인 것이다.

<br>

## 코드

```python
# 17404번 RGB거리 2
from sys import stdin, maxsize
INF = maxsize

n = int(stdin.readline())
cost = [[0] * n for _ in range(n+1)]
dp = [[0] * n for _ in range(n+1)]

for i in range(1, n+1):
    cost[i][0], cost[i][1], cost[i][2] = map(int, stdin.readline().split())

answer = INF
for first in range(3):
    for i in range(3):
        if first == i:
            dp[1][i] = cost[1][i]
        else:
            dp[1][i] = INF

    for i in range(2, n+1):
        dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    for i in range(3):
        if i == first:
            continue
        answer = min(answer, dp[n][i])

print(answer)

```

