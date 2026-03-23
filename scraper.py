import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Script started...")

url = "https://quotes.toscrape.com/"
response = requests.get(url)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

for quote in soup.find_all("span", class_="text"):
    quotes.append(quote.text)

for author in soup.find_all("small", class_="author"):
    authors.append(author.text)

df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

# Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df["Quote"] = df["Quote"].str.replace("“", "", regex=False).str.replace("”", "", regex=False)
df["Quote"] = df["Quote"].str.strip()
df["Author"] = df["Author"].str.strip().str.title()

print("After Cleaning:")
print(df.head())

import datetime
df["Scraped_Date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

df.to_csv("quotes_cleaned.csv", index=False)
print("CSV file saved successfully!")