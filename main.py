## import package

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


###########################################

# driver code
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.techwithtim.net/")
print(driver.title)
#########################################

# action code
# search = driver.find_element_by_name("s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

##############################################
# main = driver.find_element_by_id("main")
# print(main.text)
#############################################


## printing web page source
# -- print(driver.page_source)
#########################################

link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    # driver.back()
    # driver.back()
    # driver.back()
    # driver.forward()
    # driver.forward()


except:
    driver.quit()


# time.sleep(5)

# driver.quit()