# [백준2589번] 보물섬 / Python3

## 문제

보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다. 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.

![img](https://www.acmicpc.net/upload/images/c1bYIsKpI6m317EAx.jpg)

예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고, 이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.

![img](https://www.acmicpc.net/upload/images/XqDkWCRUWbzZ.jpg)

보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다. 이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다. 보물 지도의 가로, 세로의 크기는 각각 50이하이다.

## 출력

첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다.

## 예제 입력 1

```
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
```

## 예제 출력 1

```
8
```

<br>

## 나의 풀이

> 이 문제는 생각보다 간단하다. 모든 육지의 좌표에 대하여 BFS를 돌려서 최댄 경로에 대한 최댓값을 구하면 된다. BFS의 장점으로는 최단 경로들이 저장이 된다는 것이다. 그럼 이 장점을 활용해서 육지인 좌표에서 출발하여 도달할 수 있는 모든 곳의 최단 경로의 길이를 구하게 되고 각각의 출발 지점에서 최단경로의 길이 중에서 최댓값을 계속 업데이트해나가면 문제가 풀린다. 
>
> <br>
>
> 1. 보물 지도를 입력을 받는다.
>    1. 입력을 받는 과정에서 'L'인 곳의 좌표를 따로 배열에 저장한다.
> 2. 육지인 곳의 좌표들을 반복하여 한 곳씩 시작지점으로 BFS에 넣어준다.
> 3. BFS를 돌면서 각 지점에 도달때 필요한 경로의 길이를 저장한다.
>    - 여기서 전역변수로 최댓값을 저장하는 변수를 현재의 최댓값과 현재 지점에 도달하는데 필요한 시간 중 큰 값을 저장한다.
> 4. 모든 육지에 대하여 BFS를 돌고나면 최댓값을 저장하는 변수에는 가능한 모든 최단 경로 중 최댓값이 저장이 되어있다.

<br>

## 코드

```python
# 2589번 보물섬
from collections import deque
import sys

# bfs
def bfs(x, y):
    global h, w, board, maxLen

    visited = [[-1 for _ in range(w)] for _ in range(h)]
    visited[y][x] = 0

    q = deque()
    q.append([x,y])

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while q:
        x, y = q.popleft()
        maxLen = max(maxLen, visited[y][x])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h:
                if visited[ny][nx] == -1 and board[ny][nx] == 'L':
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([nx,ny])

# main
h, w = [int(x) for x in sys.stdin.readline().split()]

board = []
lands = []
for y in range(h):
    row = sys.stdin.readline()
    board.append(row)
    for x in range(w):
        if row[x] == 'L':
            lands.append([x,y])
    
maxLen = 0
for land in lands:
    bfs(land[0], land[1])

print(maxLen)

```

