import requests

def get_ip_address():
    url = 'https://api.myip.com/'
    response = requests.get(url)
    data = response.json()
    ip_address = data['ip']
    country = data['country']
    return ip_address, country

# Example usage
ip = get_ip_address()
print("Your IP address is:", ip)
#print("Your country:", country)