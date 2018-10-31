# 한줄짜리 주석

"""
여러줄짜리 주석
"""

# 변수선언
num1 = 0
num2 = 0
num1 = 100
num2 = 100

# 두 개의 숫자를 변수에 할당하고
# 두 변수의 값을 덧셈하여 sum 변수에 보관하고
# sum 변수의 값을 콘솔에 표시
num1 = 20
num2 = 30
sum = num1 + num2
print(sum)

num1 = "대한민국"   # 문자열 할당
# print(num1 + num2)
# sum = num1 + num2

# 파이썬에서는 한번 할당된 변수에 다른 형태의 값을 재할당 할 수 있다.
# 때문에, 어떤 값의 연산 결과에 대하여 철저히 개발자가 책임을 져야 한다.
# 그래서, 파이썬에서는 최소한의 논리적 오류를 막도록 여러가지 <언어적 특징>이 존재를 한다.
# 1. 숫자 + 문자열, 또는 문자열 + 숫자 연산을 일단 허용하지 않는다.

# 숫자를 문자열로 변환
num1 = "30" # 문자열은 '' 또는 "" 묶여진 값(리터널)
num2 = 40

print(num1+str(num2))   # num2를 문자열로 변환

# 문자열을 숫자로 변환
print(int(num1)+num2)   # num1을 숫자(정수형)로 변환

num1 = 30
num2 = 5

# 숫자의 5가지 연산
print("덧셈 : "+str(num1+num2))
print("뺄셈 : "+str(num1-num2))
print("곱셈 : "+str(num1*num2))
print("나눗셈 : "+str(num1/num2)) # 나눗셈 연산을 했을때 python 2.7은 결과가 정수
                               # 3.6(3.7)는 결과가 실수
print("나머지 : "+str(num1%num2))













