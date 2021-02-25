import requests
import json
  
r = requests.post('https://api.github.com/some/endpoint',
                  data=json.dumps({'some': 'data'}))
print(r.json())
