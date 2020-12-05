# [백준4195번] 친구 네트워크 / Python3

## 문제

민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

## 입력

첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

## 출력

친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

## 예제 입력 1

```
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
```

## 예제 출력 1

```
2
3
4
2
2
4
```

<br>

## 나의 풀이

> 친구 관계를 나타내는 딕셔너리와 각각의 친구 네트워크의 크기를 저장하는 딕셔너리를 만들어주고 Union-Find를 이용해 친구가 추가될 때마다 친구관계를 업데이트함과 동시에 root에 있어서 친구 네트워크에 몇명이 있는지를 업데이트해주면서 출력해준다. Union-Find를 이해한 상태라면 아래 코드를 보면 한눈에 이해를 할 수 있을 것이다. 
>
> 이 문제는 일반 유니온 파인드에서 추가되는 크기를 다루면 되는 문제였던 것 같다. 예를들어, x라는 친구와, y라는 친구가 서로 친구가 아닌 상태에서 서로 친구를 맺게 된다면, x가 가진 친구의 수와 y가 가진 친구의 수를 더하는 것이 곧 그 둘의 친구 관계의 수가 된다.

<br>

## 코드

```python
# 4195번 친구 네트워크
import sys


def set_index(f):
    global network, size

    if not f in network:
        network[f] = f
        size[f] = 1

    return network[f]


def find(x):
    global network

    if network[x] == x:
        return x

    network[x] = find(network[x])
    return network[x]


def union(x, y):
    global network

    x = find(x)
    y = find(y)

    if not x == y:
        if size[x] < size[y]:
            x, y = y, x

        network[y] = x
        size[x] += size[y]

    print(size[x])


for _ in range(int(sys.stdin.readline())):
    f = int(sys.stdin.readline())
    network, size = {}, {}

    for _ in range(f):
        f1, f2 = sys.stdin.readline().split()
        f1 = set_index(f1)
        f2 = set_index(f2)

        union(f1, f2)

```

