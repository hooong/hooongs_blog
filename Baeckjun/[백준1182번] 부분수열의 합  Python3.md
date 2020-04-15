# [백준1182번] 부분수열의 합 / Python3

## 문제

N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

## 출력

첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

## 예제 입력 1

```
5 0
-7 -3 -2 5 8
```

## 예제 출력 1 

```
1
```

<br>

## 나의 풀이

> DFS를 사용해서 주어진 배열에서 가능한 모든 합을 구하면서 합이 s가 되는 순간에 cnt를 증가시키면 되는 문제이다.

<br>

## 코드

```python
# 1182번 부분수열의 합
import sys

# dfs
def dfs(cur,cur_s):
    global n, s, arr, cnt
    
    if cur_s == s:
        cnt += 1

    for i in range(cur+1,n):
        dfs(i,cur_s+arr[i])

# main
n, s = map(int, input().split())
arr = [int(x) for x in sys.stdin.readline().split()]

cnt = 0
for i in range(n):
    dfs(i,arr[i])

print(cnt)

```

