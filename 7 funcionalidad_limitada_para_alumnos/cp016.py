from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\paulo\cuenta_desconocida')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/edit?courseid=phidalgo.uns-demo&fsname=Second%20team%20feedback%20session%20(point-based)&editingMode=true"
driver.get(url_edicion)
wait = WebDriverWait(driver, 15)
esperar = '//*[@id="main-content"]/div/tm-instructor-session-edit-page/tm-loading-retry[1]/div/button'
wait.until(EC.presence_of_element_located((By.XPATH, esperar)))

input("Presiona ENTER para cerrar el navegador...")
driver.quit()