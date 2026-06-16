import requests

BASE_URL ="https://worldcupjson.net"
def get(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()