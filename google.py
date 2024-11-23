from selenium  import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://www.google.com/")

WebDriverWait(driver, 5).until(
	EC.presence_of_all_elements_located(  (By.CLASS_NAME ,  "gLFyf")  )
)

time.sleep(2)

input_element = driver.find_element( By.CLASS_NAME ,  "gLFyf")
input_element.send_keys("Vimal Daga")

time.sleep(2)

input_element.send_keys(Keys.ENTER)

time.sleep(2)

for i in range(500):
	driver.execute_script(f"window.scrollTo(0, {i} )")


WebDriverWait(driver, 5).until(
	EC.presence_of_all_elements_located(  (By.PARTIAL_LINK_TEXT,  "Vimal Daga - LinuxWorld Informatics Pvt Ltd")  )
)

time.sleep(10)

link = driver.find_element( By.PARTIAL_LINK_TEXT,  "Vimal Daga - LinuxWorld Informatics Pvt Ltd")
link.click()


time.sleep(10)

driver.close()



