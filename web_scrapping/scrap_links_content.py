import requests
from bs4 import BeautifulSoup
import re

def scrape_text_from_url(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'lxml')

        # Extract all text
        page_text = soup.get_text(separator=' ')

        # Remove extra spaces
        cleaned_text = re.sub(r'\s+', ' ', page_text)

        return cleaned_text.strip()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

# Example usage
url = "https://daffodilvarsity.edu.bd/admission"
text = scrape_text_from_url(url)
if text:
    print("Extracted Text:")
    print(text)
