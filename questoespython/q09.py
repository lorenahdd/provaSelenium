#utilizei como exemplo o site da drogasil e o alerta de utilização de cookies

from selenium import webdriver 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


navegador.get('https://www.drogasil.com.br/')
time.sleep(10) #espera a página carregar
navegador.find_element(By.XPATH, ('//*[@id="onetrust-reject-all-handler"]')).click() #rejeitar cookies

