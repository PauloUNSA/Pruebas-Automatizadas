from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

add = webdriver.ChromeOptions()
add.add_argument(r'user-data-dir=C:\Users\paulo\chrome_automation_profile')
driver = webdriver.Chrome(options=add)
driver.maximize_window()
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/students"
driver.get(url_edicion)
wait = WebDriverWait(driver, 15)

try:
    labDropdown = '//*[@id="main-content"]/div/tm-instructor-student-list-page/tm-loading-retry/div[3]/div/div/div/tm-panel-chevron/button'
    wait.until(EC.presence_of_element_located((By.XPATH, labDropdown)))
    dropdown = driver.find_element(By.XPATH, labDropdown)
    dropdown.click()
    
except Exception as e:
    print(f"Error detectado: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()