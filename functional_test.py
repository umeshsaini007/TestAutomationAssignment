from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)

driver.get("https://demo.dealsdray.com/")
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("prexo.mis@dealsdray.com")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("prexo.mis@dealsdray.com")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

order_button = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div[1]/div/div[2]/div[1]/div[2]/button")))

order_button.click()
# driver.find_element(By.CLASS_NAME,"MuiButtonBase-root has-submenu compactNavItem css-46up3a").click()
driver.find_element(By.XPATH,"(//button[@name='child'])[2]").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Add Bulk Orders']").click()

file_uploader = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='mui-7']")))
file_uploader.send_keys("D://Test Automation Assignment/demo-data.xlsx")

driver.find_element(By.XPATH,"//button[normalize-space()='Import']").click()

validate_data = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Validate Data']")))
validate_data.click()
alert_message = wait.until(EC.alert_is_present())

driver.switch_to.alert.accept()
time.sleep(2)

driver.save_screenshot("screenshot_of_data.png")

driver.quit()