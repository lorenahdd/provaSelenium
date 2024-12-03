from selenium import webdriver 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

navegador.get("https://the-internet.herokuapp.com/login")
user = navegador.find_element(By.ID, ("username"))
user.click()
user.send_keys("tomsmith")

senha = navegador.find_element(By.ID, ("password"))
senha.click()
senha.send_keys("SuperSecretPassword!")

navegador.find_element(By.XPATH, ("/html/body/div[2]/div/div/form/button/i")).click()

sucesso = navegador.find_element(By.ID, ("flash")).text

if "You logged into a secure area!" in sucesso:
    print("entrouuu parabens")
else: 
    print("eita algo deu errado")
