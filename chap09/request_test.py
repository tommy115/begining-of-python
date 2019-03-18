import requests
url = 'https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/fortune_cookie_random2.txt'
resp = requests.get(url)

print("###########print response########")
print(resp)

print("###########print response text########")
print(resp.text)

"""
for method in dir(resp):
    print(method)
"""
