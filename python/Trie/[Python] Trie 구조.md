# [Python] Trie 구조



### Trie란?

```
원래 Trie는 탐색을 뜻하는 retrieval에서 중간 글자인 trie에서 유래가 되었다고합니다. 
Tree의 일종으로 Prefix tree라고 부르는 사람도 있다고한다. Prefix로 보면 좀 더 직관적으로 이해가 가능하다.
예를들면, IP주소를 routing table에 저장할때에도 앞에 오는 bit들부터 정해놓고 routing을 해주는 것과 비슷하다고 볼 수 있다.
```



아래 그림을 보면 Trie구조를 좀 더 쉽게 이해를 할 수 있다. *(아래 그림에서 '*'은 문자열의 끝을 나타낸 것이다.)*

<img width="468" alt="Screen Shot 2019-11-26 at 11 27 58 AM" src="https://user-images.githubusercontent.com/37801041/69594505-e178dd00-103f-11ea-88a8-a094c66d712d.png">

### Trie구조를 왜? 사용할까

Trie구조는 우선 **탐색의 속도가 빠르다**는 것입니다. 문자열의 길이를 m이라할때, 탐색의 시간복잡도를 계산해보면 **O(m)**이 되므로 탐색에서는 아주 빠르다는 것을 알 수 있다. 물론 각 노드에 자식들을 모두 저장*(python으로 구현하면 딕셔너리를 모두 저장)*하기때문에 사용하는 공간의 크기가 크다는 단점이 있기는 합니다. 또한 Trie구조를 사용하면 앞에서 **Prefix Tree**라고 불린다고 했던 그 점이 장점이 될 수도 있다. 어떠한 문자열의 접두어를 통해 해당하는 문자열을 찾을 때 유용할 수 있기때문이다.



### Python으로 Trie 구현하기

우선 각 문자들을 저장하기 위한 노드를 만들어준다.

```python
class Node(object):
    def __init__(self, key, count=0): 
        self.key = key								# 해당 문자를 key값으로 가진다.
        self.child = {}								# 자식들을 Dict에 저장을 한다.
```

그리고나서 Trie class를 만들어준다.

```python
class Trie(object):
    def __init__(self):
        self.head = Node(None)			# 처음 Trie가 만들어지면 빈 Node 하나를 head로 만들어 놓는다.

    def insert(self, word):			
        cur = self.head

        for ch in word:								# 문자열의 각 문자들을 반복
            if ch not in cur.child:		# 해당 문자가 자식노드에 존재하지 않을 경우 노드를 추가
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.child['*'] = True					# 문자열의 마지막에 '*'을 삽입.

    def search(self, word):
        cur = self.head

        for ch in word:								# 문자열의 각 문자들을 반복
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        if '*' in cur.child:
            return True
```

- `insert(word)` : 새로운 문자열을 Trie에 추가하는 코드
- `search(word)` : Trie에서 word로 들어오는 문자열을 탐색하고 있으면 `True`, 없으면 `False` 를 반환.

#### Test

````python
# test code
trie = Trie()
trie.insert('hooong')
trie.insert('hi')
trie.insert('how')
print(trie.search('hooong'))
print(trie.search('hi'))
print(trie.search('home'))

# 출력결과
True
True
False
````

- *test에서의 Trie구조 그림.*

<img width="352" alt="Screen Shot 2019-11-26 at 11 56 09 AM" src="https://user-images.githubusercontent.com/37801041/69595745-c27c4a00-1043-11ea-8f9d-04d242869ff2.png">



#### 이렇게 Trie구조 설명을 마치겠습니다. 감사합니다.

