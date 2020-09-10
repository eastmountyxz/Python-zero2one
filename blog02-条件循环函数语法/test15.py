#函数定义
def fun2(a,b):  
    print(a,b)
    X = a + b  
    Y = a - b  
    Z = a * b  
    M = a / b  
    N = a ** b  
    return X,Y,Z,M,N

#函数调用
a,b,c,d,e = fun2(4,3)  
print('the result are ',a,b,c,d,e)
re = fun2(2,10)  
print(re)
