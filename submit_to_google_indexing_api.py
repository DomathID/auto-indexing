import os
import requests
import xml.etree.ElementTree as ET
from google.oauth2 import service_account
from googleapiclient.discovery import build

# URL of your sitemap
SITEMAP_URL = "https://www.yukinoshita.web.id/sitemap.xml"

# Load service account credentials
credentials = service_account.Credentials.from_service_account_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/indexing']
)

# Build the service
service = build('indexing', 'v3', credentials=credentials)

# Function to fetch and parse sitemap
def fetch_sitemap(url):
    response = requests.get(url)
    response.raise_for_status()
    sitemap = ET.fromstring(response.content)
    urls = [element.text for element in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    return urls

# Function to publish a URL
def publish_url(url):
    body = {
        "url": url,
        "type": "URL_UPDATED"
    }
    service.urlNotifications().publish(body=body).execute()

# Fetch URLs from sitemap
urls = fetch_sitemap(SITEMAP_URL)

# Submit each URL
for url in urls:
    publish_url(url)
    print(f"Submitted {url} to Google Indexing API")
  import os
import requests
import xml.etree.ElementTree as ET
from google.oauth2 import service_account
from googleapiclient.discovery import build

# URL of your sitemap
SITEMAP_URL = "https://www.yukinoshita.web.id/sitemap.xml"

# Load service account credentials
credentials = service_account.Credentials.from_service_account_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/indexing']
)

# Build the service
service = build('indexing', 'v3', credentials=credentials)

# Function to fetch and parse sitemap
def fetch_sitemap(url):
    response = requests.get(url)
    response.raise_for_status()
    sitemap = ET.fromstring(response.content)
    urls = [element.text for element in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    return urls

# Function to publish a URL
def publish_url(url):
    body = {
        "url": url,
        "type": "URL_UPDATED"
    }
    service.urlNotifications().publish(body=body).execute()

# Fetch URLs from sitemap
urls = fetch_sitemap(SITEMAP_URL)

# Submit each URL
for url in urls:
    publish_url(url)
    print(f"Submitted {url} to Google Indexing API")
