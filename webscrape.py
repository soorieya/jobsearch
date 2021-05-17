from bs4 import BeautifulSoup
import requests

def webscrape():
    url = "https://careers.a-star.edu.sg/JobListing.aspx?ID=1klk05BAWCprrKGx9yWbPaUcwy2W0Mi8Cf4PK16sIEngvAkC2kuIC6pWPVwlR5hNvudMzpPi5gjbv0iFLd1hGQ=="
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')
    return soup

