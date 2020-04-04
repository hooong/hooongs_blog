# [백준2096번] 내려가기 / Python3

## 문제

N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.

먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다. 바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다. 이 제약 조건을 그림으로 나타내어 보면 다음과 같다.

![img](https://www.acmicpc.net/JudgeOnline/upload/201007/down.png)

별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며, 빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다. 숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오. 점수는 원룡이가 위치한 곳의 수의 합이다.

## 입력

첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다. 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.

## 출력

첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.

## 예제 입력 1

```
3
1 2 3
4 5 6
4 9 0
```

## 예제 출력 1 

```
18 6
```

<br>

## 나의 풀이

>아주 쉽게 풀 수 있는 문제라고 생각하고 다들 풀 것이다. 물론 그렇게 풀면 아주 쉽다. 그러나 메모리가 4MB한정이다. 쉽게푸는 방법은 dp를 주어지는 N에 따라 `N*3` 만큼 최댓값과 최솟값을 저장하는 배열 두 개를 만들면 아주 쉽게 풀 수 있다. 하지만 이렇게 풀면 당연히 메모리초과가 발생하게 된다.
>
><br>
>
>따라서 이 문제를 푸는 방법은 dp를 최소 한 줄씩 유지해나가는 것이다. 한 줄 입력받을 때마다 각 줄에서의 최댓값과 최솟값을 구해나가는 것이다. 첫 줄은 그대로 복사를 해준다. 그리고 두 번째 줄부터는 입력받은 줄과 dp를 가지고 최댓값 및 최솟값을 구하면 된다. 그런데 주의할 점은 바로 전 단계에서 끝난 dp를 tmp로 복사를 해서 가지고 있어야한다는 것이다. 이걸 가지고 있지않으면 그때그때 dp가 바뀌면 그 바뀐 값을 가지고 최댓값이나 최솟값을 구하게 되어 원하는 결과가 나오지 않을 것이다. 이 점만 주의하고 푼다면 쉽게 풀 수 있는 문제일 것이다.

<br>

## 코드

```python
# 2096번 내려가기
import sys, copy

# main
N = int(input())

for n in range(N):
    line = [int(x) for x in sys.stdin.readline().split()]

    if n == 0:
        dpMax = copy.deepcopy(line)
        dpMin = copy.deepcopy(line)
    else:
        tmpMax = copy.deepcopy(dpMax)
        tmpMin = copy.deepcopy(dpMin)
        
        # 최댓값, 최솟값
        for i in range(3):
            if i == 0:
                dpMax[i] = line[i] + max(tmpMax[i], tmpMax[i+1])
                dpMin[i] = line[i] + min(tmpMin[i], tmpMin[i+1]) 
            elif i == 1:
                dpMax[i] = line[i] + max(tmpMax[i-1], max(tmpMax[i], tmpMax[i+1]))
                dpMin[i] = line[i] + min(tmpMin[i-1], min(tmpMin[i], tmpMin[i+1]))
            elif i == 2:
                dpMax[i] = line[i] + max(tmpMax[i-1], tmpMax[i])
                dpMin[i] = line[i] + min(tmpMin[i-1], tmpMin[i])

print(max(dpMax), min(dpMin))

```

####  