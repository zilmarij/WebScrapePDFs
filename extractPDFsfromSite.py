from bs4 import BeautifulSoup as bs
import requests
import re
from PyPDF2 import PdfReader
import os


url = "https://arxiv.org/list/cs.AR/recent"
page = requests.get(url)
soup = bs(page.content, 'html.parser')
# print(soup.prettify())

links = soup.find_all('a',href=re.compile("pdf"))
# print(links)

list_of_pdf = []
for pdf in links:
    href = pdf.get('href')
    href= "https://arxiv.org"+href

    list_of_pdf.append(href)
    
# print(list_of_pdf)

# Function to download PDFs
def download_pdf(pdf_url, folder="pdfs"):
    os.makedirs(folder, exist_ok=True)  # Create folder if it doesn't exist
    pdf_name = os.path.join(folder, pdf_url.split("/")[-1])
    
    response = requests.get(pdf_url, stream=True)
    if response.status_code == 200:
        with open(pdf_name, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded: {pdf_name}")
    else:
        print(f"Failed to download: {pdf_url}")



# download_pdf(list_of_pdf[15])
for pdf_url in list_of_pdf:
        download_pdf(pdf_url)
        
