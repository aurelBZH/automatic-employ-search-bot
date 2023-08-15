"""module parsing indeed website"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from library import reject_cookies
# Chemin vers le fichier exécutable du navigateur
# Assurez-vous d'avoir téléchargé le pilote approprié pour votre navigateur
options = webdriver.ChromeOptions()
options.add_argument("--disable-cookies")  # Désactiver les cookies

# Initialisation du navigateur
driver = webdriver.Chrome(options=options)

# Charger la page avec le formulaire
driver.get('https://fr.indeed.com')
time.sleep(5) #wait 5 seconds
reject_cookies(driver)
time.sleep(5) #wait 5 seconds
# Rechercher l'élément "Quoi" et entrer la valeur "developpeur aws"
quoi_input = driver.find_element(by=By.ID, value="text-input-what")
quoi_input.send_keys('developpeur aws')

# Rechercher l'élément "Où" et entrer la valeur "Nantes 44"
ou_input = driver.find_element(by=By.ID, value="text-input-where")
# focus = driver.find_element(By.CLASS_NAME, 'icl-TextInputClearable').click()
# clear_button = driver.find_element(By.CLASS_NAME, 'icl-TextInputClearable').click()
print(ou_input)
ou_input.send_keys(Keys.CONTROL + "a")
ou_input.send_keys(Keys.DELETE) 

ou_input.clear()
ou_input.send_keys('Nantes')

# Soumettre le formulaire
# driver.find_element_by_css_selector('form#jobsearch button[type="submit"]').click()
# submit_button = driver.find_element(By.CSS_SELECTOR, 'button.yosegi-InlineWhatWhere-primaryButton')

# Attendre que la page se charge
# Vous pouvez ajuster le délai d'attente en fonction de la vitesse de votre connexion Internet
driver.implicitly_wait(100)
ou_input.send_keys(Keys.RETURN) 
conteneur = driver.find_element(By.CLASS_NAME, "jobsearch-LeftPane")

# Iterate over each element

links = conteneur.find_elements(By.TAG_NAME, "a")
time.sleep(5) #wait 5 seconds
list_link=[]
for link in links:
    href = link.get_attribute("href")
    list_link.append(href)
job_listing = []
# Iterate over each element
for href in list_link:
    # Scroll the page to bring the element into view
    time.sleep(2)
    driver.get(href)
    title = driver.find_element(By.CLASS_NAME,"jobsearch-JobInfoHeader-title").text


    # Print the content
    # print(content)
# submit_button.click()

# Effectuer d'autres actions sur la page des résultats de recherche ici

# Fermer le navigateur
# driver.quit()

def connect(driver):
    email_field = driver.find_element(By.NAME, '__email')
    email_field.send_keys('aurel.beliard@gmail.com')
    email_field.send_keys(Keys.RETURN)
    driver.find_element(By.CLASS_NAME, 'dd-privacy-allow').click()
    time.sleep(5)
    driver.find_element(By.ID, 'auth-page-google-password-fallback').click()
    passwd = driver.find_element(By.ID, "auth-page-google-password-fallback")
    passwd.send_keys('bcabca12456')
    passwd.send_keys(Keys.RETURN)
    