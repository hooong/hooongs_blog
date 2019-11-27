# [2020 kakao blind_Python3] 4번 가사 검색



#### 문제설명

> 친구들로부터 천재 프로그래머로 불리는 **프로도**는 음악을 하는 친구로부터 자신이 좋아하는 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 궁금하니 프로그램으로 개발해 달라는 제안을 받았습니다.
> 그 제안 사항 중, 키워드는 와일드카드 문자중 하나인 '?'가 포함된 패턴 형태의 문자열을 뜻합니다. 와일드카드 문자인 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정합니다. 예를 들어 `"fro??"`는 `"frodo"`, `"front"`, `"frost"` 등에 매치되지만 `"frame"`, `"frozen"`에는 매치되지 않습니다.
>
> 가사에 사용된 모든 단어들이 담긴 배열 `words`와 찾고자 하는 키워드가 담긴 배열 `queries`가 주어질 때, 각 키워드 별로 매치된 단어가 몇 개인지 **순서대로** 배열에 담아 반환하도록 `solution` 함수를 완성해 주세요.



### 가사 단어 제한사항

- `words`의 길이(가사 단어의 개수)는 2 이상 100,000 이하입니다.
- 각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
- 전체 가사 단어 길이의 합은 2 이상 1,000,000 이하입니다.
- 가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 `words`에는 하나로만 제공됩니다.
- 각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.

### 검색 키워드 제한사항

- `queries`의 길이(검색 키워드 개수)는 2 이상 100,000 이하입니다.
- 각 검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
- 전체 검색 키워드 길이의 합은 2 이상 1,000,000 이하입니다.
- 검색 키워드는 중복될 수도 있습니다.
- 각 검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 `'?'` 로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
- 검색 키워드는 와일드카드 문자인 '?' 가 하나 이상 포함돼 있으며, '?' 는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.
  - 예를 들어 `"??odo"`, `"fro??"`, `"?????"`는 가능한 키워드입니다.
  - 반면에 `"frodo"`(`'?'`가 없음), `"fr?do"`(`'?'`가 중간에 있음), `"?ro??"`(`'?'`가 양쪽에 있음)는 불가능한 키워드입니다.

----

#### 입출력 예

<img width="617" alt="Screen Shot 2019-11-27 at 12 31 47 PM" src="https://user-images.githubusercontent.com/37801041/69691279-ee660100-1111-11ea-9ab0-16a0b1e7e066.png">



### 입출력 예에 대한 설명

- `"fro??"`는 `"frodo"`, `"front"`, `"frost"`에 매치되므로 3입니다.
- `"????o"`는 `"frodo"`, `"kakao"`에 매치되므로 2입니다.
- `"fr???"`는 `"frodo"`, `"front"`, `"frost"`, `"frame"`에 매치되므로 4입니다.
- `"fro???"`는 `"frozen"`에 매치되므로 1입니다.
- `"pro?"`는 매치되는 가사 단어가 없으므로 0 입니다.



## 나의 풀이



#### 접근

> 이 문제는 정확성과 효율성을 따로 채점을 하는 문제였다. 테스트 당시에는 그냥 배열에서 문자열들을 확인하는식으로 정확성만 맞췄었다. 효율성을 맞춰보기 위해 카카오의 문제 풀이를 보니 Trie구조를 사용하면 된다고 쓰여있었다. 이번 계기로 Trie구조를 처음 접해서 검색을 통하여 공부를 하여 이 문제를 풀어보았다. (트라이 구조가 무엇인지 궁금하다면? ["Trie구조 정리"](https://hooongs.tistory.com/28?category=807728)) 또한 이 문제는 '?'가 앞이나 뒤에 (가운데 문자를 두고 앞뒤에는 못오지만) 오기때문에도 생각을 많이 해보았다. 생각 결과 문자열의 길이에 따라 나누고 접두어로만 확인을 하기 위해서 '?'가 앞에 나오는 경우에는 문자열이 뒤집어진 Trie구조를 만들어놓고 찾아야 했다.



#### 풀이 코드

```python
class Node(object):                     # 각 문자들을 저장할 노드
    def __init__(self, key, count=0): 
        self.key = key
        self.count = count              # 해당 문자까지를 접두어로 가지는 문자열의 개수 저장
        self.child = {}

class Trie(object):                     # Trie구조 클래스
    def __init__(self):
        self.head = Node(None)

    def add(self, word):
        cur = self.head

        for ch in word:
            cur.count = cur.count + 1       # 문자열이 저장될때마다 접두어로 가지는 문자열 개수 갱신
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.child['*'] = True

    def search(self, word):
        cur = self.head

        for ch in word:
            if ch == '?':                   # '?'가 나오기 시작 -> 접두어를 가지는 문자열의 개수 반환
                return cur.count
            elif ch not in cur.child:
                return False                # 일치하는 문자열이 0개인 상황
            cur = cur.child[ch]
        if '*' in cur.child:
            return True                     # 일치하는 문자열이 오로지 1개인 상황

def solution(words, queries):
    answer = []
    trie_list = [Trie() for i in range(0,10001)]        # 정상적인 문자열들의 Trie
    rev_trie_list = [Trie() for i in range(0,10001)]    # 뒤집어진 문자열들의 Trie

    for word in words:
        trie_list[len(word)].add(word)
        rev_trie_list[len(word)].add(word[::-1])        # 문자열을 뒤집어서도 Trie를 만들어둔다.
    
    for query in queries:
        if query[0] == '?':         # 문자열이 '?'부터 시작하면 뒤에서부터 검색.
            result = rev_trie_list[len(query)].search(query[::-1])
        else:
            result = trie_list[len(query)].search(query)
        if type(result) == int:     # 타입으로 int형이면 0,1개가 아닌 상황.
            answer.append(result)
        else:                       # Boolean이면 0개 또는 1개.
            if result:
                answer.append(1)
            else:
                answer.append(0)
    return answer
```

- Trie구조를 만들어 놓고 문자열의 길이에 따른 Trie구조를 리스트에 저장을 해놓고 'words'로 들어오는 문자열들을 길이에 따른 Trie에 넣어주고 문자열을 뒤집은 뒤에도 Trie에 넣었다.
- Trie를 구현할 때에는 각 Node에 'count'라는 변수를 두고 문자열이 Trie에 추가될때 그 노드를 거칠때마다 1씩 증가를 시켜주었다. 이렇게 해주면 해당 접두어로 시작하는 단어들의 개수를 저장해 둘 수 있기때문에 'search'에서 '?'가 나오는 경우 해당 Node의 'count'를 반환해주면 된다.



#### 이 문제를 풀면서...

> 문제를 딱 보고 문자열 검사라 아주 쉬운 문제라 생각하고 정확성을 쉽게 맞추고 효율성을 보고나서 좌절을 했던 기억이 난다... 이 문제를 통하여 Trie라는 자료구조를 알게되었고 문자열 검색에서는 빠른 속도를 보장해주기때문에 좋은 구조라는 생각이 들었다. 새로운 구조를 알게되고 또 활용해서 문제를 풀어보니 이해도가 높아졌고 뭔가 한단계 level up을 한 느낌이 들어서 좋았다. 



##### - 본 문제는 프로그래머스에서 풀어보실 수 있습니다.

