from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses/edit?courseid=ID001"
driver.get(url_edicion)
time.sleep(2)

input("Presiona ENTER para cerrar el navegador...")
driver.quit()