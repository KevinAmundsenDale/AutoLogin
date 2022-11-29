import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

browser= webdriver.Chrome(executable_path="D:\\Downloads\\chromedriver.exe")
browser.set_window_size(1920, 1080)

browser.get('https://echo.uib.no/event/inf264-kraesjkurs-med-gnist')
action = webdriver.common.action_chains.ActionChains(browser)


påmelding = browser.find_element("xpath", "//button[contains(string(), 'Påmelding')]")
action.move_to_element_with_offset(påmelding, 5, 5)
action.click()
action.perform()

mail = browser.find_element(By.NAME, "email")
mail.send_keys("Kevin.Amundsen.Dale@gmail.com")
mail.send_keys(Keys.ENTER)

name = browser.find_element(By.NAME, "firstName")
name.send_keys("Kevin")
name.send_keys(Keys.ENTER)

lastname = browser.find_element(By.NAME, "lastName")
lastname.send_keys("Dale")
lastname.send_keys(Keys.ENTER)

degree = Select(browser.find_element(By.NAME, "degree"))
degree.select_by_index(3)

year = Select(browser.find_element(By.NAME, "degreeYear"))
year.select_by_index(3)

try:
    allergi = browser.find_element(By.NAME, "answers.0")
    allergi.send_keys("ingen")
    allergi.send_keys(Keys.ENTER)
except:
    0

term1 = browser.find_element(By.NAME, "terms1")
action.move_to_element_with_offset(term1, 5, 5)
action.click()
action.perform()

term2 = browser.find_element(By.NAME, "terms2")
action.move_to_element_with_offset(term2, 5, 5)
action.click()
action.perform()

term3 = browser.find_element(By.NAME, "terms3")
action.move_to_element_with_offset(term3, 5, 5)
action.click()
action.perform()

term3.send_keys(Keys.PAGE_DOWN)

send = browser.find_element("xpath", "//button[contains(string(), 'Send inn')]")
action.move_to_element_with_offset(send, 5, 5)
action.click()
action.perform()

time.sleep(8) #Stays open for 60 seconds (which is 1 min)

browser.close()

# pos = påmelding.location
# el=browser.find_elements_by_xpath("//button[contains(string(), 'Påmelding')]")[0]
# pos = browser.find_element(By.CLASS_NAME, ('chakra-button css-2c2h1w'))
# print(browser.find_element(By.XPATH, '//button[text()="Påmelding"]'))

# pyautogui.moveTo(pos["y"], pos["x"], duration = 0.1)





# allergi=False

# pyautogui.moveTo(1800, 20, duration = 0.1)
# pyautogui.click()
# pyautogui.moveTo(380, 640, duration = 0.1)
# pyautogui.click()
# pyautogui.moveTo(640, 700, duration = 0.01)
# pyautogui.click()
# pyautogui.typewrite("ingenting")
# pyautogui.typewrite(["enter"])
# pyautogui.moveTo(640, 775, duration = 0.01)
# pyautogui.click()
# pyautogui.moveTo(640, 860, duration = 0.01)
# pyautogui.click()
# if(not allergi):
#     pyautogui.moveTo(1140, 935, duration = 0.01)
#     pyautogui.click()
# else:
#     pyautogui.moveTo(640, 960, duration = 0.01)
#     pyautogui.click()
#     pyautogui.moveTo(1140, 1025, duration = 0.01)
#     pyautogui.click()

# pyautogui.moveTo(315, 20, duration = 0.01)