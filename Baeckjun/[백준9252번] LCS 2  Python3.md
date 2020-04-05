# [백준9252번] LCS 2 / Python3

## 문제

LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

## 입력

첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

## 출력

첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

LCS가 여러 가지인 경우에는 아무거나 출력하고, LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.

## 예제 입력 1

```
ACAYKP
CAPCAK
```

## 예제 출력 1

```
4
ACAK
```

<br>

## 나의 풀이

> [9251번 LCS](https://hooongs.tistory.com/64) 문제에 해당되는 가장 긴 문자열까지 찾은 문제였다. 이전 문제에서 LCS의 길이를 구하는 법은 설명하였으니 생략하겠다. 
>
> <br>
>
> 이제 문제는 해당 문자열을 찾는 것이었다. 필자는 처음에 dp가 완성되고 마지막 행에서의 첫번째로 각각의 1,2,3...의 문자를 반환하면 되는 줄 알았다. 그러나 행과 열을 바꾸어서 하니 다른 결과가 나와 한참을 생각하다가 검색을 통하여 알았다.
>
> <br>
>
> 풀이 방법은 dp에서 가장 맨아래의 오른쪽인 `[n-1][m-1]`에서부터 시작하여 대각선에서 +1이 된 경우의 문자를 저장하는 것이었다. 만약 대각선에서 + 1이 되었다면 대각선으로 이동하고 그렇지 않다면 바로 위의 값과 왼쪽의 값 중 큰 값이 있는 곳으로 이동을 하여 계속 탐색해나가야 했다. 이는 말보다 코드로 보는 것이 더 잘 이해가 될 것이다.
>
> ![IMG_B9A4CC109F78-1](https://user-images.githubusercontent.com/37801041/78468049-7a3a0a80-774e-11ea-955e-473b1d7a0cd6.jpeg)

<br>

## 코드

```python
# 9252번 LCS 2
import sys

# main
s1 = sys.stdin.readline()
s2 = sys.stdin.readline()

# n(s1) : 세로, m(s2) : 가로
n = len(s1)  # '\n'도 포함되어 있음.
m = len(s2)

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(1,n):
    for j in range(1,m):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

maxLen = dp[n-1][m-1]
print(maxLen)

# 문자열 찾아내기
answer = []
x = m - 1
y = n - 1
while x > 0 and y > 0:
    if dp[y][x-1] == dp[y][x]:
        x -= 1
    elif dp[y-1][x] == dp[y][x]:
        y -= 1
    else:
        answer.append(s1[y-1])
        x -= 1
        y -= 1
    
for c in answer[::-1]:
    print(c, end='')
print()

```

