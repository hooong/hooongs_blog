# [백준1197번] 최소 스패닝 트리 / Python3

## 문제

그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

## 입력

첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

## 출력

첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.

## 예제 입력 1

```
3 3
1 2 1
2 3 2
1 3 3
```

## 예제 출력 1

```
3
```

<br>

## 나의 풀이

> 이 문제는 크루스칼 알고리즘을 사용해 최소 스패닝 트리를 찾아내는 문제였습니다. 크루스칼 알고리즘은 Greedy하게 가중치가 작은 간선의 연결된 두 개의 노드를 유니온-파인드를 이용해 낮은 시간복잡도를 가지고 사이클의 여부를 판단해 최소 스패닝 트리를 찾아내는 알고리즘입니다. 따라서 크루스칼 알고리즘의 큰 흐름은 다음과 같습니다.
>
> 1. 입력된 간선 중 제일 작은 가중치를 가진 간선 선택
> 2. 1번에서 고른 간선이 연결하는 두 개의 노드가 같은 집합에 속하는지 확인
>    - 같은 집합에 속한다면 -> 사이클이 존재
>    - 같은 집합엣 속하지 않는다면 -> 해당 간선을 연결(즉, 두 개의 노드를 union)하고 총 가중치에 현재 간선의 가중치 합산
> 3. 모든 간선을 확인할때까지 과정을 반복

<br>

## 코드

```python
# 1197번 최소 스패닝 트리
from sys import stdin
import heapq


def find(x):
    global parent

    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if rank[x] < rank[y]:
        x, y = y, x

    parent[y] = x

    if rank[x] == rank[y]:
        rank[x] += 1


def is_same(x, y):
    return find(x) == find(y)


v, e = map(int, stdin.readline().split())
total_cost = 0

parent = [0] * (v+1)
rank = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

que = []
for _ in range(e):
    a, b, cost = map(int, stdin.readline().split())
    heapq.heappush(que, [cost, a, b])

while que:
    cost, a, b = heapq.heappop(que)

    if not is_same(a, b):
        union(a, b)
        total_cost += cost

print(total_cost)

```

