from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\paulo\chrome_automation_profile')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses/student/edit?courseid=phidalgo.uns-demo&studentemail=paulohidalgoch@gmail.com"
driver.get(url_edicion)
wait = WebDriverWait(driver, 15)
nombre = "//*[@id='student-name']"
submit = '//*[@id="btn-submit"]'
wait.until(EC.presence_of_element_located((By.XPATH, nombre)))

try:
    actions = ActionChains(driver)
    nombreField = driver.find_element(By.XPATH, nombre)
    submitBoton = driver.find_element(By.XPATH,submit)

    nombreField.clear()
    nombreField.click()
    actions.send_keys("a"*101).perform()

    submitBoton.click()


except Exception as e:
    print(f"Error detectado: {e}")


input("Presiona ENTER para cerrar el navegador...")
driver.quit()