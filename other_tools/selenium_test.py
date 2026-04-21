# from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org/")

search_field = driver.find_element(By.ID, "id-search-field")
search_field.click()
search_field.send_keys("comprehension")
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

# DO NOT USE IT
# sleep(10)

wait = WebDriverWait(driver, 10)
result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".list-recent-events li:first-child")))
print(result.text)
