# [백준6603번] 로또 / Python3

## 문제

독일 로또는 {1, 2, ..., 49}에서 수 6개를 고른다.

로또 번호를 선택하는데 사용되는 가장 유명한 전략은 49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것이다.

예를 들어, k=8, S={1,2,3,5,8,13,21,34}인 경우 이 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지이다. ([1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34])

집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있다. 첫 번째 수는 k (6 < k < 13)이고, 다음 k개 수는 집합 S에 포함되는 수이다. S의 원소는 오름차순으로 주어진다.

입력의 마지막 줄에는 0이 하나 주어진다. 

## 출력

각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다. 이때, 사전 순으로 출력한다.

각 테스트 케이스 사이에는 빈 줄을 하나 출력한다.

## 예제 입력 1

```
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
```

## 예제 출력 1

```
1 2 3 4 5 6
1 2 3 4 5 7
1 2 3 4 6 7
1 2 3 5 6 7
1 2 4 5 6 7
1 3 4 5 6 7
2 3 4 5 6 7

1 2 3 5 8 13
1 2 3 5 8 21
1 2 3 5 8 34
1 2 3 5 13 21
1 2 3 5 13 34
1 2 3 5 21 34
1 2 3 8 13 21
1 2 3 8 13 34
1 2 3 8 21 34
1 2 3 13 21 34
1 2 5 8 13 21
1 2 5 8 13 34
1 2 5 8 21 34
1 2 5 13 21 34
1 2 8 13 21 34
1 3 5 8 13 21
1 3 5 8 13 34
1 3 5 8 21 34
1 3 5 13 21 34
1 3 8 13 21 34
1 5 8 13 21 34
2 3 5 8 13 21
2 3 5 8 13 34
2 3 5 8 21 34
2 3 5 13 21 34
2 3 8 13 21 34
2 5 8 13 21 34
3 5 8 13 21 34
```

<br>

## 나의 풀이

> DFS나 BFS를 사용하여 해결할 수 있는 문제이다. 그래서 DFS와 BFS 두 가지 모두 구현을 해보았다.
>
> <br>
>
> - BFS
>
>   우선 입력받는 배열 s를 오름차순으로 정렬을 하여 넘겨주는 방법으로 하였다. 그리고 k개 중 6개를 뽑아야하기 때문에 bfs를 시작할 때 처음에 queue에 넣어주는 것은 앞에서부터 k개 중에서 6개를 뽑아낼 수 있는 범위인 `range((k-6)-1)`만큼을 list형태로 넣어주고 시작을 했다. 그리고나서는 큐에서 뽑아진 list의 크기가 6개라면 출력을 해주고 그렇지않다면 s에 대해 모든 원소를 반복하면서 큐에서 뽑아진 list의 마지막 값보다 크다면 맨뒤에 추가를 해주고 큐에도 이 list를 push해주었다. 참고로 이 문제에서도 cur이라는 배열이 얕은 복사가 일어나서 문제가 되었지만 `deepcopy()`를 사용해서 해결해냈다.
>
> <br>
>
> - DFS
>
>   dfs의 경우에는 배열에서 현재 위치의 인덱스 정보를 계속 유지해나가면서 각 단계마다 현재위치부터 s배열의 마지막까지 반복을 해가면서 재귀를 통해 6개가 되는지를 확인하고 재귀가 끝나면 다시 추가했던 원소를 빼서 반복을 해주는 과정을 통해 구현하였다. 이 부분은 코드로 보는 것이 더 쉽게 이해가 갈 것이다.

<br>

## 코드

- BFS

  ```python
  # 6603번 로또
  from collections import deque
  import sys, copy
  
  # bfs
  def bfs(s, k):
      q = deque()
      
      for i in range(k-5):
          q.append([s[i]])
  
      while q:
          lotto = q.popleft()
  
          if len(lotto) == 6:
              for i in lotto:
                  print(i, end=' ')
              print()
  
          for num in s:
              if num > lotto[-1]:
                  tmp = copy.deepcopy(lotto)
                  tmp.append(num)
                  q.append(tmp)
  
  # main
  while True:
      # input array
      s = [int(x) for x in sys.stdin.readline().split()]
      k = s.pop(0)
  
      # end of testcase
      if k == 0:
          break
  
      s.sort()
      bfs(s, k)
      print()
      
  ```

- DFS

  ```python
  # 6603번 로또
  from collections import deque
  import sys
  
  # dfs
  def dfs(s, cur, pos):
      if len(cur) == 6:
          for i in cur:
              print(i, end=' ')
          print()
          return
  
      for i in range(pos, len(s)):
          if pos < len(s):
              cur.append(s[i])
              dfs(s,cur,i+1)
              cur.pop()
  
  # main
  while True:
      # input array
      s = [int(x) for x in sys.stdin.readline().split()]
      k = s.pop(0)
  
      # end of testcase
      if k == 0:
          break
  
      s.sort()
      dfs(s,[],0)
      print()
      
  ```

  