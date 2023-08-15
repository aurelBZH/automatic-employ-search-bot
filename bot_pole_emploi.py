import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from jobclass import JobListing

from library import reject_cookies,scroll_to_bottom,is_button_present ,scroll_page, is_element_present_on_screen, is_at_bottom, is_element_present_on_screen_css 

# Chemin vers le fichier exécutable du navigateur
# Assurez-vous d'avoir téléchargé le pilote approprié pour votre navigateur
options = webdriver.ChromeOptions()
options.add_argument("--disable-cookies")  # Désactiver les cookies

# Initialisation du navigateur
driver = webdriver.Chrome(options=options)
# Charger la page avec le formulaire
driver.get('https://candidat.pole-emploi.fr/offres/emploi')
time.sleep(5) #wait 5 seconds   
driver.find_element(By.CLASS_NAME,'tc-open-privacy-center').click()
driver.find_element(By.ID, 'idmotsCles-selectized').send_keys('devops')
driver.find_element(By.ID,'idlieux-selectized').send_keys('Nan')
time.sleep(1)
driver.find_element(By.ID,'idlieux-selectized').send_keys('tes')
 #wait 5 seconds
driver.find_element(By.ID,'idlieux-selectized').send_keys(Keys.ENTER)
driver.find_element(By.ID,'btnSubmitRechercheForm').click()
time.sleep(3)

button_selector = '#zoneAfficherPlus a.btn.btn-primary'

# Function to check if the button is present in the DOM

while True:
    scroll_page(driver,800)
    print(is_element_present_on_screen_css(driver,button_selector))
    if (is_button_present(driver, button_selector) and is_element_present_on_screen_css(driver,button_selector)):
        try:
            button = driver.find_element(By.CSS_SELECTOR,button_selector)
            time.sleep(1)
            button.click()
        except (StaleElementReferenceException,NoSuchElementException):
            pass    
    elif is_at_bottom(driver) and  not is_button_present(driver,button_selector):
        break

# Now you can interact with the button
links = driver.find_elements(By.CSS_SELECTOR,'a.media')
link_list = []
job_list = []
for link in links:
    href = link.get_attribute("href")
    link_list.append(href)

for link in link_list:
    driver.get(link)
    title = driver.find_element(By.CSS_SELECTOR,'span[itemprop="title"]').text  
    print(title)
    city = driver.find_element(By.CSS_SELECTOR,'span[itemprop="addressLocality"]').text  + ' ' + driver.find_element(By.CSS_SELECTOR,'span[itemprop="addressRegion"]').text
    try:
        dt_element = driver.find_element(By.CSS_SELECTOR,'dt span[title="Type de contrat"]')

        # Get the content of the <dd> element following the <dt>
        dd_element = dt_element.find_element(By.XPATH,'following-sibling::dd')
        employment_type = dd_element.text
    except:


    try:
        dt_element = driver.find_element(By.CSS_SELECTOR,'dt span[title="Salaire"]')

    except:
        salary = ''
    

        


    #job_list.append(JobListing(title=title,salary=salary,type=employment_type,link=link,description=description,city=city,responded=False,response="",publicationdate=date))

driver.quit()
# reject_cookies(driver)