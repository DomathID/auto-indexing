import os
import requests
import xml.etree.ElementTree as ET
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime

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
    urls = []
    for element in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
        loc = element.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
        lastmod = element.find("{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod").text
        urls.append((loc, lastmod))
    urls.sort(key=lambda x: x[1], reverse=True)
    return [url[0] for url in urls]

# Function to publish a URL with type URL_UPDATED
def publish_url(url):
    body = {
        "url": url,
        "type": "URL_UPDATED"
    }
    service.urlNotifications().publish(body=body).execute()

# Fetch URLs from sitemap
urls = fetch_sitemap(SITEMAP_URL)

# Select the most recently updated URL
selected_url = urls[0]

# Submit the selected URL
publish_url(selected_url)
print(f"Submitted {selected_url} to Google Indexing API")

# Update README.md or updated.md with the submitted URL and timestamp
timestamp = datetime.utcnow().isoformat()
with open("updated.md", "a") as file:
    file.write(f"Submitted URL: {selected_url} at {timestamp} UTC\n")
    
