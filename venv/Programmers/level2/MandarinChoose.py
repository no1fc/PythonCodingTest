"""
문제 귤 고르기

문제 설명
경화는 과수원에서 귤을 수확했습니다.
경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다.
그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는
귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.

예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다.
경화가 귤 6개를 판매하고 싶다면, 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면,
귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.

경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다.
경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
1 ≤ k ≤ tangerine의 길이 ≤ 100,000
1 ≤ tangerine의 원소 ≤ 10,000,000

입출력 예
k	tangerine	                result
6	[1, 3, 2, 5, 4, 5, 2, 3]	3
4	[1, 3, 2, 5, 4, 5, 2, 3]	2
2	[1, 1, 1, 1, 2, 2, 2, 3]	1

입출력 예 설명
입출력 예 #1
본문에서 설명한 예시입니다.

입출력 예 #2
경화는 크기가 2인 귤 2개와 3인 귤 2개 또는
2인 귤 2개와 5인 귤 2개 또는
3인 귤 2개와 5인 귤 2개로 귤을 판매할 수 있습니다.
이때의 크기 종류는 2가지로 이 값이 최소가 됩니다.

입출력 예 #3
경화는 크기가 1인 귤 2개를 판매하거나 2인 귤 2개를 판매할 수 있습니다.
이때의 크기 종류는 1가지로, 이 값이 최소가 됩니다.
"""

# def solution(k, tangerine):
#     answer = 0
#     #배열을 비교해 같은 값이 있다면 stack에 count하여 값을 추가합니다.
#     # 추가한 값중 count 값이 1이라면 제거해줍니다.
#     stack = [[tangerine[0],1]]
#     total=0
#     # print("aaa:",stack)
#     for i in sorted(tangerine[1:]) :
#         if stack[-1][0] != i :
#             stack.append([i,1])
#         elif stack[-1][0] == i :
#             stack[-1][1] += 1
#     print("stack:",stack.count(1))
#     stack = sorted([i[1] for i in stack if i[1] != 1])
#     # #stack이 있고 total 값이 k 보다 작으면 반복한다.
#     print(stack)
#     while stack and total < k:
#         total += max(stack)
#         stack.pop()
#         answer += 1
#     return answer

# def solution(k, tangerine):
#     answer = 0
#     stack = []
#     ## 1번 방법 통과 X
#     # stack=[tangerine.count(i) for i in stack]
#     # stack = sorted(stack,reverse=True)
#     ## 2번 방법 통과 X
#     for i in list(set(tangerine)) :
#         stack.append(tangerine.count(i))
#     stack.sort(reverse=True)
#     while k > 0:
#         k -= stack[answer]
#         answer += 1
#     return answer

# def solution(k, tangerine):
#     answer = 0
#     stack = []
#     for i in range(max(tangerine)):
#         stack.append(tangerine.count(i+1))
#     stack.sort(reverse=True)
#     print(stack)
#     while k > 0:
#         k -= stack[answer]
#         answer+=1
#     return answer

# 정답 O
from collections import Counter
def solution(k, tangerine):
    # 귤크기 : 개수
    # 딕셔너리 객체 생성
    dic = Counter(tangerine)
    # 개수를 기준으로 내림차순 정렬
    # sorted() 사용 이유는 원본 보존하기 위함
    li = sorted(dic.values(), reverse=True)
    total = 0  # 선택한 귤 개수 총합
    kinds = 0  # 선택한 귤 종류 수
    for v in li:
        total += v
        kinds += 1
        if total >= k:  # 필요한 만큼의 귤을 선택한 경우 종료
            break
    return kinds

print(":",solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))
# print(":",solution(4,[1, 3, 2, 5, 4, 5, 2, 3]))
# print(":",solution(2,[1, 1, 1, 1, 2, 2, 2, 3]))