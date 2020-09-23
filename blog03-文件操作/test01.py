infile = open("test.txt","r",encoding="utf8")
data = infile.read()
print(data)
print("")

infile = open("test.txt","r",encoding="utf8")
list_data = infile.readlines()
print(list_data)
