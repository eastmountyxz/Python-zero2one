import requests

#设置浏览器代理,它是一个字典
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
url = 'https://movie.douban.com/top250?start=0&filter='

#向服务器发出请求
r = requests.get(url = url, headers = headers)
print(r.text)
