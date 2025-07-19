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
grupo = '//*[@id="team-name"]'
submit = '//*[@id="btn-submit"]'
confirmacion = '/html/body/ngb-modal-window/div/div/tm-confirmation-modal/div[4]/button[2]'
wait.until(EC.presence_of_element_located((By.XPATH, grupo)))

try:
    actions = ActionChains(driver)
    grupoField = driver.find_element(By.XPATH, grupo)
    submitBoton = driver.find_element(By.XPATH,submit)

    grupoField.clear()
    grupoField.click()
    actions.send_keys("Grupo 2").perform()

    submitBoton.click()
    wait.until(EC.presence_of_element_located((By.XPATH, confirmacion)))
    driver.find_element(By.XPATH, confirmacion).click()


except Exception as e:
    print(f"Error detectado: {e}")


input("Presiona ENTER para cerrar el navegador...")
driver.quit()