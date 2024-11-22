""""
머쓱이는 친구들과 369게임을 하고 있습니다.
369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는
숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다.
머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때,
머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

프로그램이 시작됩니다.
3,6,9에서 박수를 치면 박수칠때 count 한다.

문자열로 변경하고 비교한다.
배열을 반복하여 값을 확인하고 3,6,9가 나오면 값을 count 한다.

"""

## 내 풀이
'''
def solution(order):
    answer = 0
    for i in str(order) :
        if i == "3" or i == "6" or i == "9" :
            answer += 1
    return answer

result = solution(input())
print(result)
'''

def solution(order):
    answer = 0
    arr = ['3','6','9']
    for i in str(order) :
        if str(order) in arr :
            answer += 1
    return answer

result = solution(input())
print(result)