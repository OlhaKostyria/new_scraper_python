# 📰 News Headlines Scraper

This is a simple Python script that scrapes news headlines from [Hacker News](https://news.ycombinator.com) and saves them to a CSV file.

## ✅ Features
- Extracts article titles from the homepage
- Saves the data to `headlines.csv`
- Uses `requests` and `BeautifulSoup4`
- Handles missing elements and errors
- Designed for beginners who want to practice web scraping

## 🛠 Requirements

Install the required libraries using pip:

```bash
pip install requests beautifulsoup4
▶️ How to Run

Run the script from terminal or command line:

python scraper.py


After running, you'll see a file called headlines.csv in the same directory. It will contain the article titles and their links.
Title,Link
"Example News Title 1",https://example.com/article1
"Example News Title 2",https://example.com/article2
...
📌 Notes

Make sure you have internet access to fetch the page.

The script uses a custom User-Agent to avoid being blocked.

👩‍💻 Author

Created by Olha Kostyria
Part of my Python learning journey and early portfolio.

Thank you for checking out this project!