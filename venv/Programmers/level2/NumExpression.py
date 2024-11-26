"""
문제 숫자의 표현

문제 설명
Finn은 요즘 수학공부에 빠져 있습니다.
수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

제한사항
n은 10,000 이하의 자연수 입니다.
입출력 예
n	result
15	4
입출력 예 설명
입출력 예#1
문제의 예시와 같습니다.
"""
def solution(n):
    answer = 1
    #정수 n의 값을 받습니다.
    # 정수 n을 연속된 자연수로 표현하는 방법을 구한다.
    # n의 값 만큼 반복하고
    # 다음 반복문에서 n의 값이 num부터 반복한다.
    for num in range(1,n):
        total=0
        for x in range(num, n):
            total += x # 1,2,3,4,5 #4,5,6 #7,8
            # n과 같다면 answer에 +1을 하고 반복문을 종료한다.
            if total == n:
                answer += 1
                break
            # total 보다 n 값이 작다면 반복문을 종료한다.
            elif total > n:
                break

    return answer
print(solution(30))
#다른 사람 풀이
# num=30
# print(len([i  for i in range(1,num+1,2) if num % i == 0]))