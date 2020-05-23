# [백준9251번] LCS (Long Common Subsequence)

## 문제

LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

## 입력

첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

## 출력

첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

## 예제 입력 1 복사

```
ACAYKP
CAPCAK
```

## 예제 출력 1 복사

```
4
```



## 나의 풀이

> 이 문제는 LCS (Long Common Subsequence), Long Common String과 다르게 연속되는 문자가 아닌 부분수열을 찾는 문제이다. 나는 이번에 LCS문제를 처음 접해서 어떻게 풀어야할지 감을 잘 잡지못하였다. 두 문자열의 index로 dp를 사용해 최댓값을 저장해가며 풀어보려했지만 잘 되지 않았다. 그래서 검색을 해본결과 2차원배열을 사용해서 풀면 되었었다.
>
> 이 문제를 푸는 방법은 2차원 배열을 사용해 각 문자들끼리 비교를 하며 같을 경우 공통된 부분수열의 크기(대각선 위쪽의 값)를 1씩 증가시켜나가고 같지 않을 경우에는 바로 전(즉, 바로 왼쪽과 위쪽) 중 큰 값을 가지고가는 것이다. 이 방법은 아래 그림으로 보면 더 쉽게 이해를 할 수 있을 것이다. 아래 그림을 보면 오른쪽 두가지의 경우의 수를 가지고 왼쪽의 2차원 배열을 완성시킬 수 있다.
>
> 처음에 이 문제에대해 검색을 해보고 글만 읽어보았을때에는 잘 이해가 가지않았는데 2차원배열의 그림을 보고 혼자서 한번 표를 만들어보니 금방 이해를 할 수 있었다. 잘 이해가 안가는 독자가 있다면 꼭 직접 그림을 그려서 해보기를 추천합니다.

![IMG_F0120022F7C1-1](https://user-images.githubusercontent.com/37801041/72216010-84d57100-355e-11ea-9811-5f9a91642ec9.jpeg)



## 코드

```java
import java.util.Scanner;

/**
 * 9251번 LCS
 */
public class Baeckjun9251 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s1,s2;

        s1 = sc.next();
        s2 = sc.next();

        int[][] dp = new int[s1.length()+1][s2.length()+1];

        for (int i=1; i<=s1.length(); i++) {
            for (int j=1; j<=s2.length(); j++) {
              	// String을 index를 통해 값을 가져오기위해 charAt()을 사용.
                if (s1.charAt(i-1) == s2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                }
                else dp[i][j] = Math.max(dp[i][j-1],dp[i-1][j]);
            }
        }

        System.out.println(dp[s1.length()][s2.length()]);
    }
}

```



