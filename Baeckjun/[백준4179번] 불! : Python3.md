# [백준4179번] 불! / Python3

## 문제

지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!

미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.

지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동한다. 

불은 각 지점에서 네 방향으로 확산된다. 

지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다. 

지훈이와 불은 벽이 있는 공간은 통과하지 못한다.

## 입력

입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수이다.

다음 입력으로 R줄동안 각각의 미로 행이 주어진다.

 각각의 문자들은 다음을 뜻한다.

- \#: 벽
- .: 지나갈 수 있는 공간
- J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
- F: 불이 난 공간

J는 입력에서 하나만 주어진다.

## 출력

지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.

지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다. 

## 예제 입력 1

```
4 4
####
#JF#
#..#
#..#
```

## 예제 출력 1

```
3
```

<br>

## 나의 풀이

> 지훈이가 최단 경로로 탈출을 하는 문제로 BFS로 풀이할 수 있다. 이 문제에서 핵심은 각 단계별로 불을 먼저 확산시키고 지훈이를 이동시키는 것이었다. 왜냐하면, 만약에 지훈이가 먼저 움직여 이번 단계에서 불이 확산되는 위치로 갈 경우 문제가 생기기때문이다. 따라서 BFS로 각 단계별로 존재하는 불의 인접한 곳으로 불을 모두 확산시킨 뒤 같은 단계에서의 지훈이의 이동을 확인해보면 문제를 해결할 수 있었다.

<br>

## 코드

```python
# 4179번 불!
from collections import deque
import sys, heapq


def bfs():
    global board, start, fire

    visited = [[False] * c for _ in range(r)]
    move = list()
    heapq.heappush(move, [0, start[0], start[1]])
    visited[start[0]][start[1]] = True
    while move:
      
      	# 불의 확산
        f_size = len(fire)
        for _ in range(f_size):
            f_y, f_x = fire.popleft()

            for i in range(4):
                f_ny = f_y + dy[i]
                f_nx = f_x + dx[i]

                if 0 <= f_ny < r and 0 <= f_nx < c:
                    if board[f_ny][f_nx] == '.' or board[f_ny][f_nx] == 'J':
                        board[f_ny][f_nx] = 'F'
                        fire.append([f_ny, f_nx])

        # 지훈이 이동
        m_size = len(move)
        for _ in range(m_size):
            cnt, cur_y, cur_x = heapq.heappop(move)

            for i in range(4):
                ny = cur_y + dy[i]
                nx = cur_x + dx[i]

                if 0 <= ny < r and 0 <= nx < c:
                    if not visited[ny][nx] and board[ny][nx] == '.':
                        visited[ny][nx] = True
                        heapq.heappush(move, [cnt+1, ny, nx])
                else:
                    return cnt + 1
    return 'IMPOSSIBLE'


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(r)]

start = []
fire = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            start = [i, j]
        if board[i][j] == 'F':
            fire.append([i, j])

print(bfs())

```

