from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

add = webdriver.ChromeOptions()
add.add_argument(r'user-data-dir=C:\Users\paulo\chrome_automation_profile')
driver = webdriver.Chrome(options=add)
driver.maximize_window()
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/courses/edit?courseid=phidalgo.uns-demo"
driver.get(url_edicion)
wait = WebDriverWait(driver, 15)


try:
    add = '//*[@id="btn-add-instructor"]'
    wait.until(EC.presence_of_element_located((By.XPATH, add)))
    driver.find_element(By.XPATH, add).click()

    nombre = '//*[@id="name-instructor-2"]'
    wait.until(EC.presence_of_element_located((By.XPATH, nombre)))
    nombInp = driver.find_element(By.XPATH, nombre)
    nombInp.click()
    nombInp.send_keys("Paulo Hidalgo")
    
    email = '//*[@id="email-instructor-2"]'
    wait.until(EC.presence_of_element_located((By.XPATH, email)))
    emInp = driver.find_element(By.XPATH, email)
    emInp.click()
    emInp.send_keys("paulohidalgoch@gmail.com")

    save = '//*[@id="btn-save-instructor-2"]'
    wait.until(EC.presence_of_element_located((By.XPATH, save)))
    driver.find_element(By.XPATH, save).click()


except Exception as e:
    print(f"Error detectado: {e}")


input("Presiona ENTER para cerrar el navegador...")
driver.quit()