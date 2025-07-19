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
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/edit?courseid=phidalgo.uns-demo&fsname=First%20team%20feedback%20session%20(percentage-based)&editingMode=true"
driver.get(url_edicion)
wait = WebDriverWait(driver, 15)

try:
    colapsar= '//*[@id="btn-collapse-expand"]'
    wait.until(EC.presence_of_element_located((By.XPATH, colapsar)))
    colapsarBot = driver.find_element(By.XPATH, colapsar)
    colapsarBot.click()
    add = '//*[@id="btn-new-question"]'
    wait.until(EC.presence_of_element_located((By.XPATH, add)))
    driver.find_element(By.XPATH, add).click()
    easy = '//*[@id="new-question-dropdown"]/div[2]/div/button'
    wait.until(EC.presence_of_element_located((By.XPATH, easy)))
    driver.find_element(By.XPATH, easy).click()
    inp = '//*[@id="question-brief"]'
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.XPATH, inp)))
    driver.find_element(By.XPATH, inp).click()
    driver.find_element(By.XPATH, inp).send_keys("Pregunta de Feedback")
    #-----------FEEDBACK PATH-----------
    feedback = '//*[@id="btn-feedback-path"]'
    wait.until(EC.presence_of_element_located((By.XPATH, feedback)))
    driver.find_element(By.XPATH, feedback).click()
    #tipo
    tipo = '//*[@id="feedback-path-dropdown"]/li[4]/div/button'
    wait.until(EC.presence_of_element_located((By.XPATH, tipo)))
    driver.find_element(By.XPATH, tipo).click()
    #seleccion especifica
    seleccion = '//*[@id="feedback-path-dropdown"]/li[4]/ul/li[5]/button'
    wait.until(EC.presence_of_element_located((By.XPATH, seleccion)))
    driver.find_element(By.XPATH, seleccion).click()
    
    #-----------VISIBILIDAD-----------
    visibilidad = '//*[@id="btn-question-visibility"]'
    wait.until(EC.presence_of_element_located((By.XPATH, visibilidad)))
    driver.find_element(By.XPATH, visibilidad).click()
    #especifica
    especifica = '//*[@id="question-visibility-dropdown"]/li[5]/button'
    wait.until(EC.presence_of_element_located((By.XPATH, especifica)))
    driver.find_element(By.XPATH, especifica).click()
    #--CONFIRMAR--
    confirmar = '//*[@id="question-form-7"]/div/div/div[2]/div/button[2]'
    wait.until(EC.presence_of_element_located((By.XPATH, confirmar)))
    driver.find_element(By.XPATH, confirmar).click()

except Exception as e:
    print(f"Error detectado: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()