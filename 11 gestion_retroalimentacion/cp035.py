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
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses?isAddNewCourse=true"
driver.get(url_edicion)
wait = WebDriverWait(driver, 15)


try:
    #ID del curso
    courseID = '//*[@id="course-id"]'
    wait.until(EC.presence_of_element_located((By.XPATH, courseID)))
    driver.find_element(By.XPATH, courseID).click()
    driver.find_element(By.XPATH, courseID).send_keys("ID002")

    name = '//*[@id="course-name"]'
    wait.until(EC.presence_of_element_located((By.XPATH, name)))
    nombre = driver.find_element(By.XPATH, name)
    nombre.click()
    nombre.send_keys("Nombre del curso con ID duplicado")
    nombre.send_keys(Keys.CONTROL + "a")  # Selecciona todo
    nombre.send_keys(Keys.BACKSPACE) 
    
    #-CONFIRMAR--
    confirmar = '//*[@id="btn-submit-course"]'
    wait.until(EC.presence_of_element_located((By.XPATH, confirmar)))
    driver.find_element(By.XPATH, confirmar).click()

except Exception as e:
    print(f"Error detectado: {e}")


input("Presiona ENTER para cerrar el navegador...")
driver.quit()