import requests
from bs4 import BeautifulSoup
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import TAVILY_TARGET_WEBSITES, TAVILY_CRAWL_DEPTH, DATA_STORAGE_PATH

def crawl_website(url, depth, max_depth):
    if depth > max_depth:
        return []

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text content
        texts = soup.stripped_strings
        content = ' '.join(texts)

        # Find links to crawl further
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('http'):
                links.append(href)

        data = [{
            'url': url,
            'content': content
        }]

        # Crawl links recursively
        for link_url in links[:5]:  # limit to first 5 links to avoid explosion
            data.extend(crawl_website(link_url, depth + 1, max_depth))

        return data
    except Exception as e:
        print(f"Failed to crawl {url}: {e}")
        return []

def run_research_agent():
    """
    Entry point for the Research Agent.
    Crawls target websites and collects data.
    """
    all_data = []
    max_depth = TAVILY_CRAWL_DEPTH

    for website in TAVILY_TARGET_WEBSITES:
        print(f"Crawling website: {website} with depth {max_depth}")
        data = crawl_website(website, 0, max_depth)
        all_data.extend(data)

    # Ensure data directory exists
    os.makedirs(DATA_STORAGE_PATH, exist_ok=True)
    output_file = os.path.join(DATA_STORAGE_PATH, 'collected_data.json')

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=2)

    print(f"Collected data saved to {output_file}")

if __name__ == "__main__":
    run_research_agent()
