start = 1
end = 100
step = 1

# start부터 end-1까지 step만큼 증가하면서 반복하라
for i in range(start, end, step) :
    print(i)
    
# start는 0으로 step은 1로 설정
for i in range(end) :
    print(i)
    
# for(int i = 100 ; i < 200 ; i+=10)
for i in range(100,200,10) :
    print(i)
    
list = [1,2,3,4,5,6,7,8,9,10]
for i in list :     # list를 순회하면서..
    print(i)
    
for i in list :
    i = 3
    print(i)
    
print(list)

# for(int i = 0 ; i < list.length ; i++)
for i in range(len(list)) :     # len(list) 리스트의 개수가 몇개냐
    list[i] = 3
    
print(list)

listAndList = [[1,3,4],[0,3,4],["대한민국", "우리나라", "Korea"]]
for(i, j, k) in listAndList :
    print(i,j,k)
    