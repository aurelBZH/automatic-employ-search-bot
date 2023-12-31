"""highlight the element"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions

def highlight_element(element):
    """
    Highlight the given element by applying a temporary highlight style.
    
    Parameters:
    - element: The element to be highlighted.
    
    Returns:
    None
    """
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

    except exceptions.TimeoutException:
        pass

    finally:
        # Restore the original style of the element
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, original_style)
