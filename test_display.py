import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up the WebDriver
driver = webdriver.Chrome()
driver.get('https://www.monster.fr/emploi/recherche?q=devops&where=Nantes&page=12&so=m.h.s')

def can_scroll():
    # Compare the current and previous scroll heights
    return driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")

# Function to scroll to the bottom of the page
def scroll_to_bottom():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Scroll until the end of the page
previous_height = 0
current_height = can_scroll()
time.sleep(5)
while current_height > previous_height:
    previous_height = current_height
    scroll_to_bottom()
    current_height = can_scroll()


# Close the browser
driver.quit()
