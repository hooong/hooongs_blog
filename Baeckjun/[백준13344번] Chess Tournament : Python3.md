# [백준13344번] Chess Tournament / Python3

## 문제

Your friend is an organizer of the International Chess Playing Championship. He is worried that some of the contestants may be cheating, and he has asked you to help out. The chess players are allowed to report matches to the jury themselves, and this is not checked with the reported opponent. So, it is possible for competitors to make up matches and falsely report themselves as the winners.

Since chess is a game of skill, and not of chance, a player will always beat their opponent if their skill level is higher. A game will result in a draw if and only if the two players’ skills are exactly equal.

However, the skill level of the players is not known. He has therefore asked you to write a program that, given a list of reported matches, determines whether this list is consistent or not. The list is inconsistent if we can determine that at least reported match is falsely reported, otherwise it is consistent.

## 입력

The first line contains two integers N (2 ≤ N ≤ 50 000) and M (1 ≤ M ≤ 250 000), to describe a championship with N players and M reported matches.

The following M lines each consist of an integer K, a symbol which is either ‘=’ or ‘>’, and another integer L. The integers K and L each uniquely identify a player (0 ≤ K, L < N). If the symbol is ‘=’, then the game between K and L was a draw. If the symbol is ‘>’, then K beat L in a match.

You may assume that there is at most one reported match between any given pair of players. Also, each player takes part in at least one reported match.

## 출력

Output a single line containing a single word: “consistent” if the list of recorded matches is consistent, and “inconsistent” if it is not.

## 예제 입력 1 

```
3 3
0 > 1
1 = 2
0 = 2
```

## 예제 출력 1 

```
inconsistent
```

## 예제 입력 2 

```
5 5
0 = 1
1 = 2
3 = 4
0 > 3
1 > 4
```

## 예제 출력 2 

```
consistent
```

## 예제 입력 3 

```
6 5
0 > 1
1 > 2
3 = 4
4 = 5
5 > 3
```

## 예제 출력 3 

```
inconsistent
```

<br>

## 나의 풀이

> 처음 문제를 접하고 `>` 이긴 경우에 대해서 방향이 있는 간선을 그리고 싸이클을 찾아내면 되겠다는 생각으로 출발을 하였다. 그러나 `=` 비긴 경우에 도대체 간선을 어떻게 그리지?라는 생각을 하다가 결국 검색을 통해 힌트를 얻었다. 문제의 해결법은 바로 서로소 집합이었다. 비긴 경우들에 대해서 유니온 파인드를 이용하여 서로소 집합을 만들고나서 저장해두었던 `>` 이긴 경우에 대하여 root의 노드들만 가지고 인접리스트와 진입차수를 계산한 뒤 위상정렬 알고리즘을 통해 싸이클이 존재하는지를 알아내면 된다.
>
> 예를 들어, 예제 1번의 경우 `0, 1, 2`가 모두 같은 집합에 속하게 된다. 따라서 `0 > 1`에서 `find(0)`과 `find(1)`이 같은 값이 나오게되고 결국 싸이클이 존재하게 되는 것이다. 
>
> 유니온 파인드와 위상정렬을 조합해서 푼다는 힌트를 보고 감탄하면서 재밌게 풀었던 문제였다^^

<br>

## 코드

```python
# 13344번 Chess Tournament
import sys
from collections import deque


def find(x):
    global parents

    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]


def union(x, y):
    global rank, parents

    x = find(x)
    y = find(y)

    if x != y:
        if rank[x] > rank[y]:
            x, y = y, x

        parents[x] = y

        if rank[x] == rank[y]:
            rank[y] += 1


n, m = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(n)]
in_degree = [0] * n

parents = [0] * n
rank = [1] * n
for i in range(n):
    parents[i] = i

tmp = []
for _ in range(m):
    a, op, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)

    if op == '>':
        tmp.append([a, b])
    else:
        union(a, b)

for a, b in tmp:
    a = find(a)
    b = find(b)

    adj_list[a].append(b)
    in_degree[b] += 1

cnt = 0
q = deque()
for i in range(n):
    if in_degree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    cnt += 1

    for there in adj_list[cur]:
        in_degree[there] -= 1
        if in_degree[there] == 0:
            q.append(there)

print("consistent" if cnt == n else "inconsistent")

```

