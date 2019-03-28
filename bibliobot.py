import selenium
from selenium import webdriver 
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

senhaarqui="suasenha"
loginarquias="seucpf"
browser = Chrome()
browser.get("https://www.athena.biblioteca.unesp.br/F/RR61ETIMN453GKPD568TA7PDXE6NR6T665RJLJ6XB8FG34BTGV-43921?func=BOR-INFO")
time.sleep(5)
for a in range(0,17):
 browser.find_element_by_tag_name("body").send_keys(Keys.TAB)
time.sleep(5)


actions = ActionChains(browser)

actions.key_down(Keys.ENTER)

actions.perform()
time.sleep(5)
browser.find_element_by_id("pat_id").send_keys(loginarquias)
browser.find_element_by_id("pat_password").send_keys(senhaarqui)
browser.find_element_by_id("pat_password").send_keys(Keys.ENTER) 
time.sleep(5)

for a in range(0,17):
 browser.find_element_by_tag_name("body").send_keys(Keys.TAB)

actions = ActionChains(browser)

actions.key_down(Keys.ENTER)

actions.perform()
for a in range(0,22):
 browser.find_element_by_tag_name("body").send_keys(Keys.TAB)
actions = ActionChains(browser)

actions.key_down(Keys.ENTER)

actions.perform()
