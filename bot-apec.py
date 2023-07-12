print("test")
#a function to parse apec website with selenium
from selenium import webdriver as wd    
from selenium.webdriver.common.by import By    #import webdriver
from selenium.webdriver.common.keys import Keys #import keys
from selenium.webdriver.common.action_chains import ActionChains #import action_chains  
import time #import time            

#open apec website      
driver = wd.Chrome()    
driver.get("https://www.apec.fr/candidat.html") #open apec website  

#parse apec website with selenium       
time.sleep(5) #wait 5 seconds       
driver.find_element(By.NAME,"keywords").send_keys("devops") #send keywords  
time.sleep(5) #wait 5 seconds   
where_input = driver.find_element(By.NAME,"locationOffresDisplay") #send where
where_input.send_keys("nantes") #click login button     
where_input.send_keys(Keys.RETURN)  
#click button onetrust-reject-all-handler if exist
try:    
    driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
except:
    pass

#find button type="submit"
# button = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")            
# button.click()
# driver.find_element_by_id("username").send_keys("username") #enter username
# driver.find_element_by_id("password").send_keys("password") #enter password
time.sleep(5) #wait 5 seconds   
