from bs4 import BeautifulSoup
soup = BeautifulSoup(open('test04_01.html'), "html.parser")
tag = soup.title
print(type(tag.string))
#<class 'BeautifulSoup.NavigableString'>

unicode_string = tag.string
print(unicode_string)
#BeautifulSoup技术
print(type(unicode_string))
#<type 'unicode'>

markup = "<b><!-- This is a comment code. --></b>"  
soup = BeautifulSoup(markup, "html.parser")
comment = soup.b.string  
print(type(comment)) 
# <class 'bs4.element.Comment'>
print(comment)  
# This is a comment code.
