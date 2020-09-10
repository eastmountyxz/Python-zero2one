numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if(number % 2 == 0):      #偶数判断
        even.append(number)
    else:
        odd.append(number)
#输出结果
print(even)
print(odd)
