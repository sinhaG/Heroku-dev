import requests

response = requests.get('https://httpbin.org/ip')
print(response)
print('Your IP is {0}'.format(response.json()['origin']))