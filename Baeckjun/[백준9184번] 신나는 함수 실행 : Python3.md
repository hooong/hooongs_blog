# [백준9184번] 신나는 함수 실행 / Python3

## 문제

재귀 호출만 생각하면 신이 난다! 아닌가요?

다음과 같은 재귀함수 w(a, b, c)가 있다.

```
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
```

위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)

a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.

## 입력

입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다. 입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

## 출력

입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.

## 제한

- -50 ≤ a, b, c ≤ 50

## 예제 입력 1

```
1 1 1
2 2 2
10 4 6
50 50 50
-1 7 18
-1 -1 -1
```

## 예제 출력 1

```
w(1, 1, 1) = 2
w(2, 2, 2) = 4
w(10, 4, 6) = 523
w(50, 50, 50) = 1048576
w(-1, 7, 18) = 1
```

<br>

## 나의 풀이

> 필자는 해당 문제를 메모제이션 기법을 사용해 풀었습니다. 
>
> `mem`이라는 딕셔너리를 하나 만들어두고 문제에서 주어지는 재귀 함수를 정의하면서 매개변수로 들어오는 `(a, b, c)`라는 튜플이 mem에서 키로 존재한다면 바로 그것을 반환해주며 그렇지 않으면 함수를 실행하면서 `mem[(a, b, c)]`에 값을 저장해두고 그 값을 리턴해주는 방식으로 메모제이션을 구현하였습니다.

<br>

## 코드

```python
# 9184번 신나는 함수 실행
import sys


def w(a, b, c):
    global mem

    if (a, b, c) in mem.keys():
        return mem[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        mem[(20, 20, 20)] = w(20, 20, 20)
        return mem[(20, 20, 20)]

    elif a < b < c:
        mem[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return mem[(a, b, c)]

    else:
        mem[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return mem[(a, b, c)]


while True:
    x, y, z = map(int, sys.stdin.readline().split())

    if x == -1 and y == -1 and z == -1:
        break

    mem = dict()
    print('w({}, {}, {}) = {}'.format(x, y, z, w(x, y, z)))

```

