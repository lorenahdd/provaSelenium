from selenium import webdriver 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
navegador.get('https://www.selenium.dev/')
navegador.find_element(By.XPATH, ('/html/body/header/nav/div/ul/li[2]/a/span')).click()
time.sleep(7)
texto = navegador.find_element(By.ID, ("bindings")).text  #pesquisei h2 no inspecionar e apareceu esse id

print(texto)


