import requests

# [!] Secret hardcoded
API_KEY = "sk_live_1234567890abcdef1234567890abcdef"

# [~] Sem tratamento de erro em fetch()
def fetch(endpoint):
    url = f"https://api.exemplo.com/{endpoint}?key={API_KEY}"
    response = requests.get(url)
    return response.json()