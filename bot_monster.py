"""module parsing monster website"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from library import reject_cookies, find_element_in_iframe,scroll_page
from jobclass import JobListing

class Monster_bot:
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
        driver.get('https://www.monster.fr')
        time.sleep(5) #wait 5 seconds   

        reject_cookies(driver)

        job_input_elem = driver.find_element(By.NAME,"q")
        job_input_elem.send_keys(self.job_input)
        job_input_elem.send_keys(Keys.TAB)

        where_input_elem = driver.find_element(By.NAME,"where")
        where_input_elem.send_keys(self.where_input)
        where_input_elem.send_keys(Keys.TAB)

        button_search = driver.find_element(By.CSS_SELECTOR,"[data-testid='searchbar-submit-button-desktop']")
        button_search.click()
        # time.sleep(5) #wait 5 seconds   
        time.sleep(5) #wait 5 seconds
        def can_scroll_down(driver):
            # Get the current scroll position
            prev_scroll_position = driver.execute_script("return window.pageYOffset;")
            
            # Perform a scroll action
            scroll_page(800, driver)
            
            # Wait for a short period to let the page load
            time.sleep(3)
            
            # Get the new scroll position after the scroll action
            new_scroll_position = driver.execute_script("return window.pageYOffset;")
            
            # Compare scroll positions
            val = new_scroll_position != prev_scroll_position
            return val

        while can_scroll_down(driver):
            can_scroll_down(driver)

        # find_element_in_iframe(driver,"sc-kdBSHD jZSyxV ds-button")
        time.sleep(5)
        conteneur = driver.find_element(By.CSS_SELECTOR, "div[class^='job-search-resultsstyle__CardGrid']")
        links = conteneur.find_elements(By.TAG_NAME, "a")
        time.sleep(5) #wait 5 seconds

        for link in links:
            href = link.get_attribute("href")

            self.list_link.append(href)

        return self.list_link

    def create_joblist(self, driver):
        """
        Creates a job list by scraping job information from a website.

        Parameters:
            driver (WebDriver): The Selenium WebDriver instance used to interact with the web page.

        Returns:
            None
        """
        for  href in self.list_link:
            driver.get(href)
            time.sleep(2)
            title = driver.find_element(By.CLASS_NAME, "JobViewTitle").text
            date =  driver.find_element(By.CSS_SELECTOR,"[data-test-id='svx-jobview-posted']").text

            try:
                salary = driver.find_element(By.CSS_SELECTOR,"[data-testid='svx_jobview-salary']").text 
            except:
                salary = None

            description =  driver.find_element(By.CSS_SELECTOR, "div[class^='descriptionstyles__DescriptionBody-']").text

                # new JobListing(title=title,salary=salary,)
            try:
                employment_type = driver.find_element(By.CSS_SELECTOR,"[data-test-id='svx-jobview-employmenttype']").text
            except:
                employment_type = None
            link = driver.current_url
            city =  driver.find_element(By.CSS_SELECTOR,"[data-test-id='svx-jobview-location']").text
            self.job_list.append(JobListing(title=title,salary=salary,type=employment_type,link=link,description=description,city=city,responded=False,response="",publicationdate=date))
        return self.job_list