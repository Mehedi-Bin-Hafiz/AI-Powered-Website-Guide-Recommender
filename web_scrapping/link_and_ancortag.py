import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
from tqdm import  tqdm


def clean_text(text):
    # Remove all punctuation
    text = re.sub(r'[^\w\s]', '', text)  # Remove any character that is not a word character or whitespace

    # Remove extra spaces and newlines
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces or newlines with a single space
    text = text.strip()  # Remove leading and trailing spaces

    return text

def scrape_links_and_text(url):
    # Send an HTTP request to the URL
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to access {url}: {e}")
        return []

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags with 'href' attribute
    links_and_texts = []
    for a_tag in soup.find_all('a', href=True):
        # animation no need this code
        relative_link = a_tag['href']  # Extract the raw link
        link = urljoin(url, relative_link)  # Convert to absolute URL
        text = a_tag.get_text(strip=True)  # Extract the text within the link

        # Clean the text before appending
        cleaned_text = clean_text(text)

        # Check if the link is valid (starts with 'http' or 'https') and has cleaned text
        if link.startswith(('http://', 'https://')) and cleaned_text:
            links_and_texts.append({'link': link, 'text': cleaned_text})
    return links_and_texts


# Example Usage
url = 'https://daffodilvarsity.edu.bd/'
links_data = scrape_links_and_text(url)

for item in links_data:
    print(f"Link: {item['link']}, Text: {item['text']}")

