from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from library import reject_cookies, find_element_in_iframe,scroll_page
from jobclass import JobListing
import bot_monster
import bot_apec

options = webdriver.ChromeOptions()
options.add_argument("--disable-cookies")  # Désactiver les cookies

# Initialisation du navigateur
driver = webdriver.Chrome(options=options)
# bot_monster_instance = bot_monster.Monster_bot(job_input="devops", where_input="nantes", contract_type="full-time")
# bot_monster_instance.get_offer_info(driver)
# bot_monster_instance.create_joblist(driver)

bot_apec_instance = bot_apec.Apec_bot(job_input="devops", where_input="nantes", contract_type="full-time")
bot_apec_instance.get_offer_info(driver)
bot_apec_instance.create_joblist(driver)
