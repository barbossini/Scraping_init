from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
# Initialiser le service pour ChromeDriver
service = Service(executable_path="./chromedriver")
# Initialiser le WebDriver avec le service
driver = webdriver.Chrome(service=service)

# Ouvrir Google
driver.get("https://google.com")
print("Connecting to google website..")

# Utiliser WebDriverWait pour attendre que le bouton des cookies soit cliquable
print("Pushing the button..")
wait = WebDriverWait(driver, 10)
cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "L2AGLb")))
cookie_button.click()

print("Entering 'youtube' text..")
# Utiliser WebDriverWait pour attendre que la barre de recherche soit disponible
search_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))
search_box.send_keys("youtube" + Keys.ENTER)

# Attendre 10 secondes pour voir les résultats
time.sleep(10)

# Fermer le navigateur
driver.quit()
