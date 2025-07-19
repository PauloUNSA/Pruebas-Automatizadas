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
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses/enroll?courseid=phidalgo.uns-demo"
driver.get(url_edicion) 
#time.sleep(3)
wait = WebDriverWait(driver, 15)  # espera hasta 15 segundos
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="newStudentsHOT"]/div[1]/div/div/div/table/tbody/tr[1]/td[1]')))


try:
    actions = ActionChains(driver)
    seccion = driver.find_element(By.XPATH, '//*[@id="newStudentsHOT"]/div[1]/div/div/div/table/tbody/tr[1]/td[1]')
    equipo = driver.find_element(By.XPATH, '//*[@id="newStudentsHOT"]/div[1]/div/div/div/table/tbody/tr[1]/td[2]')
    nombre = driver.find_element(By.XPATH, '//*[@id="newStudentsHOT"]/div[1]/div/div/div/table/tbody/tr[1]/td[3]')
    correo = driver.find_element(By.XPATH, '//*[@id="newStudentsHOT"]/div[1]/div/div/div/table/tbody/tr[1]/td[4]')
    comentarios = driver.find_element(By.XPATH, '//*[@id="newStudentsHOT"]/div[1]/div/div/div/table/tbody/tr[1]/td[5]')

    seccion.click()
    actions.send_keys("A").perform()
    
    equipo.click()
    actions.send_keys("Grupo 1").perform()
    
    nombre.click()
    actions.send_keys("Nombre Apellido").perform()
    
    correo.click()
    #actions.send_keys("persona23com12").perform()
    actions.send_keys("paulohidalgoch@gmail.com").perform()

    submit = driver.find_element(By.XPATH, '//*[@id="btn-enroll"]')
    submit.click()


except Exception as e:
    print(f"Error detectado: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()