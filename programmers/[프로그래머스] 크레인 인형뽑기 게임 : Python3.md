# [프로그래머스] 크레인 인형뽑기 게임 / Python3

 해당 문제는 2019 카카오 개발자 겨울 인턴십에서 1번으로 나왔던 문제이다.

## 나의 풀이

> 필자는 board가 2차원 배열로 주어진 것을 collum별로 스택에 나누어 담아 놓고 크레인이 움직일 때 2차원 배열을 반복하며 찾는 과정을 없애는 방향으로 풀이를 진행하였다. 따라서 초기에 N개 만큼의 deque()를 담는 list를 만들어두고 board의 모든 행을 거꾸로 탐색하여 해당 deque()에 `0이 아니라면` append를 해놓았다. 또한, bucket이라는 deque()도 생성해두었다.
>
> 이후, 주어지는 moves를 반복하며 해당하는 deque()가 비어있지 않다면 pop을 하였다. 그리고나서 bucket이 비어있지 않다면 가장 위에 있는 인형과 같은지를 비교하고 같다면 bucket에서 pop을 진행하고 asnwer에 2만큼을 더해주었고, 반대로 같지 않다면 bucket에 크레인이 집고 있는 인형을 append해주었다. 이렇게 모든 moves를 반복하고 나면 정답이 나온다.

<br>

## 코드

```python
from collections import deque

def solution(board, moves):
    answer = 0
    board_stack = [deque() for _ in range(len(board))]
    bucket = deque()
    
    for row in board[::-1]:
        for i in range(len(row)):
            if not row[i] == 0:
                board_stack[i].append(row[i])
    
    for num in moves:
        if board_stack[num-1]:
            doll = board_stack[num-1].pop()
        
            if bucket:
                if doll == bucket[-1]:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(doll)
            else:
                bucket.append(doll)
    
    return answer
```



