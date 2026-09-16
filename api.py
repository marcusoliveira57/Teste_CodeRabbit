import requests

# [!] Secret hardcoded
API_KEY = "minha_chave_secreta_api_12346"

# [~] Sem tratamento de erro em fetch()
def fetch(endpoint):
    url = f"https://api.exemplo.com/{endpoint}?key={API_KEY}"
    response = requests.get(url)
    return response.json()