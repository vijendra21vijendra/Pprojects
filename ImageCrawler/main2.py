import requests
import os

im = requests.get("https://images.pexels.com/photos/3577561/pexels-photo-3577561.jpeg?auto=compress&amp;cs=tinysrgb&amp;h=750&amp;w=1260")
img = im.content
os.mkdir("WebImages")
with open("WebImages/"+str(1)+".jpg","wb+") as f:
			f.write(img)
