import requests
from bs4 import BeautifulSoup

def scrape_who_data(query):
    # Set the base URL for the WHO website
    base_url = "https://www.who.int"
    
    # Set the search URL for the WHO website
    search_url = f"{base_url}/search?query={query}&facet_content_type=Document"
    
    # Send a GET request to the search URL and parse the HTML response
    search_response = requests.get(search_url)
    search_soup = BeautifulSoup(search_response.text, "html.parser")
    
    # Find all links to CSV files in the search results
    csv_links = search_soup.select("a[href$='.csv']")
    
    # Download each CSV file
    for link in csv_links:
        csv_url = f"{base_url}{link['href']}"
        csv_response = requests.get(csv_url)
        
        # Save the CSV file to disk
        filename = link['href'].split("/")[-1]
        with open(filename, "w") as f:
            f.write(csv_response.text)

# Example usage: Scrape data for the "influenza" query
scrape_who_data("influenza")
