#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

#Este script va a comprobar cuales de las prácticas que son subidas a https://www.etsi.us.es/movilidad_practicas/ofertas_practicas
#pueden interesarme, imprimiendo los enlaces nuevos en la consola para poder acceder a ellos con un click.


url = requests.get('https://www.etsi.us.es/movilidad_practicas/ofertas_practicas')
soup = BeautifulSoup(url.content, 'html.parser')

#Lista de oferta de prácticas de la primera página. Sólo voy a comprobar las ofertas más recientes (las de la primera página).
practicas = soup.find_all('td', class_='movilidad_columna_oferta')

for link in practicas:
    #Esta línea permite trabajar con los contenidos de cada enlace a cada página de prácticas 
    soup2 = BeautifulSoup(requests.get('https://www.etsi.us.es' + link.a.get('href')).content , 'html.parser')

    #Busco que en el texto aparezcan SEVILLA y TELECO para asegurarme de que la práctica es para mi titulación y dentro de la ciudad.
    texto = soup2.get_text()
    if 'TELECO' in texto:
        if 'SEVILLA' in texto:
            #Aparecerá en pantalla el enlace a la práctica
            print('https://www.etsi.us.es' + link.a.get('href'))



