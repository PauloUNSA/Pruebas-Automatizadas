from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

add = webdriver.ChromeOptions()
add.add_argument(r'user-data-dir=C:\Users\paulo\chrome_automation_profile')
driver = webdriver.Chrome(options=add)
driver.maximize_window()
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses/details?courseid=ID001"
driver.get(url_edicion)
time.sleep(2)
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(5)
wait = WebDriverWait(driver, 15)

url2 = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses/enroll?courseid=ID001"
driver.get(url2)
try:
    #seccion,equipo,nombre,correo,comentarios
    # Encuentra la celda
    #                                        //*[@id="newStudentsHOT"]/div[1]/div/div/div/table/tbody/tr[1]/td[1]
    labSec = '//*[@id="newStudentsHOT"]/div[1]/div/div/div/table/tbody/tr[1]/td[1]'
    wait.until(EC.presence_of_element_located((By.XPATH, labSec)))
    seccion = driver.find_element(By.XPATH, labSec)
    equipo = driver.find_element(By.XPATH, '//*[@id="newStudentsHOT"]/div[1]/div/div/div/table/tbody/tr[1]/td[2]')
    nombre = driver.find_element(By.XPATH, '//*[@id="newStudentsHOT"]/div[1]/div/div/div/table/tbody/tr[1]/td[3]')
    correo = driver.find_element(By.XPATH, '//*[@id="newStudentsHOT"]/div[1]/div/div/div/table/tbody/tr[1]/td[4]')
    seccion.click()
    seccion.send_keys("C")

    equipo.click()
    equipo.send_keys("Grupo 4")

    nombre.click()
    nombre.send_keys("Nuevo Estudiante")

    correo.click()
    correo.send_keys("nuevo@gmail.com")


    submit = driver.find_element(By.XPATH, '//*[@id="btn-enroll"]')
    submit.click()
except Exception as e:
    print(f"Error detectado: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()