print("Hi!My Name is %s,I am %d years old and %f pounds heavy."%("YXZ", 26, 55.5))
#Hi!My Name is YXZ,I am 26 years old and 55.500000 pounds heavy.

str1 = 'abcdefghijklmn'
print(str1[3:6])
# def

str1 = 'abcdefghijklmn'
print(str1[-1:-5:-1])
# nmlk

str1 = 'abcdefghijklmn'
num = str1.find('def')
print(num)
# 3

str1 = "    I am a teacher    "
print(str1.strip())
#I am a teacher

num = ['I','am','a','teacher']
sep = ' '
str1 = sep.join(num)
print(str1)
#I am a teacher

