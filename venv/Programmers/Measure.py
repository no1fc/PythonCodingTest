'''
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수,
solution을 완성해주세요.
'''

def solution(n):
    answer = 0
    #입력 받은 값 만큼 반복합니다.
    #반복되는 값을 나눴을 때 나머지가 0 이라면
    #answer 값에 추가한다.

    for i in range(1, n+1) :
        if n % i == 0 :
            answer += i

    print(answer)
    return answer

solution(5)

#print(sum([i for i in range(1, 12+1) if 12 % i == 0]))