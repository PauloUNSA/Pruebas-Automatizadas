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
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses/edit?courseid=ID001"
driver.get(url_edicion)
wait = WebDriverWait(driver, 15)


try:
    courseID = '//*[@id="btn-edit-course"]'
    wait.until(EC.presence_of_element_located((By.XPATH, courseID)))
    driver.find_element(By.XPATH, courseID).click()

    name = '//*[@id="course-name"]'
    wait.until(EC.presence_of_element_located((By.XPATH, name)))
    nombre = driver.find_element(By.XPATH, name)
    nombre.click()
    
    nombre.send_keys(Keys.CONTROL + "a")  # Selecciona todo
    nombre.send_keys(Keys.BACKSPACE) 
    nombre.send_keys("Matemáticas")
    
    #-CONFIRMAR--
    confirmar = '//*[@id="btn-save-course"]'
    wait.until(EC.presence_of_element_located((By.XPATH, confirmar)))
    driver.find_element(By.XPATH, confirmar).click()

except Exception as e:
    print(f"Error detectado: {e}")


input("Presiona ENTER para cerrar el navegador...")
driver.quit()