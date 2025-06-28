from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scrape_website(website_url):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')

    # Corrected line
    options.binary_location = "/usr/bin/chromium"

    # You are using ChromeDriverManager here instead of the fixed path
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(website_url)
        driver.save_screenshot('screenshot.png')
        page_source = driver.page_source
        return page_source
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        driver.quit()

def extract_body_content(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    body_content = soup.find('body')
    return str(body_content) if body_content else ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    for tag in soup(['script', 'style']):
        tag.decompose()
    lines = soup.get_text(separator='\n', strip=True).splitlines()
    return '\n'.join(line.strip() for line in lines if line.strip())

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]
