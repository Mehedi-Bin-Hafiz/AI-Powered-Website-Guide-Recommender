import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin
import re

# Global variable to store cache
cache = {
    "date": None,  # To store the date of the last run
    "data": None  # To store the scraped data
}


def clean_text(text):
    # Remove all punctuation
    text = re.sub(r'[^\w\s]', '', text)  # Remove any character that is not a word character or whitespace

    # Remove extra spaces and newlines
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces or newlines with a single space
    text = text.strip()  # Remove leading and trailing spaces

    return text


def scrape_links_and_text(url):
    # Send an HTTP request to the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to access {url}")
        return []

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags with 'href' attribute
    links_and_texts = []
    for a_tag in soup.find_all('a', href=True):
        relative_link = a_tag['href']  # Extract the raw link
        link = urljoin(url, relative_link)  # Convert to absolute URL
        text = a_tag.get_text(strip=True)  # Extract the text within the link

        # Clean the text before appending
        cleaned_text = clean_text(text)

        # Check if the link is valid (starts with 'http' or 'https') and has cleaned text
        if link.startswith(('http://', 'https://')) and cleaned_text:
            links_and_texts.append({'link': link, 'text': cleaned_text})

    return links_and_texts


def daily_scraper(url):
    global cache
    today = datetime.now().date()  # Get today's date

    # Check if the cache has already been updated for today's date
    if cache["date"] == today:
        print("Using cached data...")
        return cache["data"]

    # If the date has changed, reset the cache and fetch new data
    print("Scraping fresh data...")
    cache = {"date": today, "data": scrape_links_and_text(url)}

    return cache["data"]


# Example Usage
url = 'https://aladaboi.com'

# First call - Scrapes fresh data
data = daily_scraper(url)
# print(data)

print("First Call Output:")
for item in data:
    print(f"Link: {item['link']}, Text: {item['text']}")
#
# # Second call (on the same day) - Uses cached data
# data = daily_scraper(url)
# print("\nSecond Call Output:")
# for item in data:
#     print(f"Link: {item['link']}, Text: {item['text']}")
