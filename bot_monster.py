"""module parsing monster website"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from highlight import highlight_element
from jobclass import JobListing

# Chemin vers le fichier exécutable du navigateur
# Assurez-vous d'avoir téléchargé le pilote approprié pour votre navigateur
options = webdriver.EdgeOptions()
options.add_argument("--disable-cookies")  # Désactiver les cookies

# Initialisation du navigateur
driver = webdriver.Edge(options=options)

# Charger la page avec le formulaire
driver.get('https://www.monster.fr')
time.sleep(5) #wait 5 seconds   

try:    
    driver.find_element(By.ID,"onetrust-reject-all-handler").click()
except:
    pass

job_input = driver.find_element(By.NAME,"q")
job_input.send_keys("devops")
job_input.send_keys(Keys.TAB)

where_input = driver.find_element(By.NAME,"where")
where_input.send_keys("Nantes")
where_input.send_keys(Keys.TAB)

button_search = button = driver.find_element(By.CSS_SELECTOR,"[data-testid='searchbar-submit-button-desktop']")
button_search.click()
time.sleep(5) #wait 5 seconds   

conteneur = driver.find_element(By.CSS_SELECTOR, "div[class^='job-search-resultsstyle__CardGrid']")
links = conteneur.find_elements(By.TAG_NAME, "a")
time.sleep(5) #wait 5 seconds
list_link=[]

for link in links:
    href = link.get_attribute("href")
    list_link.append(href)
joblist = []
time.sleep(5) #wait 5 seconds
for  href in list_link:
    driver.get(href)
    time.sleep(2)
    title = driver.find_element(By.CLASS_NAME, "JobViewTitle").text
    location =  driver.find_element(By.CSS_SELECTOR,"[data-test-id='svx-jobview-location']").text
    date =  driver.find_element(By.CSS_SELECTOR,"[data-test-id='svx-jobview-posted']").text

    try:
        salary = driver.find_element(By.CSS_SELECTOR,"[data-testid='svx_jobview-salary']").text 
    except:
        salary = None

    description =  driver.find_element(By.CSS_SELECTOR, "div[class^='descriptionstyles__DescriptionBody-']").text
    # new JobListing(title=title,salary=salary,)

