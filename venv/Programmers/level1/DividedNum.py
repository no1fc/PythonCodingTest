'''
array의 각 element 중 divisor로 나누어 떨어지는 값을
오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
'''
def solution(arr, divisor):
    answer = []
    #배열에 값을 받습니다.
    #값을 받아온 정수로 나눠 나머지가 0인 값만 배열에 담습니다.
    #배열에 담긴 정수를 나열합니다.

    answer = sorted([i for i in arr if i%divisor==0])
    return answer if answer else [-1]

result = solution([3,2,6],10);
print(result)