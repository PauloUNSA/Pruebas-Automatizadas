from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\paulo\chrome_automation_profile')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses/student/edit?courseid=phidalgo.uns-demo&studentemail=paulohidalgoch@gmail.com"
driver.get(url_edicion)
wait = WebDriverWait(driver, 15)

try:
    seccion = '//*[@id="section-name"]'
    wait.until(EC.presence_of_element_located((By.XPATH, seccion)))
    seccionField = driver.find_element(By.XPATH, seccion)
    seccionField.clear()
    seccionField.click()
    seccionField.send_keys("C")
    
    grupo = '//*[@id="team-name"]'
    wait.until(EC.presence_of_element_located((By.XPATH, grupo)))
    grupoField = driver.find_element(By.XPATH, grupo)
    grupoField.clear()
    grupoField.click()
    grupoField.send_keys("Grupo 2")
    
    submit = '//*[@id="btn-submit"]'
    submitBoton = driver.find_element(By.XPATH,submit)
    submitBoton.click()
    
    confirmar = '/html/body/ngb-modal-window/div/div/tm-confirmation-modal/div[4]/button[2]'
    wait.until(EC.presence_of_element_located((By.XPATH, confirmar)))
    driver.find_element(By.XPATH, confirmar).click()


except Exception as e:
    print(f"Error detectado: {e}")


input("Presiona ENTER para cerrar el navegador...")
driver.quit()