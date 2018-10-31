# 파이썬의 출력문
print(1,2,3,4,5,"대한민국")
num1 = 30
num2 = 40
print(num1, "와", num2, "의 덧셈결과 = ", (num1 + num2))

for i in range(10) :
    print(i, end= "," )
    
keyin = input("숫자를 입력하세요")
print(keyin)


num1 = input("숫자1을 입력하세요")
num2 = input("숫자2를 입력하세요")

print(num1, "+", num2, " = ", (int(num1)+int(num2)))