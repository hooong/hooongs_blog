#  [2020 kakao blind_Python3] 3번 자물쇠와 열쇠



#### 문제설명

> 고고학자인 **튜브**는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 그런데 문을 열려고 살펴보니 특이한 형태의 **자물쇠**로 잠겨 있었고 문 앞에는 특이한 형태의 **열쇠**와 함께 자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.
>
> 잠겨있는 자물쇠는 격자 한 칸의 크기가 **`1 x 1`**인 **`N x N`** 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 **`M x M`** 크기인 정사각 격자 형태로 되어 있습니다.
>
> 자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.
>
> 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.



#### 제한사항

- key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
- lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
- M은 항상 N 이하입니다.
- key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
  - 0은 홈 부분, 1은 돌기 부분을 나타냅니다.

------

####  입출력 예

<img width="492" alt="Screen Shot 2019-10-29 at 12 02 30 AM" src="https://user-images.githubusercontent.com/37801041/67690010-87a0db00-f9df-11e9-9332-7d5c2af4d763.png">



#### 입출력 예에 대한 설명

<img width="627" alt="Screen Shot 2019-10-29 at 12 04 20 AM" src="https://user-images.githubusercontent.com/37801041/67690104-ad2de480-f9df-11e9-892e-cdad90f7af3b.png">

key를 시계 방향으로 90도 회전하고, 오른쪽으로 한 칸, 아래로 한 칸 이동하면 lock의 홈 부분을 정확히 모두 채울 수 있습니다.

----



## 나의 풀이



#### 접근

> 나는 이 문제는 카카오 테크 블로그에서 힌트를 얻고 풀어보았다. 힌트의 내용은 lock보다 가로,세로로 3배씩 큰 2차원배열을 만들고 key배열을 오른쪽과 아래로 움직이면서 90도씩 회전을 시키며 모든 경우의 수를 확이해보는 것이었다. 이것이 가능한 이유는 제한사항에 n과 m이 3이상 20이하로 아주 작은 값이기 때문이다. 
>
>  따라서 나는 회전을 시키는 함수, 키와 맞아떨어지는지 확이하는 함수를 만들고 이것들을 활용하면서 모든 경우의 수를 확인해보았다.



- Rotate_90 function

  <img width="500" src="https://user-images.githubusercontent.com/37801041/67691642-4958eb00-f9e2-11e9-9cd6-dbecf2ae86eb.jpg">

  위의 그림에서 보듯이 2차원 배열을 90도 회전시키려 할때 첫번째 행을 보면 회전 전의 *열* 과 회전 후의 *행* 의 index가 같은 것을 확인할 수 있다. 이 성질을 사용하면 2차원 배열을 90도 회전시키는 함수는 쉽게 구현할 수 있다.

  

- 어떠한 경우들을 모두 검사해야하는가?

  <img width="500" src="https://user-images.githubusercontent.com/37801041/67691441-f54e0680-f9e1-11e9-86d0-3c91d506ccdb.jpg">

  위의 그림은 n은 4, m은 3일때의 경우를 그려보았는데 이것을 본보기로 삼아서 값들을 n과 m으로 일반화를 시켜보니 확인을 할때 처음으로 하나라도 겹치는 부분이 생기는 시작점은 `n-m+1` 이라는 값이었다. 따라서 나는 두 개의 포문을 사용하여 key와 lock가 하나이상 겹치는 모든 부분을 확인할 수 있었다.



#### 풀이 코드

```python
def rotate_90(key,m):         # 2차원 배열 90도 회전함수
    rot_key = [[0] * m for _ in range(m)]

    for c in range(m):
        for r in range(m):
            rot_key[r][m-1-c] = key[c][r]
    return rot_key

def confirm(try_key,n):         # 키가 맞는지 확인하는 함수
    for c in range(n,2*n):
        for r in range(n,2*n):
            if try_key[c][r] == 1:      # lock부분이 모두 1인지 확인
                pass
            else:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    ex_lock = [[0] * (3*n) for _ in range(3*n)]     # 3배로 확장된 lock 생성
    for c in range(n,2*n):
        for r in range(n,2*n):
            ex_lock[c][r] = lock[c-n][r-n]
    
    for x in range(n-m+1,2*n):                      # 가로로 n-m+1부터 2n까지 반복
        for y in range(n-m+1,2*n):                  # 세로도 마찬가지로 반복
            for _ in range(4):                      # 90도씩 회전하면서 반복
                ex_key = [[0] * (3*n) for _ in range(3*n)]      # 확장된 lock과 더하여 비교하기 위해 key도 확장
                for c in range(x,x+m):
                    for r in range(y,y+m):
                        ex_key[c][r] = key[c-x][r-y]
                
                try_key = [[0] * (3*n) for _ in range(3*n)]
                for c in range(3*n):
                    for r in range(3*n):
                        try_key[c][r] = ex_lock[c][r] + ex_key[c][r]    # 돌기와 맞물리는지 확인하기 위해 더함

                if confirm(try_key,n):
                    return True
                else:
                    key = rotate_90(key,m)
    
    return False
```



#### 이 문제를 풀면서...

> 처음에 코딩테스트를 할 때 이 문제를 읽고나서 아주 어려운 문제 같아서 그냥 건너뛰고 마지막에 조금 생각해보다가 시간이 부족했던 기억이 난다. 이제와서 카카오 기술블로그의 힌트를 보니 뭔가 쉽게 풀 수 있을 것 같은 기분이 들었다. 그래서 생각을 해보고 짜보았는데 음... 짜고나서 보니 복잡도가 너무 크다는걸 느꼈다... 그래도 n의 값이 작아서 망정이지 아마도 컸다면 난 이 문제를 풀지 못했을 것 같다... 프로그래머스에서 이 문제를 풀고나서 다른 사람들의 풀이들을 봤는데 역시 실력자들은 많았다.. 시간이 충분할때 남이 짠 코드를 분석해보고 다시 한번 이 문제에 도전해서 더욱 짧고 효율적인 코드를 짜봐야겠다...

