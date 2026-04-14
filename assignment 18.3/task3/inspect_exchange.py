import requests

url = 'https://api.exchangerate.host/latest'
params = {'base': 'INR', 'symbols': 'USD,EUR,GBP'}
r = requests.get(url, params=params, timeout=10)
print(r.status_code)
print(r.headers.get('Content-Type'))
print(r.text)
