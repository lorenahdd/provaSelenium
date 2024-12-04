#fiz um scrip utilizando o webdriver

from selenium import webdriver 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
navegador.get('https://example.com')
tituloinicial = navegador.title
teste = navegador.find_element(By.XPATH, '/html/body/div/p[2]/a').click() #more information
titulofinal = navegador.title

if tituloinicial == titulofinal:
    print("mesmo titulo :)")
else:
    print("titulo mudou >:)")
