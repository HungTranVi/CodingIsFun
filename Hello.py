# #1 Hello World
# print ("Hello World")

# #2 Variable 
# int = 1
# Hung = "Hùng"
# Arr = ['1','123', 'Hung Dep Trai', '12`132423423452453456363463']
# print(int)
# print(Hung)
# print(Arr)
# print(Arr[0])

# dict1 = {'Ho va ten': "Tran Vi Hung", 'So_do':[90,90,90], 'chieu_cao': 1.78,'quoc_tich':"Viet Nam"}

# print (dict1['Ho va ten']+" co chieu cao la "+str(dict1['chieu_cao']))

# strDemo = "Demo 'hehe' "
# print(strDemo)
# i=0
# while  i <= 10:
#     print(strDemo+str(i))
#     i+=1

# Howk = """I"m a fucking hehe\a
# And I think I love programming\tHehehehee
# Esspecailly  python\b"""
# print(Howk)

# print('\a')

# print(r'C\ProgramFile\nI_lov_you')

# strA = "Hello"
# strB = "Fuck"
# strC = strA + '\n' +strB
# print(strC)
# print("H" in strA)

# print(strA[len(strA)-1])

# from math import *

# strTest = 'l'

# i=0
# while i < len(strA):
#     if strA[i] == strTest:
#      print(i)
#      break
#     i+=1

# strB = str(69) +"5"
# print(strB)


# so = 6.9
# print(ceil(6.9))

# ví dụ: viết hàm thay kí tự trong chuôi bất kì 

# def Replace_Using_while(chuoi, ki_tu):
#     i =0
#     while i < len(chuoi):
#         chuoi[i] = ki_tu

# strA = "Hung Oi Dep trai"
# char = '1'
# # strB = Replace_Using_while(strA,char)
# strB = strA.replace('i',char)
# # print(strB)

# str1 = input("enter your name:")

# a = "Hello %s" %(str1)

# print(a)

# f = 'hungtv41'
# print(f)
# h='con me may '
# f1 = f'{h}ungtv41'
# print(f1)

# one =  input()
# two = input()
# r = "Your name: {}\n Your age: {}".format(one,two)
# print(r)

# r = "Hello{:@^15}Hhahah".format("Yourname")
# print(r)

# a = "hello"
# b = a.capitalize()
# c = a.upper()
# d = "HELlOO"
# e = d.lower()
# f = d.swapcase()
# k = "Hello you  are so BEU    "
# g = k.replace(" ", "")
# print(a,b,c,d,e,f,k,g)

# test = "Hello Hung"
# b = test.center(20,'*')
# print(b)
# c = test.rjust(20,'x')
# d = test.ljust(20,'g')
# print(c)
# print(d)

# test = 'có gì vậy'
# encoded = test.encode(encoding= 'utf-16', errors ='strict')
# print(encoded)

# a  = "ó ó ó ó"
# b = a.replace('ó','o',2)
# print(b)

# a = "prefix How To get it done suffix"
# b = a.removeprefix('prefix')
# c = a.removesuffix('suffix')
# print(a)
# print(b)
# print(c)

# a = "hello I love youu so muach"
# b = a.rsplit(' ',2)
# print(b)

# a = "hello I love youu so muach"
# b = a.partition(' ')
# print(b)

# a = "hello I love youu so muach"
# b = a.count('I')
# print(a)
# print(b)

# s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'.lstrip('aAo').rstrip('a').title()
# print(s)

# # create an emty list 
# a = []

# #List comprehension => list khoi tao = vong lap
# a = [i for i in range(5)]

# #Constructor list => list dc tạo từ khởi tạo từ list và string (cấu trúc tập hợp nhiều phần tử)
# numlist = list([1,2,3])
# strlist = list('HungDepTrai')
# print(numlist)
# print(strlist)

# #Operator in list
# a = [1,2,3]
# b = ['one', 'two', 'three']
# c= [4,5]
# print(a+b)
# print(a*2)

# #matrix
# a = [[1,2,3],[4,5,6],[7,8,9]]
# print(a[0])
# print(a[1])
# print(a[2])

#Operator in python list

# a = id("hello")
# b = id('h')
# print(a,b)


# n =77
# print(n%7)
# print(n.__divmod__(7))

# file_obj = open('filetest.txt')
# #print(file_obj)
# file_obj.close()

# cho 1 file có dãy số đằng sau, hãy dùng kiến thức học, đọc file gốc và ghi hết phần số từ bên phải vào file mới
# dùng with mở và đóng file gốc
# with open('filetest.txt','r+') as file_source:
#     with open('file_processed','w+') as file_des:
#         for i in range (file_source):
#             data = (file_source.readline(i)).rstrip(' ')
#             file_des.writelines(data[1])

# from time import sleep # nhập hàm sleep từ thư viện time

# print('start....', end='')
# sleep(3) # dừng chương trình 3 giây
# print('end...')

# from time import sleep # nhập hàm sleep từ thư viện time

# print('line 1\n', 'line2', end='')
# sleep(3) # dừng chương trình 3 giây
# print('end...')

# from time import sleep # nhập hàm sleep từ thư viện time

# print('line 1', 'lin\ne2', end='')
# sleep(3) # dừng chương trình 3 giây
# print('end...')

# from time import sleep # nhập hàm sleep từ thư viện time

# print('start...', end='')
# sleep(3) # dừng chương trình 3 giây
# print('end...')

# from time import sleep # nhập hàm sleep từ thư viện time

# print('start...', end='', flush=True)
# sleep(3) # dừng chương trình 3 giây
# print('end...')

# from time import sleep

# your_name = "Henry"
# your_great = "Hello! My name is "

# for c in your_great + your_name:
#     print(c, end='', flush=True)
#     sleep(0.1)
# print()


# def printhaha(param):
#     print(param,', Hello')

# printhaha('Hung')


import requests
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)
print(response.json())