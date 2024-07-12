from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import random

def get_page_content(url, proxy=None):
    # Set up headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    if proxy:
        chrome_options.add_argument(f'--proxy-server={proxy}')

    driver = webdriver.Chrome(options=chrome_options)

    # Add random delay to mimic real user behavior
    delay = random.uniform(1, 3)
    time.sleep(delay)

    # Attempt to get the page
    try:
        driver.get(url)
        # Add another random delay after loading the page
        delay = random.uniform(1, 3)
        time.sleep(delay)
        
        # Get page source
        page_content = driver.page_source
    except Exception as e:
        print(f"Error fetching the URL: {e}")
        page_content = None

    driver.quit()
    return page_content

def scrape_text(url, proxy=None):
    page_content = get_page_content(url, proxy)
    
    if page_content is None:
        print("Failed to retrieve the page.")
        return
    
    soup = BeautifulSoup(page_content, 'html.parser')

    # Extract all text
    texts = soup.stripped_strings
    all_text = ' '.join(texts)

    # Save the text to a file
    file_name = 'phone_text.txt'
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(all_text)

    print(f"Text content saved to {file_name}")

if __name__ == "__main__":
    url = input("https://www.amazon.in/s?k=mobile+phone").strip()
    proxy = input("Enter the proxy (if required, else leave blank): ").strip()
    if proxy == "":
        proxy = None
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://www.amazon.in/s?k=mobile+phone" 
    scrape_text(url, proxy)
