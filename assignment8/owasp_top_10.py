# Task 6: Scraping Structured Data

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import csv

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.get("https://owasp.org/Top10/2025/")

top_ten_heading = driver.find_element(
    By.CSS_SELECTOR,
    '[id="top-102025-list"]'
)

top_ten_list = top_ten_heading.find_element(
    By.XPATH,
    "following-sibling::ol[1]"
)

vulnerability_links = top_ten_list.find_elements(
    By.XPATH,
    "./li/a"
)

vulnerabilities = []

for link in vulnerability_links:
    title = link.text
    href = link.get_attribute("href")

    vulnerability = {
        "Title": title,
        "Link": href
    }

    vulnerabilities.append(vulnerability)

print(vulnerabilities)

driver.quit()

with open(
    "assignment8/owasp_top_10.csv",
    "w",
    newline=""
) as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(["Title", "Link"])

    for vulnerability in vulnerabilities:
        writer.writerow([
            vulnerability["Title"],
            vulnerability["Link"]
        ])