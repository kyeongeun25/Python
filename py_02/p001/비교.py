# 비교(if)의 사용
num1 = 38
if(num1 % 2 ==0) :
    print("짝수")     # 첫 글자가 들여쓰기가 된 문장은 위의 문장에 포함된 문장이다.
    print("안녕")
    print("반갑습니다") 
else : 
    print("홀수")
    
print("if종료")   # 이 문장은 위의 다른 문장과는 독립적인 문장이다.

num1 = 45
num2  = 3
if(num1 % num2 == 0 ) :
    print("3의 배수이다")
elif(num1 % 2 == 0) :
    print("짝수이다")