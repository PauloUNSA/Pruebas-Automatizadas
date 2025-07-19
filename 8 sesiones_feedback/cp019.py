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
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions"
driver.get(url_edicion)
wait = WebDriverWait(driver, 15)
add = '//*[@id="btn-add-session"]'
wait.until(EC.presence_of_element_located((By.XPATH, add)))
time.sleep(1)

try:
    driver.find_element(By.XPATH, add).click()
    nombre = '//*[@id="add-session-name"]'
    wait.until(EC.presence_of_element_located((By.XPATH, nombre)))
    time.sleep(1)
    nomInp = driver.find_element(By.XPATH, nombre)
    nomInp.click()
    nomInp.send_keys("Sesión de Feedback")
    dateFin = '//*[@id="submission-end-date"]/tm-datepicker/div/button'
    wait.until(EC.presence_of_element_located((By.XPATH, dateFin)))
    driver.find_element(By.XPATH, dateFin).click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="submission-end-date"]/tm-datepicker/div/ngb-datepicker')))
    driver.find_element(By.XPATH, '//*[@id="submission-end-date"]/tm-datepicker/div/ngb-datepicker/div[2]/div/ngb-datepicker-month/div[5]/div[3]/div').click()
    driver.find_element(By.XPATH, '//*[@id="btn-change-email"]').click()
    time.sleep(1)
    desactivar = '//*[@id="email-closing"]'
    wait.until(EC.presence_of_element_located((By.XPATH, desactivar)))
    driver.find_element(By.XPATH, desactivar).click()
    confirmar = '//*[@id="btn-create-session"]'
    wait.until(EC.presence_of_element_located((By.XPATH, confirmar)))
    driver.find_element(By.XPATH, confirmar).click()

except Exception as e:
    print(f"Error detectado: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()