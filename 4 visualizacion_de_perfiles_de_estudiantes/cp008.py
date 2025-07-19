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
url = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses/student/details?courseid=phidalgo.uns-demo&studentemail=phidalgo@unsa.edu.pe"

driver.get(url)

input("Presiona ENTER para cerrar el navegador...")
driver.quit()