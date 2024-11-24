"""
문제 JademCase 문자열 만들기

문제 설명
JadenCase란 모든 단어의 첫 문자가 대문자이고,
그 외의 알파벳은 소문자인 문자열입니다.
단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
s는 길이 1 이상 200 이하인 문자열입니다.
s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
숫자는 단어의 첫 문자로만 나옵니다.
숫자로만 이루어진 단어는 없습니다.
공백문자가 연속해서 나올 수 있습니다.
입출력 예
s	                    return
"3people unFollowed me"	"3people Unfollowed Me"
"for the last week"	    "For The Last Week"
※ 공지 - 2022년 1월 14일 제한 조건과 테스트 케이스가 추가되었습니다.
"""
def solution(s):
    # 한 단어씩 배열로 만들어줍니다.
    # 배열에 첫 단어의 앞글자가 정수인지 확인합니다.
    # 정수가 아니라면 첫글자를 대문자로 변경
    # 정수라면 그대로 입력합니다.
    s = s.lower()
    result = []
    for i in s.split(" "):
        if i == '':
            result.append(" ")
        else:
            if i[0].isdigit():
                result.append(i + " ")
            else:
                result.append(i.title() + " ")

    return "".join(result)[:-1]


print(solution(" 3people    unFollowed    me"))
print(solution("for the    last week"))