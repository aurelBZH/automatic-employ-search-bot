from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
def highlight_element(element):
    driver = element._parent

    # Store the original style of the element
    original_style = element.get_attribute("style")

    # Use JavaScript to apply a highlight style to the element
    driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');", element)

    try:
        # Wait for a short duration to display the highlight
        driver.implicitly_wait(0.5)

        # Perform an action to remove the highlight and restore the original style
        ActionChains(driver).move_to_element(element).perform()

    except ScriptTimeoutException:
        pass

    finally:
        # Restore the original style of the element
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, original_style)