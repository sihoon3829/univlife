#2_22

#리스트 생성하기
list_1 = [1, 2, 3, 4, 5, 1, 3]
list_2 = [ ]
print(list_1)
print(list_2)
print(len(list_1))

#리스트 변경하기
list_1[3] = 9999
print(list_1)
list_1.append(100)
print(list_1)
list_1.remove(9999)
print(list_1)
list_1.insert(0,777)
print(list_1)

#리[스트 복제하기
list_2= list_1.copy( )
print(list_2)