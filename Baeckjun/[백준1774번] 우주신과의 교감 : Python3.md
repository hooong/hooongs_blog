# [백준1774번] 우주신과의 교감 / Python3

## 문제

황선자씨는 우주신과 교감을 할수 있는 채널러 이다. 하지만 우주신은 하나만 있는 것이 아니기때문에 황선자 씨는 매번 여럿의 우주신과 교감하느라 힘이 든다. 이러던 와중에 새로운 우주신들이 황선자씨를 이용하게 되었다.

하지만 위대한 우주신들은 바로 황선자씨와 연결될 필요가 없다. 이미 황선자씨와 혹은 이미 우주신끼리 교감할 수 있는 우주신들이 있기 때문에 새로운 우주신들은 그 우주신들을 거쳐서 황선자 씨와 교감을 할 수 있다.

우주신들과의 교감은 우주신들과 황선자씨 혹은 우주신들 끼리 이어진 정신적인 통로를 통해 이루어 진다. 하지만 우주신들과 교감하는 것은 힘든 일이기 때문에 황선자씨는 이런 통로들이 긴 것을 좋아하지 않는다. 왜냐하면 통로들이 길 수록 더 힘이 들기 때문이다.

또한 우리들은 3차원 좌표계로 나타낼 수 있는 세상에 살고 있지만 우주신들과 황선자씨는 2차원 좌표계로 나타낼 수 있는 세상에 살고 있다. 통로들의 길이는 2차원 좌표계상의 거리와 같다.

이미 황선자씨와 연결된, 혹은 우주신들과 연결된 통로들이 존재한다. 우리는 황선자 씨를 도와 아직 연결이 되지 않은 우주신들을 연결해 드려야 한다. 새로 만들어야 할 정신적인 통로의 길이들이 합이 최소가 되게 통로를 만들어 “빵상”을 외칠수 있게 도와주자.

## 입력

첫째 줄에 우주신들의 개수(N<=1,000) 이미 연결된 신들과의 통로의 개수(M<=1,000)가 주어진다.

두 번째 줄부터 N개의 줄에는 황선자를 포함하여 우주신들의 좌표가 (0<= X<=1,000,000), (0<=Y<=1,000,000)가 주어진다. 그 밑으로 M개의 줄에는 이미 연결된 통로가 주어진다. 번호는 위의 입력받은 좌표들의 순서라고 생각하면 된다. 좌표는 정수이다.

## 출력

첫째 줄에 만들어야 할 최소의 통로 길이를 출력하라. 출력은 소수점 둘째짜리까지 출력하여라.

## 예제 입력 1

```
4 1
1 1
3 1
2 3
4 3
1 4
```

## 예제 출력 1

```
4.00
```

<br>

## 나의 풀이

> 해당 문제는 크루스칼 알고리즘을 적용하여 푸는 문제였습니다. [백준4386번 별자리 만들기](https://hooongs.tistory.com/317)문제와 매우 유사한 문제였습니다. 다만, 다른점은 입력에서 이미 연결되어 있는 점들을 알려주는데 이것들을 우선 union을 해주고 난 뒤 '별자리 만들기'문제와 같은 방법으로 풀면 쉽게 풀리는 문제였습니다.

<br>

## 코드

```python
# 1774번 우주신과의 교감
import sys, math, heapq


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
        return False

    if rank[x] < rank[y]:
        x, y = y, x

    parent[y] = x

    if rank[x] == rank[y]:
        rank[y] += 1
    return True


def calc_diff(a, b):
    return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))


n, m = map(int, sys.stdin.readline().split())

answer = 0
parent = [0] * (n+1)
rank = [1] * (n+1)
for i in range(1, n+1):
    parent[i] = i

god = [0]
for _ in range(n):
    god.append(list(map(int, sys.stdin.readline().split())))

# 이미 존재하는 간선들의 MST
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

# 아직 연결되지 않은 곳 최소 간선으로 연결
q = []
for i in range(1, n):
    for j in range(i+1, n+1):
        diff = calc_diff(god[i], god[j])
        heapq.heappush(q, [diff, i, j])

while q:
    cost, a, b = heapq.heappop(q)

    if union(a, b):
        answer += cost

print("%0.2f" % answer)

```

