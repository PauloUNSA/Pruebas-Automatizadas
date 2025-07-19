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
# Esperar hasta que la primera celda esté visible
wait = WebDriverWait(driver, 15)  # espera hasta 15 segundos
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="newStudentsHOT"]/div[1]/div/div/div/table/tbody/tr[1]/td[1]')))


try:
    actions = ActionChains(driver)
    #seccion,equipo,nombre,correo,comentarios
    # Encuentra la celda
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
    actions.send_keys("Paulo Hidalgo").perform()
    
    correo.click()
    actions.send_keys("paulohidalgoch@gmail.com").perform()

    comentarios.click()
    actions.send_keys("Cuenta Personal").perform()

    submit = driver.find_element(By.XPATH, '//*[@id="btn-enroll"]')
    submit.click()


except Exception as e:
    print(f"Error detectado: {e}")

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="results-panel"]/h1')))

time.sleep(0.5)  # Espera para que se procese la inscripción
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses/details?courseid=phidalgo.uns-demo"
driver.get(url_edicion) 
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-send-invite-phidalgo.uns-demo-1"]')))


try:
    actions = ActionChains(driver)
    enviar_invitacion = driver.find_element(By.XPATH, '//*[@id="btn-send-invite-phidalgo.uns-demo-1"]')
    enviar_invitacion.click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/ngb-modal-window/div/div/tm-confirmation-modal/div[4]/button[2]'))).click()
    confirmar = driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/tm-confirmation-modal/div[4]/button[2]')
    confirmar.click()
    
except Exception as e:
    print(f"Error detectado: {e}")
input("Presiona ENTER para cerrar el navegador...")
driver.quit()