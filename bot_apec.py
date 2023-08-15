"""
module parsing apec website
"""
import time #import time            
from selenium import webdriver as wd    
from selenium.webdriver.common.by import By    # import webdriver
from selenium.webdriver.common.keys import Keys # import keys
from highlight import highlight_element
from library import reject_cookies
from jobclass import JobListing
# open apec website      

class Apec_bot:
    def __init__(self, job_input, where_input, contract_type=None):
        self.job_input = job_input
        self.where_input = where_input
        self.contract_type = contract_type
        self.list_link = []
        self.job_list = []
        
    def get_offer_info(self,driver):
        """
        Get offer information from a job search website.
        
        Args:
            driver (webdriver): A webdriver instance.
        Returns:
            list_link (list): A list of links to the offers.
        """
        # Chemin vers le fichier exécutable du navigateur
        # Assurez-vous d'avoir téléchargé le pilote approprié pour votre navigateur
        
        # Charger la page avec le formulaire
      
    # parse apec website with selenium   
        driver.get('https://www.apec.fr/candidat.html')     
        time.sleep(5) # wait 5 seconds
        reject_cookies(driver)
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

        # Parcourir chaque élément <a> et extraire le lien
        print(driver.current_url+"&page=")

        for i in range(0,8):
            driver.get(driver.current_url+"&page="+str(i))
            time.sleep(3)
            while True:
                try:
                    conteneur = driver.find_element(By.CLASS_NAME, "container-result")
                    links = conteneur.find_elements(By.TAG_NAME, "a")
                    break
                except:
                    pass

            for link in links:
                href = link.get_attribute("href")
                if type(href) == str:
                    self.list_link.append(href)
        
    def create_joblist(self,driver):
        """
        Get offer information from a job search website.
        
        Args:
            driver (webdriver): A webdriver instance.
        Returns:
            list_link (list): A list of links to the offers.
        """
        # Chemin vers le fichier exécutable du navigateur
        # Assurez-vous d'avoir téléchargé le pilote approprié pour votre navigateur
        
        # Charger la page avec le formulaire
        for  href in self.list_link:
            driver.get(href)    
            title = driver.find_element(By.TAG_NAME, "h1").text
            date =  driver.find_element(By.CLASS_NAME,"date-offre").text
            salary = driver.find_element(By.CSS_SELECTOR,".details-post span").text 
            description =  driver.find_element(By.CLASS_NAME,"details-post").text 
            print(title)
            balise_spans = driver.find_elements(By.CSS_SELECTOR,'.details-offer-list span')
            employment_type =  driver.find_element(By.CSS_SELECTOR,'.details-offer-list span').text
            city = driver.find_elements(By.CSS_SELECTOR,'.details-offer-list li')[2].text
            link = driver.current_url
            self.job_list.append(JobListing(title=title,salary=salary,type=employment_type,link=link,description=description,city=city,responded=False,response="",publicationdate=date))
        return self.job_list

