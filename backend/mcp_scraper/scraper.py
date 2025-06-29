import requests
from bs4 import BeautifulSoup

def scrape_cves(limit=5):
    url = "https://www.cvedetails.com/vulnerability-list/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.select("table.searchresults tr.srrowns")
    cves = []

    for row in rows[:limit]:
        cols = row.find_all("td")
        cve_id = cols[1].text.strip()
        description = cols[4].text.strip()
        cves.append({
            "cve_id": cve_id,
            "description": description
        })

    return cves

