# [2020 kakao blind_Python3] 5번 기둥과 보 설치



#### 문제보기

- [문제 풀러가기](https://programmers.co.kr/learn/courses/30/lessons/60061)



## 나의 풀이



#### 접근

> 시뮬레이션 문제로서 문제에서 제시하는 조건에 따라 기둥이나 보를 설치 및 삭제를 하면 되는 문제였다. 처음에는 조건들이 살짝 까다로워 보이지만 특정 좌표가 기둥이 있는지 또는 보가 있는지 확인하는 함수와 각 기둥과 보가 조건에 위배되지는 않는지 확인해주는 함수를 만들어 쉽게 풀 수 있었다.



#### 풀이 코드

```python
# 기둥 설치
def add_col(wall,x,y):
    
    if y==0:                # 바닥일 경우
        wall[y][x][0] = 1
    else:                   # 바닥이 아닐 경우
        if (iscol(wall,x,y-1)) or (isbeam(wall,x,y)) or (isbeam(wall,x-1,y)):
            wall[y][x][0] = 1
    return wall

# 기둥 삭제
def remove_col(wall,x,y):
    
    if wall[y][x][0] == 1:
        wall[y][x][0] = 0
        confirm = True
        if iscol(wall,x,y+1):                   # 바로 위에 기둥이 있는 경우
            if not confirm_col(wall,x,y+1): 
                confirm = False             
        if isbeam(wall,x-1,y+1):                # 기둥 왼쪽으로 보가 있는 경우
            if not confirm_beam(wall,x-1,y+1):
                confirm = False
        if isbeam(wall,x,y+1):                  # 기둥 오른쪽으로 보가 있는 경우
            if not confirm_beam(wall,x,y+1):
                confirm = False
        
        if not confirm:
            wall[y][x][0] = 1
    else:
        pass

    return wall

# 보 설치
def add_beam(wall,x,y):

    if iscol(wall,x,y-1) or iscol(wall,x+1,y-1) or (isbeam(wall,x-1,y) and isbeam(wall,x+1,y)):
        wall[y][x][1] = 1
            
    return wall

# 보 삭제
def remove_beam(wall,x,y):
    
    if wall[y][x][1] == 1:
        wall[y][x][1] = 0
        confirm = True
        if iscol(wall,x,y):                     # 보 시작점에 기둥이 있는 경우
            if not confirm_col(wall,x,y):
                confirm = False
        if iscol(wall,x+1,y):                   # 보의 오른쪽 끝에 기둥이 있는 경우
            if not confirm_col(wall,x+1,y):
                confirm = False
        if isbeam(wall,x-1,y):                  # 보의 왼쪽에 보가 있는 경우
            if not confirm_beam(wall,x-1,y):
                confirm = False
        if isbeam(wall,x+1,y):                  # 보의 오른쪽에 보가 있는 경우
            if not confirm_beam(wall,x+1,y):
                confirm = False
        
        if not confirm:
            wall[y][x][1] = 1
    else:
        pass

    return wall

# 기둥이 있는지 확인
def iscol(wall,x,y):
    if x < 0 or y < 0 or x > len(wall) or y > len(wall):
        return False
    else:
        if wall[y][x][0] == 1:
            return True
        else:
            return False

# 보가 있는지 확인
def isbeam(wall,x,y):
    if x < 0 or y < 0 or x > len(wall) or y > len(wall):
        return False
    else:
        if wall[y][x][1] == 1:
                return True
        else:
            return False

# 기둥이 유효한가 확인
def confirm_col(wall,x,y):
    
    # 바닥일 경우는 항상 유효
    if y == 0:
        return True
    # 왼쪽 또는 오른쪽으로 보가 있거나, 바로 아래 기둥이 있는 경우가 유효
    else:
        if isbeam(wall,x-1,y) or isbeam(wall,x,y) or iscol(wall,x,y-1):
            return True
        else:
            return False

# 보가 유효한지 확인
def confirm_beam(wall,x,y):

    # 양 끝에 한 곳에라도 기둥이 있거나, 보의 왼쪽, 오른쪽 모두 보가 있는 경우가 유효
    if iscol(wall,x,y-1) or iscol(wall,x+1,y-1) or (isbeam(wall,x-1,y) and isbeam(wall,x+1,y)):
        return True
    else:
        return False

def solution(n, build_frame):
    answer = []
    wall = [[[0,0] for _ in range(n+1)] for _ in range(n+1)]    # n * n 벽면 생성

    # 기둥,보 추가 및 삭제
    for frame in build_frame:
        x = frame[0]
        y = frame[1]
        if frame[2] == 0:       # 기둥
            if frame[3] == 0:   # 삭제
                wall = remove_col(wall,x,y)
            else:               # 추가
                wall = add_col(wall,x,y)
        else:                   # 보
            if frame[3] == 0:   # 삭제
                wall = remove_beam(wall,x,y)
            else:
                wall = add_beam(wall,x,y)
    
    # 현재 벽면 상태 answer로 옮기기
    for x in range(n+1):
        for y in range(n+1):
            if wall[y][x][0] == 1:
                answer.append([x,y,0])
            if wall[y][x][1] == 1:
                answer.append([x,y,1])

    return answer
```

- 그림을 그려가며 기둥 및 보의 경우의 수를 모두 따져보고 확인해야 되는 위치에서만 확인을 해준다면 쉽게 풀 수 있다.

- 주석을 보면 쉽게 이해가 갈 것입니다.



### 이 문제를 풀면서...

> 조건이 많고 복잡해서 어려운 문제인줄만 알고있었다. 허나 그림을 그려보고 경우의 수를 따져가며 하나하나 정리를 해가면서 푸니 쉽게 풀려버렸다. 뭔가 복잡해보일수록 단순하게 접근하는 것이 좋겠다는 생각이 들었고, 함수로 기능들을 나눠가며 푸는 것도 좋다는 것을 알 수 있었다. ( 근데 wall이라는 2차원 list를 계속 매개변수로 넘겨주는 것이 좋은지는 잘 모르겠지만... )