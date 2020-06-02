# http://www.indianrajputs.com/pictures.php?category=Architecture
# http://i.indianrajputs.com/t/i/thumb200_ajitpura-Ajeetpura-Fort-1.jpg


import requests
from bs4 import BeautifulSoup
import os


res_ob = requests.get("http://www.indianrajputs.com/pictures.php?category=Architecture&page=1")
print(res_ob.text)
soup = BeautifulSoup(res_ob.text,"html.parser")
print(soup.prettify())
images_contents = soup.select('img[src^="http://i.indianrajputs.com/"]')

images_links = []

for img in images_contents:
	images_links.append(img['src'])

# print(images_links)


