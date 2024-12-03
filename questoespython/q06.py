from selenium import webdriver 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
navegador.get("https://www.google.com.")
procurar = navegador.find_element(By.XPATH, '//*[@id="APjFqb"]')
procurar.click()
procurar.send_keys("Python Selenium")
procurar.send_keys(Keys.ENTER)

time.sleep(5)


navegador.save_screenshot("resultado.png")