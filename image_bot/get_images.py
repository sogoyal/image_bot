# image scraping

import requests
from bs4 import BeautifulSoup as bs
import os
from PIL import Image

# website with pictures of bridges
url = 'https://picjumbo.com/search/bridge'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for images
if not os.path.exists('images'):
    os.makedirs('images')

# move to new directory
os.chdir('images')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            filepath = 'image_' + str(x) + '.png'
            with open(filepath, 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                
                #open with the images library to resize
                im = Image.open(filepath)
                width, height = im.size
                if (width > height):
                    newsize = (2048, (height*2048)/width)
                elif (width <= height):
                    newsize = ((width*2048)/height, 2048)
                im = im.resize(newsize)
                im = im.save(filepath)
                
                x += 1
    except:
        pass
