# [백준1707번] 이분 그래프 / Python3

## 문제

그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

## 입력

입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K(2≤K≤5)가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V(1≤V≤20,000)와 간선의 개수 E(1≤E≤200,000)가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호가 빈 칸을 사이에 두고 주어진다.

## 출력

K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

## 예제 입력 1

```
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
```

## 예제 출력 1

```
YES
NO
```

<br>

## 나의 풀이

> 처음 이 문제를 접하였을때 이분 그래프를 그냥 인접하지 않은 그래프의 집합이 2개가 되는 것을 생각하고 풀었다가 다시 풀었다. 여기서 말하는 이분 그래프란 정점들을 두 집합으로 나누었을때 각 집합안의 정점들은 서로 인접하지 않는 것이다. 다시말해, 서로 인접한 정점은 같은 집합에 들어갈 수 없는 것이다. 따라서 이 문제의 풀이법은 BFS나 DFS를 사용하여 그래프를 탐색하며 인접한 곳을 빨간색과 파란색으로 색을 칠해나가고 탐색을 마친뒤 모든 정점에서 인접한 정점들의 색이 모두 다른색인지 아닌지를 확인하는 것이다. 쉽게 아래 그림을 보면 왼쪽은 각 정점에서 인접한 모든 정점이 다른색인 것을 확인할 수 있다. 따라서 이분 그래프가 될 수 있다. 하지만 오른쪽 그림은 한 정접에서 인접한 정점이 같은 색이 존재한다. 따라서 이분그래프가 될 수 없다는 것을 확인할 수 있다.
>
> ![IMG_EBE0297A6246-1](https://user-images.githubusercontent.com/37801041/78100115-da634080-741e-11ea-9b58-1505df78ecd3.jpeg)
>
> <br>
>
> 필자는 BFS를 사용하여 문제를 풀이하였다. 방문 여부 배열을 두고 방문하지 않은 곳을 시작으로 모든 그래프의 정점을 탐색하였고, 탐색하는 과정에서 각 정접에서 인접한 정점을 큐에 넣을때 `3-color`를 사용하여 `1`과`2`를 번갈아가면서 visit배열에 색을 칠하였다. 그리고나서 모든 정점에서 인접한 정점과의 색을 비교해보고 하나라도 같다면 바로 "NO"를 return해주고 그렇지않다면 "YES"를 return해주었다.

<br>

## 코드

```python
# 1707번 이분 그래프
from collections import deque
import sys

# bfs
def bfs(start):
    global graph, V, visit

    q = deque()
    q.append([start,1])

    while q:
        cur, color = q.popleft()

        for neighbor in graph[cur]:
            if visit[neighbor] == 0:
                # 인접한 곳에 컬러를 변경
                visit[neighbor] = 3 - color
                q.append([neighbor, 3 - color])

# 연결된 노드인데 같은 색이 있는지 확인
def check(visit, graph):
    for i in range(V):
        for node in graph[i]:
            if visit[i] == visit[node]:
                return False
    return True

# main
T = int(input())

for _ in range(T):
    V, E = [int(x) for x in sys.stdin.readline().split()]

    graph = [[] for _ in range(V)]
    for _ in range(E):
        x, y = [int(x) for x in sys.stdin.readline().split()]
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)

    
    visit = [0 for _ in range(V)]
    for i in range(V):
        if not visit[i]:
            visit[i] = 1
            bfs(i)

    if check(visit, graph):
        print("YES")
    else:
        print("NO")

```

