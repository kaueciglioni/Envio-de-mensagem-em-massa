import pandas as pd

contatos_df = pd.read_excel("Contatos.xlsx") 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib3

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib3.parse.quote(f"Oi, {pessoa}! {mensagem}")
    link = f"https>//web.whatsapp.com/send?phone={'numero'}&text={'texto'}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_kes(Keys.ENTER)
    time.sleep(10)
