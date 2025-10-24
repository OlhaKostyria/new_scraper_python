import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
title_spans = soup.find_all("span", class_="titleline")

print(f"Найдено заголовков: {len(title_spans)}")

with open("headlines.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])
    for span in title_spans:
        a_tag = span.find("a")
        if a_tag:
            title = a_tag.get_text(strip=True)
            link = a_tag.get("href")
            writer.writerow([title, link])

print("Done! Check headlines.csv")
