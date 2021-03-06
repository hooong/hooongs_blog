# [백준1956번] 운동 / Python3

## 문제

V개의 마을와 E개의 도로로 구성되어 있는 도시가 있다. 도로는 마을과 마을 사이에 놓여 있으며, 일방 통행 도로이다. 마을에는 편의상 1번부터 V번까지 번호가 매겨져 있다고 하자.

당신은 도로를 따라 운동을 하기 위한 경로를 찾으려고 한다. 운동을 한 후에는 다시 시작점으로 돌아오는 것이 좋기 때문에, 우리는 사이클을 찾기를 원한다. 단, 당신은 운동을 매우 귀찮아하므로, 사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.

도로의 정보가 주어졌을 때, 도로의 길이의 합이 가장 작은 사이클을 찾는 프로그램을 작성하시오. 두 마을을 왕복하는 경우도 사이클에 포함됨에 주의한다.

## 입력

첫째 줄에 V와 E가 빈칸을 사이에 두고 주어진다. (2 ≤ V ≤ 400, 0 ≤ E ≤ V(V-1)) 다음 E개의 줄에는 각각 세 개의 정수 a, b, c가 주어진다. a번 마을에서 b번 마을로 가는 거리가 c인 도로가 있다는 의미이다. (a → b임에 주의) 거리는 10,000 이하의 자연수이다. (a, b) 쌍이 같은 도로가 여러 번 주어지지 않는다.

## 출력

첫째 줄에 최소 사이클의 도로 길이의 합을 출력한다. 운동 경로를 찾는 것이 불가능한 경우에는 -1을 출력한다.

## 예제 입력 1

```
3 4
1 2 1
3 2 1
1 3 5
2 3 2
```

## 예제 출력 1

```
3
```

<br>

## 나의 풀이

> 처음에 다익스트라로 모든 마을을 시작으로 최소 거리들을 구한 후 더하면서 최솟값을 구하는 방법을 생각했지만 시간초과가 나왔다. 따라서 플로이드-와샬을 사용하여 풀이를 하였다.
>
> 원래 플로이드-와샬은 자기 자신의 가중치를 0으로 두지만 이 문제에서는 INF로 두고 자기 자신으로 돌아오는 경우도 체크를 해주었다. 모든 반복을 마친 후 `distance[i][i]`들 중 최솟값을 반환해주면 되는 은근히 간단한 문제? 였다.

<br>

## 코드

```python
# 1956번 운동
from sys import stdin, maxsize
INF = maxsize

v, e = map(int, stdin.readline().split())
distance = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    distance[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

ans = INF
for i in range(1, v+1):
    ans = min(ans, distance[i][i])

print(-1 if ans == INF else ans)

```

