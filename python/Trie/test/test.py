class Node(object):
    def __init__(self, key, count=0): 
        self.key = key
        self.count = count
        self.child = {}

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

trie = Trie()
trie.insert('hooong')
trie.insert('hi')
trie.insert('how')
print(trie.search('hooong'))
print(trie.search('hi'))
print(trie.search('home'))