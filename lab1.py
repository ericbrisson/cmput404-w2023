import requests

# prints version of requests module in current environment
# prints 2.27.1 for my system
# prints 2.28.1 for newly created virutal environment
print(requests.__version__)

response = requests.get("https://www.google.com")
print(response.text)