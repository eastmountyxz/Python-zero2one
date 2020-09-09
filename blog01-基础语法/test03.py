"""数字类型"""
z = -12.3 + 8j
print(z, type(z))
print(z.real, z.imag)

counter = 100         #赋值整型变量
miles = 1000.0        #浮点型
print(counter, type(counter))
print(miles, type(miles))


"""字符类型"""
name = "Eastmount"    #字符串
s = 'abcdef'
print(s[1:5])


"""列表类型"""
list1 = [1, 2, 3, 4, 5]
print(list1)
#[1, 2, 3, 4, 5]

print(list1[0])
print(type(list1))
#<type 'list'>

list2 = ['I', 'am', 'a', 'teacher']
print(list2)
#['I', 'am', 'a', 'teacher']
print(list2[3])
#teacher

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8]

print(list1+list2)
#[1, 2, 3, 4, 5, 6, 7, 8]
print(list2*3)
#[6, 7, 8, 6, 7, 8, 6, 7, 8]
print(list1[2:4])
#[3, 4]


"""元组类型"""
t1 = (12, 34, 'Python')
print(t1)
#(12, 34, 'Python')
print(type(t1))
#<type 'tuple'>
print(t1[2])
#Python
 

"""字典类型"""
dic = {"1":"Beijing","2":"Shanghai","3":"Chengdu","4":"Guiyang"}
print(dic)
#{'1': 'Beijing', '3': 'Chengdu', '2': 'Shanghai', '4': 'Guiyang'}
print(dic["4"])
#Guiyang

