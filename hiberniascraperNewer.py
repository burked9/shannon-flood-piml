import requests
from bs4 import BeautifulSoup
import os

# Function to download an image from a URL
def download_image(url, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    response = requests.get(url)
    if response.status_code == 200:
        file_name = os.path.join(folder_path, url.split('/')[-1])
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download: {url}")

# URL of the website to scrape
website_url = 'https://www.bargehibernia.com/'

# Send a request to fetch the website content
response = requests.get(website_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all image tags
    img_tags = soup.find_all('img')
    
    # Extract the src attribute from each img tag
    img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]
    
    # Download each image
    for img_url in img_urls:
        # Handle relative URLs
        if img_url.startswith('/'):
            img_url = website_url + img_url[1:]
        download_image(img_url, 'downloaded_images')
else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")
