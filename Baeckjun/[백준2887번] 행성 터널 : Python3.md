# [백준2887번] 행성 터널 / Python3

## 문제

때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다. 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.

행성은 3차원 좌표위의 한 점으로 생각하면 된다. 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.

민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다. 좌표는 -109보다 크거나 같고, 109보다 작거나 같은 정수이다. 한 위치에 행성이 두 개 이상 있는 경우는 없다. 

## 출력

첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.

## 예제 입력 1

```
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
```

## 예제 출력 1

```
4
```

<br>

## 나의 풀이

> 이 문제는 x, y, z를 각각 기준으로 하여금 정렬을 해서 각 행성별로 이웃한 행성과의 거리를 최소힙에 넣은 뒤 크루스칼 알고리즘을 사용해 MST를 구하는 문제입니다. 문제를 보면 터널을 연결할 때의 비용은 x, y, z들의 차이 중 최솟값인 것을 확인할 수 있습니다. 만약, 모든 행성들에 대하여 이 최솟값을 구하려고 한다면 불가피하게 `O(N^2)`이라는 시간복잡도를 가지게 되는데요... 문제에서 입력 조건이 N이 100,000까지이기 때문에 시간초과가 발생할 것입니다. 그렇기 때문에 이 문제를 풀기 위해서는  조금 다르게 접근을 하는 방법이 필요했습니다. 
>
> 어차피 터널을 연결하는 비용은 x, y, z중 한 좌표의 차이값입니다. 따라서 x, y, z을 모두 따로 생각하여 계산을 해본 뒤 작은 값들부터 확인을 해볼 수 있다는 것입니다. 이러한 접근법을 가지고 더 나아가볼 수 있는데요. 바로 x, y, z를 기준으로 각각 정렬을 해본 뒤 인접한 행성간의 차이값만 비교하는 것입니다. 예를들어, `[1,7,3,4]`가 있을때 정렬을 하면 `[1,3,4,7]`이 됩니다. 여기서 각 인접한 원소 즉, `|1 - 3|`, `|3 - 4|`, `|4 - 7|`만 비교해보면 각 원소들의 최솟값을 구할 수 있습니다. 왜냐하면 1을 기준으로 3이상인 4, 7의 값과의 차이는 어차피 3과 1의 차이보다는 크기때문에 비교해볼 가치가 없기때문입니다. 이렇게 해줌으로써 통로를 만드는데 드는 비용을 계산하는 과정이 정렬하는데 `O(NlonN)`이고, 최솟값을 구하는데 `O(N)`이 들게 됩니다. 앞서 생각했던 `O(N^2)`보다 많이 빨라진 시간이기 때문에 해당 문제를 풀 수 있게됩니다.
>
> 여기서 주의해야할 점이 있습니다. 행성의 좌표들을 저장할 때 행성을 식별할 수 있는 번호(?)를 함께 저장해야한다는 것입니다. 위의 과정에서 x, y, z를 따로따로 정렬을 하기때문에 각각의 차이의 최솟값을 구할 때 행성의 고유한 좌표를 함께 저장해주어야 크루스칼 알고리즘을 적용할 때 문제가 발생하지 않기때문입니다. 
>
> 이제 터널을 연결하는 비용을 담은 최소힙이 만들어졌다면, 이를 가지고 크루스칼 알고리즘을 돌리면 됩니다. MST의 특징으로 N개의 노드가 있다면 간선의 개수는 N-1개가 되는데요. 이 특징을 이용해 반복을 하면서 union이 될때마다 카운트를 증가시켜 이 카운트가 N-1이 된다면 반복을 멈추고 정답을 출력해주면 일반적으로 조금 더 빠른 효율적인 알고리즘이 될 수 있습니다.

<br>

## 코드

```python
# 2887번 행성 터널
import sys, heapq


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

    if rank[x] < rank[y]:
        x, y = y, x

    parent[y] = x

    if rank[x] == rank[y]:
        rank[y] += 1


def is_same(x, y):
    return find(x) == find(y)


n = int(sys.stdin.readline())

planet = []
for i in range(n):
    point = list(map(int, sys.stdin.readline().split()))
    planet.append([i] + point)			# [행성의 고유번호, x, y, z]

parent = [0] * n
rank = [1] * n
for i in range(n):
    parent[i] = i

q = []
# x를 기준으로 정렬
planet.sort(key=lambda x: x[1])
for i in range(n-1):
    heapq.heappush(q, [abs(planet[i][1] - planet[i+1][1]), planet[i][0], planet[i+1][0]])

# y를 기준으로 정렬
planet.sort(key=lambda x: x[2])
for i in range(n-1):
    heapq.heappush(q, [abs(planet[i][2] - planet[i+1][2]), planet[i][0], planet[i+1][0]])

# z를 기준으로 정렬
planet.sort(key=lambda x: x[3])
for i in range(n-1):
    heapq.heappush(q, [abs(planet[i][3] - planet[i+1][3]), planet[i][0], planet[i+1][0]])

cnt = 0
answer = 0
while q:
    cost, a, b = heapq.heappop(q)

    if not is_same(a, b):
        answer += cost
        cnt += 1
        union(a, b)

    if cnt == n-1:
        break

print(answer)

```

