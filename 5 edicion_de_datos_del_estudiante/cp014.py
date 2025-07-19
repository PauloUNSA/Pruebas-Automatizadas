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
comentarios = "//*[@id='comments']"
submit = '//*[@id="btn-submit"]'
wait.until(EC.presence_of_element_located((By.XPATH, comentarios)))

try:
    actions = ActionChains(driver)
    #seccion,equipo,nombre,correo,comentarios
    # Encuentra la celda
    comField = driver.find_element(By.XPATH, comentarios)
    submitBoton = driver.find_element(By.XPATH,submit)
    
    comField.clear()
    comField.click()
    actions.send_keys("NUevo comentario").perform()

    submitBoton.click()


except Exception as e:
    print(f"Error detectado: {e}")

driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses/student/details?courseid=phidalgo.uns-demo&studentemail=paulohidalgoch@gmail.com")
input("Presiona ENTER para cerrar el navegador...")
driver.quit()