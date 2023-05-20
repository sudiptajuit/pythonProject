import requests

print("Get request:================")
payload = {"firstName": "Sudipta", "lastName": "Biswas"}
r = requests.get("https://httpbin.org/get", params=payload)
print(r.url)
print("=========================")
print(r.status_code)
print("=========================")
print(r.content)
print("=========================")
print(r.text)

print("Post request:================")

payload = {"firstName": "Sudipta", "lastName": "Biswas"}
s = requests.post("https://httpbin.org/post", data=payload)
print(s.text)
print("=========================")
print(s.url)
print("=========================")
print(s.status_code)
