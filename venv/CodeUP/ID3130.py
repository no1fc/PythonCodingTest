#소의 수를 받는다.
#소의 수는 여럿이니 배열을 생성한다.
#받은 배열의 크기만큼 반복한다.
#다음값을 비교하기 위해 현재 배열 크기에 +1 해서 반복한다
#현재 값보다 다음 값이 더 크다면 반복 종료
# 아니라면 +1
#count로 전체 값을 출력한다

# def cowList(N,cow) :
#     count = 0
#     for i in range(N) :
#         for j in range(i+1,N) :
#             if cow[i]<=cow[j] :
#                 break
#             count+=1
#
#     return count


# 입력 받은 배열만큼 반복한다.
# 배열 안비어있고 현재 값보다 배열 값이 작다면
# 이전 값을 삭제
# 배열이 현재 비어 있거나 배열값이 현재 값보다 크면
# 배열에 값을 추가한다.
# 추가된

def test(N,cow) :
    result=int(0)
    stack=[]
    for i in range(N) :
        print(stack)
        while stack and stack[-1]<cow[i] :
            stack.pop()
            print(i,stack)
        if not stack or stack[-1] > cow[i] :
            stack.append(cow[i])
        result+=len(stack)

    return result -N

# N=6
# cow = [10,3,7,4,12,2]
N = int(input())
cow = [0]*N
for i in range(N) :
    cow[i]=int(input())

result = test(N,cow)
print(result)

