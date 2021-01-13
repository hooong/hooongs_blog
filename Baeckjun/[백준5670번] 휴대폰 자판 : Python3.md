# [백준5670번] 휴대폰 자판 / Python3

## 문제

휴대폰에서 길이가 P인 영단어를 입력하려면 버튼을 P번 눌러야 한다. 그러나 시스템프로그래밍 연구실에 근무하는 승혁연구원은 사전을 사용해 이 입력을 더 빨리 할 수 있는 자판 모듈을 개발하였다. 이 모듈은 사전 내에서 가능한 다음 글자가 하나뿐이라면 그 글자를 버튼 입력 없이 자동으로 입력해 준다! 자세한 작동 과정을 설명하자면 다음과 같다.

1. 모듈이 단어의 첫 번째 글자를 추론하지는 않는다. 즉, 사전의 모든 단어가 같은 알파벳으로 시작하더라도 반드시 첫 글자는 사용자가 버튼을 눌러 입력해야 한다.
2. 길이가 1 이상인 문자열 c1c2...cn이 지금까지 입력되었을 때, 사전 안의 모든 c1c2...cn으로 시작하는 단어가 c1c2...cnc로도 시작하는 글자 c가 존재한다면 모듈은 사용자의 버튼 입력 없이도 자동으로 c를 입력해 준다. 그렇지 않다면 사용자의 입력을 기다린다.

예를 들면, 사전에 "hello", "hell", "heaven", "goodbye" 4개의 단어가 있고 사용자가 "h"를 입력하면 모듈은 자동으로 "e"를 입력해 준다. 사전상의 "h"로 시작하는 단어들은 모두 그 뒤에 "e"가 오기 때문이다. 그러나 단어들 중 "hel"로 시작하는 것도, "hea"로 시작하는 것도 있기 때문에 여기서 모듈은 사용자의 입력을 기다린다. 이어서 사용자가 "l"을 입력하면 모듈은 "l"을 자동으로 입력해 준다. 그러나 여기서 끝나는 단어인 "hell"과 그렇지 않은 단어인 "hello"가 공존하므로 모듈은 다시 입력을 기다린다. 사용자가 "hell"을 입력하기 원한다면 여기서 입력을 멈출 것이고, "hello"를 입력하기 원한다면 직접 "o" 버튼을 눌러서 입력해 줘야 한다. 따라서 "hello"를 입력하려면 사용자는 총 3번 버튼을 눌러야 하고, "hell", "heaven"은 2번이다. "heaven"의 경우 "he"에서 "a"를 입력하면 바로 뒷부분이 모두 자동으로 입력되기 때문이다. 비슷하게, "goodbye"는 단 한 번만 버튼을 눌러도 입력이 완료될 것이다. "g"를 입력하는 순간 뒤에 오는 글자가 항상 유일하므로 끝까지 자동으로 입력되기 때문이다. 이때 사전에 있는 단어들을 입력하기 위해 버튼을 눌러야 하는 횟수의 평균은 (3 + 2 + 2 + 1)/4 = 2.00이다.

사전이 주어졌을 때, 이 모듈을 사용하면서 이와 같이 각 단어를 입력하기 위해 버튼을 눌러야 하는 횟수의 평균을 구하는 프로그램을 작성하시오.

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스의 첫째 줄에 사전에 속한 단어의 개수 N이 주어지며(1 ≤ N ≤ 105), 이어서 N개의 줄에 1~80글자인 영어 소문자로만 이루어진 단어가 하나씩 주어진다. 이 단어들로 사전이 구성되어 있으며, 똑같은 단어는 두 번 주어지지 않는다. 각 테스트 케이스마다 입력으로 주어지는 단어의 길이 총합은 최대 106이다.

## 출력

각 테스트 케이스마다 한 줄에 걸쳐 문제의 정답을 소수점 둘째 자리까지 반올림하여 출력한다.

## 예제 입력 1

```
4
hello
hell
heaven
goodbye
3
hi
he
h
7
structure
structures
ride
riders
stress
solstice
ridiculous
```

## 예제 출력 1

```
2.00
1.67
2.71
```

<br>

## 나의 풀이

> 해당 문제는 트라이 구조를 이용해 풀 수 있는 문제입니다.
>
> 우선, 문자열을 담는 노드에 count라는 변수를 추가해 몇개의 문자열이 해당 문자를 사용하는지를 카운트하였습니다. 예를들면 다음과 같습니다.
>
> ![IMG_EE56CA6FFE12-1](https://user-images.githubusercontent.com/37801041/103027596-847c8d00-4599-11eb-8c03-89d3dbdc610b.jpeg)
>
> 설명을 더하자면, 만약 'hell'이 이미 insert된 상황에서 'hello'가 insert된다면 'h', 'e', 'l', 'l'을 방문하게 되는데 이때마다 해당 노드의 count를 증가시켜준다면 위와 같은 결과를 얻어낼 수 있습니다.
>
> ![IMG_84AA1F9DA323-1](https://user-images.githubusercontent.com/37801041/103028321-dd005a00-459a-11eb-8548-c80f40a75825.jpeg)
>
> 이렇게 트라이 구조를 완성했다면 이제 휴대폰 자판의 입력 수를 알아내야합니다. 잘 생각을 해보면 자판을 입력해야 되는 문자에대한 조건은 다음과 같습니다.
>
> 1. 첫번째 문자이다.
> 2. 다음 상위 문자에서 child의 개수가 1보다 크다.
>
> 즉, 위의 예에서는 'h', 'a', 'l', 'g'의 count값들만 더해주면 되는 것입니다. 이걸 코드로 구현하기 위해서는 dfs를 활용해서 모든 노드를 탐색하며 위의 조건이 만족할 경우 count를 더해주면 됩니다.

<br>

## 코드

```python
# 5670번 휴대폰 자판
from sys import stdin


class Node:
    def __init__(self, key, count=0):
        self.key = key
        self.child = {}
        self.count = count


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
            cur.count += 1
        cur.child['*'] = True


def find_click(l, cur):
    global cnt

    if len(cur.child) > 1 or l == 0:
        for c in cur.child:
            if c != '*':
                cnt += cur.child[c].count

    for c in cur.child:
        if c != '*':
            find_click(l+1, cur.child[c])


try:
    while True:
        n = int(stdin.readline())
        trie = Trie()
        cnt = 0

        for _ in range(n):
            trie.insert(stdin.readline().strip('\n'))

        find_click(0, trie.head)
        print("{:,.2f}".format(round((cnt / n), 2)))
except:
    exit(0)

```



