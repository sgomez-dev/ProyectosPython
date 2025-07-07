from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Opciones de Chrome
options = Options()
options.add_argument("--start-maximized")

# El driver se descarga y gestiona automáticamente
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Abrir tu app
driver.get("http://localhost:4200/auth/register")
time.sleep(3)

# Localizar campos
name_field = driver.find_element(By.ID, "name")
last_name_field = driver.find_element(By.ID, "lastName")
email_field = driver.find_element(By.ID, "email")
pass_field = driver.find_element(By.ID, "pass")
conf_pass_field = driver.find_element(By.ID, "confPass")

name_field.send_keys("Santiago")
last_name_field.send_keys("Gómez")
email_field.send_keys("santiago@sgomez.dev")
pass_field.send_keys("........")
conf_pass_field.send_keys("........")

register_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Registrar')]")
register_button.click()

time.sleep(15)

