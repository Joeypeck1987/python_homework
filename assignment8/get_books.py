# Task 3: Write a Program to Extract this Data

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.get(
    "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
)

book_entries = driver.find_elements(
    By.CSS_SELECTOR,
    "li.row.cp-search-result-item"
)
print(f"Number of search results found: {len(book_entries)}")

results = []

for book in book_entries:
    title_element = book.find_element(
        By.CSS_SELECTOR,
        "span.title-content"
    )
    title = title_element.text

    author_elements = book.find_elements(
        By.CSS_SELECTOR,
        "a.author-link"
    )

    authors = []

    for author_element in author_elements:
        authors.append(author_element.text)

    author = ";".join(authors)

    format_year_container = book.find_element(
        By.CSS_SELECTOR,
        "div.cp-format-info"
    )

    format_year_element = format_year_container.find_element(
        By.CSS_SELECTOR,
        "span.display-info"
    )

    format_year = format_year_element.text

    book_data = {
        "Title": title,
        "Author": author,
        "Format-Year": format_year
    }

    results.append(book_data)

driver.quit()

books_df = pd.DataFrame(results)

print(books_df)

# Task 4: Write out the Data

books_df.to_csv(
    "assignment8/get_books.csv",
    index=False
)

with open("assignment8/get_books.json", "w") as json_file:
    json.dump(results, json_file, indent=4)