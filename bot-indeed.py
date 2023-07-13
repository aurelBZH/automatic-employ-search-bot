from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from highlight import highlight_element

# Chemin vers le fichier exécutable du navigateur
# Assurez-vous d'avoir téléchargé le pilote approprié pour votre navigateur
driver_path = 'C:\\Users\\aurel\\Downloads\\edgedriver_win32\\msedgedriver.exe'
options = webdriver.EdgeOptions()
options.add_argument("--disable-cookies")  # Désactiver les cookies

# Initialisation du navigateur
driver = webdriver.Edge(options=options)

# Charger la page avec le formulaire
driver.get('https://fr.indeed.com')

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
elements = driver.find_elements(By.CLASS_NAME, "cardOutline")

# Iterate over each element
elements = driver.find_elements(By.CLASS_NAME, "cardOutline")

# Iterate over each element
for element in elements:
    # Scroll the page to bring the element into view
    print(element)
    highlight_element(element)
    element.click()
    print(driver.find_element(By.CLASS_NAME,"jobsearch-JobInfoHeader-title").text)

    # Print the content
    # print(content)
# submit_button.click()

# Effectuer d'autres actions sur la page des résultats de recherche ici

# Fermer le navigateur
# driver.quit()
