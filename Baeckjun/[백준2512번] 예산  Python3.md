# [백준2512번] 예산 / Python3

## 문제

국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것이다. 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다. 그래서 정해진 총액 이하에서 **가능한 한 최대의** 총 예산을 다음과 같은 방법으로 배정한다.

1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
2. 모든 요청이 배정될 수 없는 경우에는 특정한 **정수** 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 

예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다. 

여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.

## 입력

첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다. 다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다. 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다. 

## 출력

첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다. 

## 예제 입력 1

```
4
120 110 140 150
485
```

## 예제 출력 1

```
127
```

<br>

## 나의 풀이

> 해당 문제는 파라메트릭 서치를 이용하여 푸는 문제였다. 즉, 상한액을 결정하는 문제로 생각하여 이분탐색을 진행하는 것이다. 
>
> 여기서 상한액은 `0부터 전체 국가예산`까지 될 수 있다. 따라서 이분탐색을 위한 l과 r은 각각 0, 전체 국가예산으로 초기화를 하고 이분탐색을 시작하면 된다. 각 이분탐색의 과정에서는 모든 예산을 더해주어 전체 국가예산보다 큰지 작은지를 판단하고 작다면 그때의 상한값을 최댓값으로 저장을하고 mid의 오른쪽 부분을 다시 탐색하면된다. 이렇게 l이 r보다 클때까지 반복을하고 모두 마친다면 최대 상한액을 찾을 수 있다. 
>
> 그리고 문제에서 출력으로 원하는 것은 배정된 예산들 중 최댓값을 출력하는 것이다. 따라서 주어진 예산액 중 최댓값과 파라메트릭 서치를 통해 찾은 상한액과 비교하여 최댓값이 상한액보다 작다면 최댓값을 그대로, 그렇지 않다면 상한액을 출력하면 문제를 해결할 수 있다.

<br>

## 코드

```python
# 2512번 예산

n = int(input())
budgets = list(map(int, input().split()))
total = int(input())

max_limit = 0
l = 0
r = total
while l <= r:
    mid = (l + r) // 2

    sub_total = 0
    for budget in budgets:
        if budget > mid:
            sub_total += mid
        else:
            sub_total += budget

    if sub_total > total:
        r = mid - 1
    else:
        max_limit = max(max_limit, mid)
        l = mid + 1

max_budget = max(budgets)
if max_budget > max_limit:
    print(max_limit)
else:
    print(max_budget)

```

