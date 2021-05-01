import requests
import pandas as pd
from bs4 import BeautifulSoup

baseurl = "https://mynasastore.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

productlinks = []
t = {}
data = []
c = 0 

# Obtener el link para cada producto
for x in range(1,8):
    # Hacer un request de la pagina
    k = requests.get('https://mynasastore.com/collections/womens?page={}'.format(x)).text
    soup = BeautifulSoup(k, 'html.parser')
    productlist = soup.find_all("div",{"grid__item grid-product medium--one-half large--one-third"})

    # acceder al href de la etiqueta <a>
    for product in productlist:
        link = product.find("a", {"grid-product__meta"}).get('href')
        productlinks.append(baseurl + link)

# Obtener el titulo del producto y el precio
for link in productlinks:
    f = requests.get(link, headers=headers).text
    hun = BeautifulSoup(f, 'html.parser')

    try:
        title=hun.find("h1", {"class":"product-single__title"}).text.replace('\n',"")
    except:
        title=None

    try:
        price=hun.find("span", {"class":"product-single__price"}).text.replace('\n',"")
    except:
        price=None
    

    # Guardar los datos en un diccionario
    clothe = {"Title":title, "Price":price}
    data.append(clothe)
    c = c + 1
    print("Completed", c)

#Crear un DataFrame
df = pd.DataFrame(data)
print(df)
