from pydoc import resolve
a = [0]*10
for i in range(10) :
    print(f'{i}번째 반복중입니다.')
    a[i] = i

print(a)
print(list(reversed(a)))
print(resolve(a))