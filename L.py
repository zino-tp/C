from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# Automatisches Installieren von ChromeDriver
chromedriver_autoinstaller.install()

# Konfiguriere die Chrome-Optionen
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Führe Chrome im Hintergrund aus

# Initialisiere den WebDriver
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Öffne Roblox
    driver.get("https://www.roblox.com/")

    # Füge hier zusätzliche Schritte hinzu, um dich anzumelden
    # (Beispiel: Fülle das Anmeldeformular aus, klicke auf den Anmelde-Button, etc.)

    # Warten, bis die Anmeldung abgeschlossen ist
    input("Drücke Enter, nachdem du dich manuell angemeldet hast...")

    # Hole Cookies
    cookies = driver.get_cookies()
    
    # Zeige Cookies an
    for cookie in cookies:
        print(f"Cookie-Name: {cookie['name']}, Cookie-Wert: {cookie['value']}")
        
finally:
    driver.quit()
