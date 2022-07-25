# Libs necessárias: selenium, pandas
# Chromedriver download: https://chromedriver.chromium.org/downloads
# O download do chrome driver deve ser referente à versão do google chrome no computador
# A versão que está sendo utilizada é a 103.0.5060.134

#chamando libs
from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

"""Configuração para remover erro de dispositivo bluetooth"""
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
"""======================================================="""

#Caminho do excel para white list
path_white_list = ("C:\Python\BotUnfollowInstagram\white_list.xlsx")

#lendo excel e guardando os dados na variável white_list
white_list = pd.read_excel(path_white_list, index_col=0).index.array

#iniciando chromedriver adicionando options e indicando caminho do chromedriver
driver = webdriver.Chrome(options=options,executable_path='chromedriver')

#realizando request para o site desejado
driver.get("https://www.instagram.com")

#sleep sendo utilizado para dar o tempo de carregar a página
sleep(4)
#inserindo login no elemento HTML de input para login
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("testewendelg")

#inserindo senha no elemento HTML de input para senha
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("Jamanta2410")

#realizando click no botão de submit
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
sleep(4)

#Click no botão de opções do usuário do instagram
driver.find_element(By.XPATH,"//nav/div/div/div/div/div/div/div/span").click()
sleep(1)
#Click no botão do perfil do usuário do instagram
driver.find_element(By.XPATH,"//nav/div/div/div/div/div/div/div/div/div/a").click()
sleep(4)
#Click no botão "Seguindo" no perfil do usuário
following = driver.find_element(By.PARTIAL_LINK_TEXT,"following")
following.click()
sleep(5)

#Recuperando nome do perfil de todos usuário que estão sendo seguidos
text_contents = [el.text for el in driver.find_elements(By.XPATH,"//ul/div/li/div/div/div/div/div/span/a")]

#Laço de repetição para entrar no perfil de cada um dos perfis seguidos
for text in text_contents:
    if any(nome in text for nome in white_list):
        continue
    driver.get("https://www.instagram.com/" + text + "/")
    sleep(4) 
    if driver.find_element(By.XPATH,'//button[@class="_acan _acap _acat"]'):
        print("\nOK\n")
    sleep(6)
