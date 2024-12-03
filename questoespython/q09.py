#utilizei como exemplo um site que tem um alerta de cookies

from selenium import webdriver 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
navegador.get('https://forbes.com.br')

navegador.execute_script("window.scrollTo(0, 500);")




