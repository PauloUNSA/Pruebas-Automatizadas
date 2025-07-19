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
#solo vera la pregunta 12, ya que las demás estan ocultas
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/student/sessions/result?courseid=paulohidalgoch.gma-demo&fsname=Session%20with%20different%20question%20types"
driver.get(url_edicion)


input("Presiona ENTER para cerrar el navegador...")
driver.quit()