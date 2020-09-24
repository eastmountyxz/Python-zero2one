infile = open('test02.txt', 'r', encoding="utf8")
for line in infile.readlines():
   print(line)
print(infile.close())

infile = open('test02.txt', 'r', encoding="utf8").read()
for line in infile:
   print(line)
print(infile.close())
