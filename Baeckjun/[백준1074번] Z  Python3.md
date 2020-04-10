# [백준1074번] Z / Python3

## 문제

한수는 2차원 배열 (항상 2^N * 2^N 크기이다)을 Z모양으로 탐색하려고 한다. 예를 들어, 2*2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

![img](https://www.acmicpc.net/upload/201003/z1.JPG)

만약, 2차원 배열의 크기가 2^N * 2^N라서 왼쪽 위에 있는 칸이 하나가 아니라면, 배열을 4등분 한 후에 (크기가 같은 2^(N-1)로) 재귀적으로 순서대로 방문한다.

다음 예는 2^2 * 2^2 크기의 배열을 방문한 순서이다.

![img](https://www.acmicpc.net/upload/201003/z2.JPG)

N이 주어졌을 때, (r, c)를 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

다음 그림은 N=3일 때의 예이다.

![img](https://www.acmicpc.net/upload/201003/z3.JPG)

## 입력

첫째 줄에 N r c가 주어진다. N은 15보다 작거나 같은 자연수이고, r과 c는 0보다 크거나 같고, 2^N-1보다 작거나 같은 정수이다

## 출력

첫째 줄에 문제의 정답을 출력한다.

## 예제 입력 1 

```
2 3 1
```

## 예제 출력 1 

```
11
```

## 예제 입력 2 

```
3 7 7
```

## 예제 출력 2 

```
63
```

<br>

## 나의 풀이

> 이 문제는 재귀를 사용해서 범위를 줄여나가면서 풀면된다. 따라서 `2^n * 2^n`그래프에서 1~4사분면을 나누어서 r과 c가 속하는 사분면에 따라 n을 줄여나가면서 마지막 `n이 1일 경우`에 0~3중 어느 것인지 반환을 해준다. 이후 1분면이라면 그대로 return받은 값을 2사분면이라면 `2^(n-1)`에 해당하는 모든 개수를 더하고 3사분면이라면 `2 * 2^(n-1)`만큼, 4사분면이라면 `3 * 2^(n-1)`을 더해주면 된다. 이 문제를 푸는 핵심원리인 그래프를 사분면으로 나누고 줄여나가는 원리를 생각하고 코드를 보면 쉽게 이해가 갈 것이다.

<br>

## 코드

```python
# 1074번 Z
import sys

# find part
def find(n,y,x):
    if n == 1:
        if y == 0:
            if x == 0:
                return 0
            else:
                return 1
        else:
            if x == 0:
                return 2
            else:
                return 3
    
    half = 2 ** (n-1)
    if 0 <= y < half:
        # 1사분면
        if 0 <= x < half:
            tmp = find(n-1,y,x)
            return tmp
        # 2사분면 
        else:
            tmp = find(n-1,y,x-half)
            return half*half + tmp
    else:
        # 3사분면
        if 0 <= x < half:
            tmp = find(n-1,y-half,x)
            return 2*half*half + tmp
        # 4사분면 
        else:
            tmp = find(n-1,y-half,x-half)
            return 3*half*half + tmp

# main
N, r, c = [int(x) for x in sys.stdin.readline().split()]

print(find(N,r,c))

```

