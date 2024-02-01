import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
page = driver.get("https://www.kabum.com.br/ofertas/ofertadodia?pagina=1")
time.sleep(10)

arq = open("kabum_ofertas.txt", "w")

for produto in driver.find_elements(By.CLASS_NAME, "productCard"):
    nome = produto.find_elements(By.CLASS_NAME, "nameCard")
    link = produto.find_elements(By.CLASS_NAME, "productLink")
    preco = produto.find_elements(By.CLASS_NAME, "priceCard")

    i = 0
    print(nome[i].text)
    print(link[i].get_attribute("href"))
    print(preco[i].text, "\n")
    texto = "%s \n%s\n%s \n\n" % (nome[i].text, link[i].get_attribute("href"), preco[i].text)
    arq.write(texto)
    i += 1
arq.close()
driver.quit()
