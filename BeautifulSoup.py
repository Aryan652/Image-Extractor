import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download image, status code: {response.status_code}")

def extract_image_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = []
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if not img_url.startswith('http'):
            print(f'before joining : {img_url}')
            img_url = urljoin(url, img_url)
            print(f'after joining : {img_url}')
        images.append(img_url)
    return images

url = "https://www.google.com"
file_name = "downloaded_image.jpg"

image_links = extract_image_links(url)
if image_links:
    download_image(image_links[0], file_name)
else:
    print("No images found on the webpage.")
