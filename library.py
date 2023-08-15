"""miscellaneous functions"""
"""
Rejects cookies by finding and clicking on the "Reject All" button.

Parameters:
    None

Returns:
    None
"""
from selenium.webdriver.common.by import By
from selenium.common.exceptions import  NoSuchElementException


def reject_cookies(driver):
    """
    Rejects cookies by finding and clicking on the "Reject All" button.

    Parameters:
        None

    Returns:
        None
    """
    try:    
        driver.find_element(By.ID,"onetrust-reject-all-handler").click()
    except:
        pass

def is_element_present_on_screen(driver, class_name):
    """
    Check if an element is present on the screen.

    Args:
        xpath (str): The xpath of the element to check.

    Returns:
        bool: True if the element is present and visible on the screen, False otherwise.
    """
    try:
        element = driver.find_element(By.CLASS_NAME, class_name)
        return element.is_displayed()
    except NoSuchElementException:
        return False

def scroll_page(driver,scroll_amount):
    """
    Scroll the page by a specified amount.
    
    Parameters:
        scroll_amount (int): The amount by which to scroll the page vertically.
        
    Returns:
        None
    """
    driver.execute_script(f"window.scrollBy(0, {scroll_amount});")

def find_element_in_iframe(driver, element_class):
    # Get all iframe elements on the page
    iframes = driver.find_elements(By.TAG_NAME, value='iframe')

    for iframe in iframes:
        # Switch to the current iframe
        driver.switch_to.frame(iframe)

        try:
            # Check if the element with the specified class exists in the current iframe
            element = driver.find_element(By.CLASS_NAME, element_class)

            # If the element is found, return information about the iframe
            iframe_info = {
                'iframe_id': iframe.get_attribute('id'),
                'iframe_src': iframe.get_attribute('src'),
                'element_text': element.text,
                'element_location': element.location,
                'element_size': element.size
            }
            
            # Switch back to the main content (outside the iframe)
            driver.switch_to.default_content()

            return iframe_info

        except NoSuchElementException:
            # If the element is not found in the current iframe, continue searching in the next one
            pass

        # Switch back to the main content (outside the iframe)
        driver.switch_to.default_content()

    # If the element is not found in any iframe, return None
    return None

def scroll_to_bottom(driver):
    """
    Scrolls the web page to the bottom using the given WebDriver.

    Parameters:
    driver (WebDriver): The WebDriver instance used to control the web browser.

    Returns:
    None
    """
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def is_button_present(driver, button_selector):
    """
    Check if a button is present on a web page.

    Parameters:
    - driver: The webdriver instance used to interact with the web page.
    - button_selector: The CSS selector used to locate the button on the web page.

    Returns:
    - True if the button is present, False otherwise.
    """
    return len(driver.find_elements(By.CSS_SELECTOR,button_selector)) > 0

def is_at_bottom(driver):
    return driver.execute_script("return (window.innerHeight + window.pageYOffset) >= document.body.scrollHeight;")

def is_element_present_on_screen_css(driver, css_selector):
    """
    Check if an element is present on the screen.

    Args:
        xpath (str): The xpath of the element to check.

    Returns:
        bool: True if the element is present and visible on the screen, False otherwise.
    """
    try:
        element = driver.find_element(By.CSS_SELECTOR, css_selector)
        return element.is_displayed()
    except NoSuchElementException:
        return False