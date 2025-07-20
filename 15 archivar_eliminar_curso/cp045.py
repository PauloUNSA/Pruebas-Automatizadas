from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\paulo\chrome_automation_profile')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
#vera la unica pregunta existente, y su respectiva respuesta, que el mismo dio
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses"
driver.get(url_edicion)
wait = WebDriverWait(driver, 15)


try:
    options = '//*[@id="btn-other-actions-0"]'
    wait.until(EC.presence_of_element_located((By.XPATH, options)))
    driver.find_element(By.XPATH, options).click()

    delete = '//*[@id="btn-soft-delete-0"]'
    wait.until(EC.presence_of_element_located((By.XPATH, delete)))
    driver.find_element(By.XPATH, delete).click()
    
    confirm = '/html/body/ngb-modal-window/div/div/tm-confirmation-modal/div[4]/button[2]'
    wait.until(EC.presence_of_element_located((By.XPATH, confirm)))
    driver.find_element(By.XPATH, confirm).click()


except Exception as e:
    print(f"Error detectado: {e}")


input("Presiona ENTER para cerrar el navegador...")
driver.quit()