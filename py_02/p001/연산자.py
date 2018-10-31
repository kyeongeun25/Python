# 연산자
# 4칙연산
num1 = 40
num2 = 3
print("덧셈 : "+str(num1+num2))
print("뺄셈 : "+str(num1-num2))
print("곱셈 : "+str(num1*num2))
print("나눗셈 : "+str(num1/num2))

print("나머지 : "+str(num1%num2))

# 특별한 산수 연산자
print("나버지 버림 : "+str(num1 // num2))
print("제곱 : " + str(num1 ** 3))     # VB, C#에서는 num1^3

print("num1 : " + str(num1))
print("num2 : " + str(num2))
# num1과 num2의 값을 서로 바꿀 때
num1, num2 = num2 , num1
print("num1 : " + str(num1))
print("num2 : " + str(num2))

# 비교 연산자
if(num1 == num2) :  #같은가?
    print("같다")

if(num1 != num2) : #다른가?
    print("다르다")

if(num1 > num2) :   # num1이 큰가
    print("num1이 크다")
    
if(num1 >= num2) : # num1이 크거나 같은가
    print("num1과 num2가 같거나 num1이 크다")
    
if(1 == 1) :
    print("참")
    
if(1 == 1 and 2 == 2) :
    print("참")
    
if( 1 == 1 or 2 == 3) :
    print("참")
    
if ( 1 == 1 and 2 != 3) :
    print("참")
    
# 참 and 반전(거짓)
if( 1 == 1 and not (2 == 3)) :      # not => ! 
    print("참")

# 할당 연산자
num1 = 3
num1 += 4 # num1 = num1 + 4
num1 -= 4 # num1 = num1 - 4

# 멤버연산자(배열과 관련된 연산자)
list = [1,2,3,4,5,6,7]
if(3 in list) :     #list내에 3이 있냐?
    print("있다")
    
if(10 not in list) :        # list내에 10이 없냐?
    print("그래 없다")
    


# 저장소(기억장소)와 관련된 연산자

num1 = 3
num2 = 4
if( num1 is num2 ) :    #저장소 주소가 같은곳이냐
    print("아니다") 
    
















