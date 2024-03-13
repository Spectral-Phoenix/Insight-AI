import requests
from bs4 import BeautifulSoup

def scrape_text(links):
    content_list = []
    for link in links:
        response = requests.get(link, timeout=4)
        soup = BeautifulSoup(response.content, 'lxml', from_encoding=response.encoding)
        
        # Remove script and style elements
        for element in soup(["script", "style"]):
            element.extract()
        
        # Get text content from relevant tags
        text = " ".join([elem.get_text(strip=True) for elem in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5'])])
        content_list.append(text)
    return content_list

def scrape(links):
    content_list = scrape_text(links)
    return "\n".join(content_list)