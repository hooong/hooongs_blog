# [백준1024번] 수열의 합 / Python3

## 문제

N과 L이 주어질 때, 합이 N이면서, 길이가 적어도 L인 가장 짧은 연속된 음이 아닌 정수 리스트를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N과 L이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이고, L은 2보다 크거나 같고, 100보다 작거나 같은 자연수이다.

## 출력

만약 리스트의 길이가 100보다 작거나 같으면, 연속된 수를 첫째 줄에 공백으로 구분하여 출력한다. 만약 길이가 100보다 크거나 그러한 수열이 없을 때는 -1을 출력한다.

## 예제 입력 1

```
18 2
```

## 예제 출력 1

```
5 6 7
```

<br>

## 나의 풀이

> 처음에 투 포인터 기법으로 접근해보았지만 알고보니 수학문제 였던 문제입니다.
>
> 연속된 L개의 숫자들로 더해진 합은 다음과 같은 수식으로 나타낼 수 있습니다.
>
> `N = (x+1) + (x+2) + (x+3) + ... + (x+L)`  
>
> 이 식을 정리하면, `N = Lx + L(L+1) / 2`가 되는데 여기서 식을 `Lx`에대하여 정리하면 다음과 같은 결과를 얻을 수 있습니다. 
>
> `Lx = N - L * (L+1) / 2 ` 
>
> 이 식에서 보면 `L`로 `N - L * (L+1) / 2`를 나누었을 때, 나누어 떨어진다면 `x`가 곧 정수가 되기때문에 문제에서 말하는 정수 리스트를 구할 수 있는 여지가 생기게 됩니다. 그러나 여기서 한번더 문제를 읽어보게되면 `음이 아닌 정수 리스트`라는 것을 볼 수 있습니다. 즉, N을 구할 때, 가장 처음 숫자가 되는  `(x+1)`이 0보다 크거나 같아야되기때문에 이러한 조건도 따져주는 코드를 구현해야합니다.
>
> 이렇게 `x`를 구하는 방법을 알았다면 이제 주어지는 `L`부터 `100`까지 확인해보면서 x를 구한다면 답을 출력하고 100까지 확인해봐도 만족하는 x를 구하지 못한다면 -1을 출력하면 됩니다.

<br>

## 코드

```python
# 1024번 수열의 합

N, L = map(int, input().split())

for i in range(L, 101):
    x = N - (i * (i + 1) / 2)

    if x % i == 0:
        x = int(x / i)

        if x >= -1:
            for j in range(1, i + 1):
                print(x + j, end=' ')
            print()
            break
else:
    print(-1)

```

