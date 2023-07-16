print("test")
# a function to parse apec website with selenium
from selenium import webdriver as wd    
from selenium.webdriver.common.by import By    # import webdriver
from selenium.webdriver.common.keys import Keys # import keys
import time #import time            
from highlight import highlight_element
# open apec website      
driver = wd.Chrome()    
driver.get("https://www.apec.fr/candidat.html") # open apec website  

# parse apec website with selenium       
time.sleep(5) # wait 5 seconds
try:    
    driver.find_element(By.ID,"onetrust-reject-all-handler").click()
except:
    pass
time.sleep(5) # wait 5 seconds
employ_input = driver.find_element(By.NAME,"keywords")
employ_input.send_keys("devops") # send keywords  
time.sleep(5) # wait 5 seconds   
employ_input.send_keys(Keys.TAB)  

where_input = driver.find_element(By.NAME,"locationOffresDisplay") # send where
time.sleep(5) # wait 5 seconds   

where_input.send_keys("nantes") # click login button     
time.sleep(5) # wait 5 seconds   

where_input.send_keys(Keys.RETURN)  
# click button onetrust-reject-all-handler if exist

# find button type="submit"
button = driver.find_element(By.CLASS_NAME,"btn-search") 
highlight_element(button)           
button.click()
while True:
    try:
        conteneur = driver.find_element(By.CLASS_NAME, "container-result")
        links = conteneur.find_elements(By.TAG_NAME, "a")
        break
    except:
        pass

# Parcourir chaque élément <a> et extraire le lien
list_link=[]
for link in links:
    href = link.get_attribute("href")
    list_link.append(href)


for  href in list_link:
    driver.get(href)    
    
    driver.back()




# driver.find_element_by_id("username").send_keys("username") #enter username
# driver.find_element_by_id("password").send_keys("password") #enter password
time.sleep(5) #wait 5 seconds   
