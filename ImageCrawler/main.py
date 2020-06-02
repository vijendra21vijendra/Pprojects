# https://www.pexels.com/@hiteshchoudhary
#enumeration is way of iterating

# from bs4 import *
# import requests as rq
# import os

# r1 = rq.get("https://www.pexels.com/@hiteshchoudhary")
# soup1 = BeautifulSoup(r1.text,"html.parser")
# links = []
# x = soup1.select('img[src^="https://images.pexels.com/photos"]')
# for imlink in x:
# 	links.append(imlink['src'])

# # for l in links:
# # 	print(l)

# # print(soup1.prettify())

# os.mkdir("WebImages")
# i=1
# for index, img_link in enumerate(links):
# 	if i <=10:
# 		img_data = rq.get(img_link).content
# 		with open("WebImages/"+str(index+1)+".jpg","wb+") as f:
# 			f.write(img_data)
# 		i+=1
# 	else:
# 		break


# from bs4 import *
# import requests
# import os
# r1 = requests.get("https://www.pexels.com/@hiteshchoudhary")
# soup1 = BeautifulSoup(r1.text,"html.parser")
# soup1.prettify();
# print(soup1)
# x = soup1.select('h1');
# print(x)

# https://www.pexels.com/search/wine/

from bs4 import BeautifulSoup
import requests as req
import os

r1 = req.get("https://www.google.com/search?q=oxford+university&sxsrf=ALeKk01nNEkzqmOwgYU9128qNLldF7Z-QA:1591064667765&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjBwNjiieLpAhVyyDgGHUq8BMkQ_AUoAnoECBwQBA&biw=1366&bih=667")
soup = BeautifulSoup(r1.text,"html.parser")
# print(soup.prettify())
# print(soup.select('img'))
# print(soup.select('div'))
image_links = [] # empty list to store all image links
links = soup.select('img[src^="https://"]')
for imlink in links:
	image_links.append(imlink['src'])

# print(image_links)
os.mkdir("oxford")

for index, img_link in enumerate(image_links):
	if index<=20:
		img_data = req.get(img_link).content
		with open("oxford/"+str(index+100)+".jpg","wb+") as f:
			f.write(img_data)
	else:
		f.close()
		break

print("*****done*****")
