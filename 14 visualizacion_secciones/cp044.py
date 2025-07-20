from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

add = webdriver.ChromeOptions()
add.add_argument(r'user-data-dir=C:\Users\paulo\chrome_automation_profile')
driver = webdriver.Chrome(options=add)
driver.maximize_window()
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/search"
driver.get(url_edicion)
wait = WebDriverWait(driver, 15)

try:
    search = '//*[@id="search-keyword"]'
    wait.until(EC.presence_of_element_located((By.XPATH, search)))
    searchBar = driver.find_element(By.XPATH, search)
    searchBar.click()
    searchBar.send_keys("Grupo 1")
    bot = '//*[@id="btn-search"]'
    wait.until(EC.element_to_be_clickable((By.XPATH, bot)))
    searchButton = driver.find_element(By.XPATH, bot)
    searchButton.click()
except Exception as e:
    print(f"Error detectado: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()