def solution(numbers):

    ##배열을 받습니다.
    ##받은 배열에 모든 정수를 더합니다.
    ##배열 개수만큼 나눠 평균을 구합니다.
    return 1.0 * sum(numbers) / len(numbers)
result = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(result)