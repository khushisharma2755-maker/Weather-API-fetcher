import requests
from bs4 import BeautifulSoup

def web_scraper(url):
    """
    Scrapes the given website, prints its title, paragraphs, and links.
    
    Args:
    url (str): URL of the website to scrape.
    """
    try:
        # Ensure the URL starts with http:// or https://
        if not (url.startswith('http://') or url.startswith('https://')):
            url = 'http://' + url
        
        response = requests.get(url, timeout=10)  # Added a timeout
        response.raise_for_status()  # check for HTTP errors
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Print page title
        print("Page Title:", soup.title.string if soup.title else "No title found")
        
        # Print paragraphs
        print("\nParagraphs:")
        for p in soup.find_all("p"):
            print(p.get_text())
        
        # Print links
        print("\nLinks:")
        for link in soup.find_all("a"):
            href = link.get("href")
            print(href if href else "No link found")
            
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection Error: {conn_err}")
    except requests.exceptions.Timeout as time_err:
        print(f"Timeout Error: {time_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    website = input("Enter website URL: ")
    web_scraper(website)

if _name_ == "_main_":
    main()

