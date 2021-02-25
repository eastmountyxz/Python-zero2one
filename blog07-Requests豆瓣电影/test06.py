import requests

#获取返回状态
r = requests.get('https://github.com/Ranxf')
print(r.status_code)
print(r.headers)
print(r.cookies)

#打印解码后的返回数据
r1 = requests.get(url='http://dict.baidu.com/s',
                  params={'wd': 'python'})
print(r1.url)
print(r1.text)
