# [백준4963번] 섬의 개수 / Python3

## 문제

정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

![img](https://www.acmicpc.net/upload/images/island.png)

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

## 출력

각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

## 예제 입력 1 

```
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
```

## 예제 출력 1 

```
0
1
1
3
1
9
```

<br>

## 나의 풀이

> 이 문제는 BFS를 사용해 영역을 구분하는 문제와 비슷한 문제이다. 지금까지 풀어본 영역문제는 모두 상하좌우만 접근이 가능했지만 이 문제에서는 대각선까지 가능하여 각 점에서 총 9곳을 확인해주어야했다. 그리고 이미 방문한 곳에 대한 중복을 없애기 위해서 visited를 만들어 방문한 곳을 표시하여 다시 방문하지 않도록 해주었다. 정리하면 각 테스트 케이스에서 주어진 맵에서 모든 원소를 탐색하되 `1 (즉, 땅인 곳)과 아직 방문을 하지 않은 곳`을 BFS로 넘겨주어 상하좌우 그리고 대각선으로 접근이 가능한 곳에 방문을 하면서 BFS를 한 번 실행할때마다 cnt를 증가시켜주게 되면 최후에는 cnt가 곧 섬의 개수가 된다.

<br>

## 코드

```python
# 4963번 섬의 개수
import sys
from collections import deque

# bfs
def bfs(y,x):
    global board, visited

    q = deque()
    q.append([y,x])

    dy = [-1,-1,-1,0,0,0,1,1,1]
    dx = [-1,0,1,-1,0,1,-1,0,1]
    while q:
        y, x = q.popleft()

        for i in range(9):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny][nx] and board[ny][nx]:
                    visited[ny][nx] = True
                    q.append([ny,nx])

# main
while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    board = []
    for _ in range(h):
        board.append([int(x) for x in sys.stdin.readline().split()])
    
    visited = [[False for _ in range(w)] for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and board[i][j] == 1:
                visited[i][j] = True
                bfs(i,j)
                cnt += 1

    print(cnt)

```

