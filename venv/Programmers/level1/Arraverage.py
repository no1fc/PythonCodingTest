"""
정수 배열 numbers가 매개변수로 주어집니다.
numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
"""

def solution(numbers):

    ##배열을 받습니다.
    ##받은 배열에 모든 정수를 더합니다.
    ##배열 개수만큼 나눠 평균을 구합니다.
    return 1.0 * sum(numbers) / len(numbers)
result = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(result)