# [백준1450번] 냅색문제 / Python3

## 문제

세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.

N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N과 C가 주어진다. N은 30보다 작거나 같은 자연수이고, C는 10^9보다 작거나 같은 음이아닌 정수이고. 둘째 줄에 물건의 무게가 주어진다. 무게도 10^9보다 작거나 같은 자연수이다.

## 출력

첫째 줄에 가방에 넣는 방법의 수를 출력한다.

## 예제 입력 1 

```
2 1
1 1
```

## 예제 출력 1 

```
3
```

<br>

## 나의 풀이

> 이 문제는 `meet in the middle` 알고리즘을 사용하여 풀이를 해야하는 문제였습니다. `meet in the middle`은  적당한 N이 주어질 때 완전탐색을 해야하는 경우 시간복잡도가 `O(2^N)`이 나오는 것을 반으로 쪼개어 시간복잡도를 `O(2^(n/2))`로 만드는 것입니다. 해당 문제를 통해 더 자세히 설명하자면, 우선 N이 최대 30이므로 2의 30승은 대략 10억이라는 숫자이지만 2의 15승은 32,768로 30승과는 아주 큰 차이가 나는 것을 확인해볼 수 있습니다.
>
> 따라서 이 문제의 해결법은 다음과 같습니다. 주어지는 무게 배열을 반으로 나누고 이를 각각 `a_weight`, `b_weight`해봅시다. 나뉘어진 이 두 배열을 완전탐색을 통해 가능한 경우를 모두 구해 각각 `a_sum`, `b_sum`에 저장을 해줍니다. 그 후 `b_sum`을 이분탐색하기 위해서 정렬을 해줍니다. 이후 `a_sum`의 각 원소를 왼쪽부터 방문하며 `c - i`에 해당하는 `b_sum`에서의 `lower_bound`를 구해준 뒤 그 값만큼 answer을 늘려주게 되면 정답을 도출해낼 수 있습니다.

<br>

## 코드

```python
# 1450번 냅색문제

def a_brute_force(l, w):
    if l >= len(a_weight):
        a_sum.append(w)
        return

    a_brute_force(l + 1, w)
    a_brute_force(l + 1, w + a_weight[l])


def b_brute_force(l, w):
    if l >= len(b_weight):
        b_sum.append(w)
        return

    b_brute_force(l + 1, w)
    b_brute_force(l + 1, w + b_weight[l])


def lower_bound(start, end, key):
    global cnt

    while start < end:
        mid = (start + end) // 2

        if b_sum[mid] <= key:
            start = mid + 1
        else:
            end = mid
    return end


n, c = map(int, input().split())
weight = list(map(int, input().split()))
cnt = 0

a_weight = weight[:n // 2]
b_weight = weight[n // 2:]

a_sum = []
b_sum = []
# a, b 완전 탐색
a_brute_force(0, 0)
b_brute_force(0, 0)
b_sum.sort()

for i in a_sum:
    if c - i < 0:			# 이미 a_sum에서 나온 값이 c보다 큰 경우 
        continue
    cnt += (lower_bound(0, len(b_sum), c - i))		# (c - i)값보다 작거나 같으면 가방에 담을 수 있음. 

print(cnt)

```

