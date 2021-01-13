# [백준4386번] 별자리 만들기 / Python3

## 문제

도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.

- 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
- 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.

별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.

## 입력

첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)

둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다. 좌표는 1000을 넘지 않는 양의 실수이다.

## 출력

첫째 줄에 정답을 출력한다. 절대/상대 오차는 10-2까지 허용한다.

## 예제 입력 1

```
3
1.0 1.0
2.0 2.0
2.0 4.0
```

## 예제 출력 1

```
3.41
```

<br>

## 나의 풀이

> 해당 문제는 크루스칼 알고리즘을 이용해 MST를 찾아내는 문제였습니다.다. [백준1197번 최소 스패닝 트리](https://hooongs.tistory.com/316) 문제와 크루스칼 알고리즘을 적용하는 것은 동일하지만 여기서는 가중치를 직접 계산해야되는 차이점이 있었습니다.
>
> 따라서, 입력 받은 점들을 배열에 넣어두고 모든 점들의 조합을 따져보면서 거리를 계산한 뒤 최소힙에 `[두 점 사이의 거리, 첫번째 점 인덱스, 두번째 점 인덱스 ]`의 형태로 삽입을 해주는 방식으로 각 점 사이의 간선의 가중치를 구할 수 있었습니다. 이후는 일반적이 유니온-파인드 구조를 접목시켜 크루스칼 알고리즘을 구현하면 쉽게 풀 수 있는 문제였습니다.

<br>

```python
# 4386번 별자리 만들기
from sys import stdin
import math, heapq


def find(x):
    global parent

    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    global parent, rank

    x = find(x)
    y = find(y)

    if x == y:
        return

    if rank[y] > rank[x]:
        x, y = y, x

    parent[y] = x

    if rank[x] == rank[y]:
        rank[y] += 1


def is_same(x, y):
    return find(x) == find(y)


n = int(stdin.readline())
points = []

for _ in range(n):
    x, y = map(float, stdin.readline().split())
    points.append([x, y])

q = []
for i in range(n-1):
    for j in range(i+1, n):
        a = points[i]
        b = points[j]
        diff = math.sqrt(pow(abs(a[0] - b[0]), 2) + pow(abs(a[1] - b[1]), 2))

        heapq.heappush(q, [diff, i, j])

parent = [0] * n
rank = [0] * n
total_cost = 0
for i in range(n):
    parent[i] = i

while q:
    cost, a, b = heapq.heappop(q)

    if not is_same(a, b):
        total_cost += cost
        union(a, b)

print(round(total_cost, 2))


```

