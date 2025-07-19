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
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/join?key=7B19757DB9FA7354324DEB262865A33A6938C284E093DBCF872AD7B18A748CE1E41E14DEE2A7CD3DC275681F478FF2B1686D5D11EB7ECC1EAD11E84A077F87E7&entitytype=student"
driver.get(url_edicion) 

input("Presiona ENTER para cerrar el navegador...")
driver.quit()