# [백준13023번] ABCDE / Python3

## 문제

BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.

오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

- A는 B와 친구다.
- B는 C와 친구다.
- C는 D와 친구다.
- D는 E와 친구다.

위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.

둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 같은 친구 관계가 두 번 이상 주어지는 경우는 없다.

## 출력

문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.

## 예제 입력 1 

```
5 4
0 1
1 2
2 3
3 4
```

## 예제 출력 1 

```
1
```

## 예제 입력 2 

```
5 5
0 1
1 2
2 3
3 0
1 4
```

## 예제 출력 2 

```
1
```

## 예제 입력 3 

```
6 5
0 1
0 2
0 3
0 4
0 5
```

## 예제 출력 3 

```
0
```

## 예제 입력 4 

```
8 8
1 7
3 7
4 7
3 4
4 6
3 5
0 4
2 7
```

## 예제 출력 4 

```
1
```

<br>

## 나의 풀이

> 해당 문제는 DFS, BFS를 사용하여 풀 수 있다. 필자는 DFS를 사용하여 문제를 해결했다. 이 문제에서 "A와 B가 친구이고 B가 C와 친구이고 C가 D와 친구이고 D와 E가 친구 인 경우"를 쉽게 말하면 특정 중복되지 않는 5개의 노드를 잇는 경로가 있는가를 말하는 것이었다. 따라서 주어지는 간선들을 가지고 인접 리스트를 만들고 0번 노드부터 N-1번 노드까지 모든 출발점에 대하여 DFS를 돌려주면서 출발점에 대한 모든 경로에 대해서 5개의 노드를 갈 수 있는 순간 가능하다고 판단을 해주면 된다. DFS 개념이 있고 여러 문제를 풀어보았다면 위의 말과 코드를 보면 쉽게 이해가 갈 것이다.

<br>

## 코드

```python
# 13023번 ABCDE
from collections import deque
import sys

# dfs 
def find(cur, cnt):
    global friends, visited

    if cnt == 5:
        return True
    
    for f in friends[cur]:
        if not visited[f]:
            visited[f] = True
            if find(f, cnt+1):
                return True
            visited[f] = False
    return False    

# main
n, m = map(int, sys.stdin.readline().split())

friends = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

visited = [False for _ in range(n)]
# bfs
for i in range(n):
    visited[i] = True
    isABCDE = find(i,1)
    visited[i] = False

    if isABCDE:
        break

print(1 if isABCDE else 0)
```

