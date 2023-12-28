from bs4 import BeautifulSoup as bs
import urllib.request
from urllib.parse import urljoin
import requests

url = 'https://www.google.com/'

# Extracting url for scrapping

response = urllib.request.urlopen(url)
soup = bs(response,'html.parser')
image = []
for img in soup.find_all('img'):
    img_url = img.get('src')
    if not img_url.startswith('http://'):
        img_url = urljoin(url, img_url)
        print(img_url)
    image.append(img_url)

print(image)


# Downloading image to the local file
i = 1
for imga in image:
    download = requests.get(imga)
    if download.status_code == 200:
         
         name = 'ima'+ str(i) +'.jpg'
         
         print(name)
         with open(name, 'wb') as f:
             f.write(download.content)
         i = i+1