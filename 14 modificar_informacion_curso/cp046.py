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
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses/details?courseid=phidalgo.uns-demo"
driver.get(url_edicion)
WebDriverWait(driver, 10).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

time.sleep(2)
driver.execute_script("window.scrollBy(0, 1000);")

time.sleep(5)
wait = WebDriverWait(driver, 15)

url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses"
try:
    driver.get(url_edicion)
    show = '//*[@id="show-statistics-1"]'
    wait.until(EC.presence_of_element_located((By.XPATH, show)))
    driver.find_element(By.XPATH, show).click()

except Exception as e:
    print(f"Error detectado: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()