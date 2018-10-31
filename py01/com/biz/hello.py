'''
Created on 2018. 8. 28.

@author: 506-09
'''

num1 =3
num2 =4
sum = num1 + num2
print(sum)

name = "홍길동"
addr = "대한민국"
print(name + addr)

sum = 0
for i in range(101) :
    if(i % 2 == 0):
        sum += i
    
print(sum)

# 리스트
# 일반적인 배열과 유사한 형태
arr = [3,4,5,6,7,8,9,10]
for i in arr :
    sum += i
    print(i)
    
print(sum)

arrA = [] #빈리스트
arrB = [1,2,3] #숫자리스트
arrC = ["대한민국", "우리나라"] #문자열리스트
arrD = [1,2,3, "korea"]
arrE = [1,2,3,[1,2,3,[2,3,4]]]  

# 집합(set)
arr1 = {3,4,5,6,7,8,9,10}
for i in arr1 :
    print(i)
    
# 튜플
arr2 = (1,3,4,5,6,7,8)
for i in arr2 :
    print(i)
    
aaa = "k" * 10
print(aaa)

for i in range(10) :
    print("* "*i)