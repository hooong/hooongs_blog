# [프로그래머스] 완주하지 못한 선수 - Python3

## 나의 풀이

>  해당 문제는 participant의 최대가 100,000으로 O(n^2)이상의 시간 복잡도가 나오면 안되는 문제이다. 
>
> 필자는 딕셔너리를 이용하여 풀이를 하였다. 우선, participant의 모든 선수들을 반복하며 {이름: 개수} 형태로 저장하고 각 선수의 숫자를 세어준다. 이후 completion을 반복하며 해당하는 이름의 숫자를 1씩 감소를 시킨다. 그리고 마지막으로 딕셔너리를 반복하며 value가 0이 아니라면 return을 해주면 문제를 해결할 수 있다.
>
> 허나 `다른 사람의 풀이`를 보니 유용한 모듈이 있어 글을 쓰게 되었다. `collections`에 보면 `Counter`라는 오브젝트가 있다. 이 오브젝트는 리스트에 있는 요소들의 개수를 자동으로 딕셔너리 형태로 갖는다. 예를 들면, `['a', 'a', 'b']`인 `list`라는 리스트가 있다면 `Counter(list)`를 하면 `{'a':2, 'b':1}`이라는 오브젝트가 생긴다는 것이다. 여기에 더욱 막강한 것은 각기 Counter끼리 `-`연산이 가능하다는 것이다. 따라서, 이 `Counter`을 사용하면 해당 문제를 단 한줄에 풀어낼 수 있었다...

<br>

## 코드

1. 처음 딕셔너리를 사용한 풀이

   ```python
   def solution(participant, completion):
       p_dic = dict()
       
       for p in participant:
           if not p in p_dic.keys():
               p_dic[p] = 1
           else:
               p_dic[p] += 1
       
       for c in completion:
           p_dic[c] -= 1
           
       for p in p_dic:
           if not p_dic[p] == 0:
               return p
   ```

2. Counter를 사용한 풀이

   ```python
   from collections import Counter
   
   def solution(participant, completion):
       return list((Counter(participant) - Counter(completion)).keys())[0]
   ```

   

