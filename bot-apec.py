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
driver.find_element(By.NAME,"locationOffres").send_keys("devops") #click login button      

driver.find_element_by_id("username").send_keys("username") #enter username
driver.find_element_by_id("password").send_keys("password") #enter password
time.sleep(5) #wait 5 seconds   
