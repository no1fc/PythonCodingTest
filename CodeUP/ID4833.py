
def checkN(s,n) :
    count = int(0)
    stack = []
    for i in range(s) :
        if chr(ord(n[i])) == '(' :
            stack.append(chr(ord(n[i])))
        else :
            stack.pop()
            if stack[-1] == '(' :
                count+=len(stack)
            else :
                count+=1
    return count


# n = "()(((()())(())()))(())"
#( 괄호가 나오고
#) 괄호가 나오면 레이저가 생성
# 이전에 나온 (개수를 더한다
n = input()
count = checkN(len(n),n)
print(count)