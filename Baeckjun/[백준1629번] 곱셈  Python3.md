# [백준1629번] 곱셈 / Python3

## 문제

자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

## 출력

첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

## 예제 입력 1

```
10 11 12
```

## 예제 출력 1

```
4
```

<br>

## 나의 풀이

> A를 B번 곱하는 것을 분할정복으로 푸는 문제로 `B에 대하여 2개로 분할을 해가면서 곱셈을 줄여나갈 있다.` 아래 그림을 보듯이 원래는 10번을 곱해야 되는 것이 6번의 곱셈만으로 결과가 나올 수 있다. 숫자가 커질수록 줄어드는 양은 더 클 것이다.
>
> <center><img width="1000" src="https://user-images.githubusercontent.com/37801041/73610333-60c6f600-4619-11ea-8843-dfb65b998f10.jpeg" alt="IMG_E0117D4E39E4-1" style="zoom:50%;" /></center>
>
> <br>
>
> 필자는 이렇게 분할을 하게하고 마지막에 C로 모듈라 연산을 진행하여 결과를 출력해주었는데 시간초과가 나왔다... 그래서 뭐가 문제인가 생각을 해본 결과 C로 나눈 나머지라서 언제든지 모듈라 연산을 진행하여 곱해주어도 상관이 없다는 것을 캐치해냈고 `B를 분할하여 곱셈을 진행할때마다 C로 나눈 나머지로 만들어 반환`을 해주니 문제를 해결할 수 있었다.

<br>

## 코드

```python
# 1629번 곱셈

# B를 2분할해가면서 곱셈 진행
def devide(a,n):
    # c로 나눈 나머지므로 계속 나눈 나머지를 곱해도 결과는 동일.
    # 여기서 % c를 해주지 않으면 시간초과
    if n==1:
        return a % c
    elif n==2:
        return a*a % c
    else:
        tmp = devide(a,n//2)
        if n%2 == 0:
            return tmp*tmp % c
        else:
            return tmp*tmp*a % c

a,b,c = map(int,input().split())

result = devide(a,b)
print(result)
```

