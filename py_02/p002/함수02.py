alist1 = [30, 30, 52, 34, 43, 22, 23, 44, 55,6]

# alist1의 요소에 9의 값을 덧셈 뺄셈 곱셈 나눗셈을 표시하고 싶다.

# 반복적인 코드로 인한 논리적인 오류 발생 최소화
# 반복적인 코드를 묶어서 함수라는 하나의 코드묶음으로 만들어두고
# 그 이름을 사용해서 코드를 실행하도록 하는 것

# 함수 선언하기
# 1. def 키워드로 시작한다.
# 2. 함수의 이름 : 보통은 첫글자 영문자, 영-숫자, _를 사용한다.
# 3. 한글도 됩니다.
# 4. 함수() : 괄호로 끝난다.
# 5. ()안에 아무런 것도 없으면 단순히 호출만(실행)만 가능한 함수가 된다.
# 6. ()안에 키워드(매개변수, 파라메터:parameter, 인수, 아규먼트:argument)
#    있으면 호출하는 곳에서 어떤 값을 보낼 수 있다.
#    일종의 바구니 역할을 한다.

def 사칙연산(alist):
    for i in alist :
        print("덧셈",i + 9,end=",")
        print("뺄셈",i - 9,end=",")
        print("곱셈",i * 9,end=",")
        print("나눗셈",i / 9,end=",")
    
alist2 = [3,4,5,2,34,2,3,42,4]
사칙연산(alist2)        # 사칙연산 함수 호출하는 곳
                        # 사칙연산 함수는 반드시 호출하는 곳보다 먼저 선언되어야 한다.

# for i in alist1 :
#     print("덧셈",i + 9,end=",")
#     print("뺄셈",i - 3,end=",")       # 고치기빼먹음!!
#     print("곱셈",i * 9,end=",")
#     print("나눗셈",i / 9,end=",")
    
alist3 = [3,4,5,2,34,2,3,42,4]
사칙연산(alist3)

# for i in alist1 :
#     print("덧셈",i + 9,end=",")
#     print("뺄셈",i - 9,end=",")
#     print("곱셈",i * 9,end=",")
#     print("나눗셈",i / 9,end=",")

# 이 덧셈 함수는 두개의 매개변수를 받아서
# 덧셈을 처리한 후 결과는 콘솔에 보이고 종료
def 덧셈(num1, num2):
    sum = num1 + num2
    print(sum)
    
덧셈(3,5)

# 이 덧셈 함수는 두개의 매개변수를 받아서
# 덧셈을 처리한 후 결과를 다시 호출한 곳에 할당값으로 보내준다.
def 덧셈_ret(num1, num2):
    sum = num1 + num2
    return sum

ret = 덧셈_ret(10, 20)
print(ret)





