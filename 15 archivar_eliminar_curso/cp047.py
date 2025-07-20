from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

expand = webdriver.ChromeOptions()
expand.add_argument(r'user-data-dir=C:\Users\paulo\chrome_automation_profile')
driver = webdriver.Chrome(options=expand)
driver.maximize_window()
#vera la unica pregunta existente, y su respectiva respuesta, que el mismo dio
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses"
driver.get(url_edicion)
wait = WebDriverWait(driver, 15)


try:
    expand = '//*[@id="deleted-table-heading"]/div/tm-panel-chevron/button'
    wait.until(EC.presence_of_element_located((By.XPATH, expand)))
    driver.find_element(By.XPATH, expand).click()
    time.sleep(2)
    restore = '//*[@id="btn-restore-0"]'
    wait.until(EC.presence_of_element_located((By.XPATH, restore)))
    res =driver.find_element(By.XPATH, restore)
    res.click()


except Exception as e:
    print(f"Error detectado: {e}")


input("Presiona ENTER para cerrar el navegador...")
driver.quit()