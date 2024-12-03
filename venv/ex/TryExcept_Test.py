# Java Try - cath
# 예외 발생시 특정 이벤트 실행
def try_except_test(num):
    try:
        1+num
        print("No Error Start try")
    except:
    #except 에러명 :
        print("Error Start except")

def try_except_else_test(num):
    try:
        1+num
        print("No Error Start try")
    except:
        print("Error Start except")
    else:
        print("No Error Start else")

def try_except_finally_test(num):
    try:
        1+num
        print("No Error Start try")
    except:
        print("Error Start except")
    finally:
        print("No Error and Error Start finally")

def try_except_else_finally_test(num):
    try:
        1+num
        print("No Error Start try")
    except:
        print("Error Start except")
    else:
        print("No Error Start else")
    finally:
        print("No Error and Error Start finally")


try_except_test(1)
##Start Debug
## No Error Start try

try_except_else_test(1)
##Start Debug
## No Error Start try
## No Error Start else

try_except_finally_test(1)
##Start Debug
## No Error Start try
## No Error and Error Start finally

try_except_else_finally_test(1)
##Start Debug
## No Error Start try
## No Error Start else
## No Error and Error Start finally


try_except_test("1")
##Start Debug
## Error Start except

try_except_else_test("1")
##Start Debug
## Error Start except

try_except_finally_test("1")
##Start Debug
## Error Start except
## No Error and Error Start finally

try_except_else_finally_test("1")
##Start Debug
## Error Start except
## No Error and Error Start finally