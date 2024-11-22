#여러 데이터를 받아야하니
#배열을 생성한다.
#생성된 배열의 크기는 사용자가 정한다.
#정한 크기만큼 배열에 데이터를 넣어준다.
#이때 들어온 데이터가 0이라면 배열에 값을 지워준다.
#만약 들어온 데이터가 0이 아니라면 배열에 값을 추가한다.
#마지막으로 최종 total 값을 출력해준다.

list = []
total = int(0)
n = int(input())

for i in range(n) :
    data = int(input())
    if data == 0 :
        list.pop()
    else :
        list.append(data)

for i in range(len(list)) :
    total += list[i]

print(total)