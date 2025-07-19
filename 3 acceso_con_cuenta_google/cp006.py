from selenium import webdriver
#este script se creo previamente a la creacion de la cuenta con el correo paulohidalgoch@gmail.com
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\paulo\cuenta_desconocida')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
url_edicion = "https://teammates-escarabajo-462900.uc.r.appspot.com/web/student/home"
driver.get(url_edicion) 

input("Presiona ENTER para cerrar el navegador...")
driver.quit()