num1 = 0

# 파이선 => 함수지향형
# 함수를 생성해서, 함수를 호출하는 방식으로 코딩을 수행

def myName():
    return "대한민국"

def myfunc():
    a = 3
    b = 4
    return a+b

num1 = myfunc()
print(num1)

for i in range(10) :
    # print("대한민국")
    print(myName())
    
# 함수를 사용해서 코딩을 하는 이유
'''
어떤 코드 묶음을 반복적으로 사용해야 할 경우
반복적인 코드를 복사 붙이기를 통해 사용할수도 있지만
코딩을 할 때 반복적인 코드가 많아지면 오류(논리적인)가 발생 할 확률이 높아진다.
그러한 문제를 방지하기 위해 함수라는 것을 사용한다.
'''

num1 = 10
num2 = 12
print(num1+num2)

num1 = 44
num2 = 12
print(num1+num2)

num1 = 33
num2 = 54
print(num1+num2)

num1 = 23
num2 = 53
print(num1+num2)

