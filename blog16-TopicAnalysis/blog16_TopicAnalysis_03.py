#coding=utf-8
#By:Eastmount CSDN
from os import path  
from scipy.misc import imread    
import jieba  
import sys  
import matplotlib.pyplot as plt  
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator    
  
# 打开本体TXT文件  
text = open('data-fenci.txt').read()  
  
# 结巴分词 cut_all=True 设置为全模式   
wordlist = jieba.cut(text)     #cut_all = True  
  
# 使用空格连接 进行中文分词  
wl_space_split = " ".join(wordlist)  
print(wl_space_split)
  
# 读取mask/color图片  
d = path.dirname(__file__)  
nana_coloring = imread(path.join(d, "pic.png"))  
  
# 对分词后的文本生成词云  
my_wordcloud = WordCloud( background_color = 'white',    
                            mask = nana_coloring,         
                            max_words = 2000,            
                            stopwords = STOPWORDS,       
                            max_font_size = 50,          
                            random_state = 30,          
                            )  
  
# generate word cloud   
my_wordcloud.generate(wl_space_split)  
  
# create coloring from image    
image_colors = ImageColorGenerator(nana_coloring)  
  
# recolor wordcloud and show    
my_wordcloud.recolor(color_func=image_colors)  
  
plt.imshow(my_wordcloud)    # 显示词云图  
plt.axis("off")             # 是否显示x轴、y轴下标  
plt.show()  
  
# save img    
my_wordcloud.to_file(path.join(d, "cloudimg.png"))  
