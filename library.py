from selenium import webdriver

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