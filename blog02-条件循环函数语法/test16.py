def fun3(a,b,c=10):
    print(a,b,c)
    n = a + b + c
    return n
  
print('result1 =',fun3(2,3))
print('result2 =',fun3(2,3,5))
