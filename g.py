from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Pfad zum WebDriver
driver_path = '/path/to/chromedriver'  # Ersetze diesen Pfad durch den tatsächlichen Pfad

# Chrome-Optionen konfigurieren
chrome_options = Options()
chrome_options.add_argument("--headless")  # Führe Chrome im Hintergrund aus

# Erstelle einen Service für den WebDriver
service = Service(driver_path)

# Initialisiere den WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Öffne Roblox-Website
driver.get('https://www.roblox.com')

# Warte hier, falls eine Anmeldung erforderlich ist

# Hole alle Cookies
cookies = driver.get_cookies()

# Ausgabe der Cookies
for cookie in cookies:
    print(f"{cookie['name']}: {cookie['value']}")

# Schließe den Browser
driver.quit()
