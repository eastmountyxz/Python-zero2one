import requests

r = requests.get('https://github.com/timeline.json')
r = requests.post("http://httpbin.org/post")
print(r)
