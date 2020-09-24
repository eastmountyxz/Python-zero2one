outfile1 = open('test.txt','a+',encoding="utf8")
str1 = '\nhello\n'  
str2 = 'world\n'
outfile1.write(str1)  
outfile1.write(str2)
outfile1.close()
  
outfile2 = open('test02.txt','w',encoding="utf8")
outfile2.writelines(['hello',' ','world'])  
outfile2.close()

infile = open('test.txt','r',encoding="utf8")
data = infile.read()
print(data)
