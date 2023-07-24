import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.kabum.com.br/ofertas/ofertadodia")

if page.status_code == 200:
    arq = open("kabum_ofertas.txt", "w")
    soup = BeautifulSoup(page.text, "html.parser")

    for produto in soup.find_all("div", class_="sc-d55b419d-7 ffpHYT productCard"):
        nome = produto.find_all("span", class_="sc-89c457ac-0 jKSmuI sc-d55b419d-16 fMikXK nameCard")
        link = produto.find_all("a", class_="sc-d55b419d-10 izMLCN productLink")
        preco = produto.find_all("span", class_="sc-3b515ca1-2 gybgF priceCard")

        i = 0
        print(nome[i].text)
        print("https://www.kabum.com.br%s" % (link[i].get("href", "")))
        print(preco[i].text, "\n")
        texto = "%s \nwww.kabum.com.br%s \n%s \n\n" % (nome[i].text, link[i].get("href", ""), preco[i].text)
        arq.write(texto)
        i += 1
    arq.close()

else:
    print("HTTP error ", page.status_code)

#import pdb; pdb.set_trace()