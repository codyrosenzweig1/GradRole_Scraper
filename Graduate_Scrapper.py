import requests
from bs4 import BeautifulSoup
# import pandas as pd

# Dictionary of job categories and their respective URLs
job_categories = {
    "Banking and Finance": "https://au.gradconnection.com/graduate-jobs/banking-and-finance/melbourne/",
    "Business and Commerce": "https://au.gradconnection.com/graduate-jobs/business-and-commerce/melbourne/",
    "Computer Science": "https://au.gradconnection.com/graduate-jobs/computer-science/melbourne/",
    "Consulting": "https://au.gradconnection.com/graduate-jobs/consulting/melbourne/",
    "Data Science and Analytics": "https://au.gradconnection.com/graduate-jobs/data-science-and-analytics/melbourne/",
    "Information Systems": "https://au.gradconnection.com/graduate-jobs/information-systems/melbourne/",
}
# User-Agent header to bot detection
headers = {'User-Agent': "Mozilla/5.0}"}

all_jobs = []

# Loop through each job category
# for category, url in job_categories.items():
#     print(f"Scraping {category} jobs...")

#     # Fetch and parse the HTML content
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, "html.parser")

#     # Extract job details
    

response = requests.get("https://au.gradconnection.com/graduate-jobs/banking-and-finance/melbourne/", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

jobs_containers = soup.find_all("p", class_="box-header-para")

print(f"Found {len(jobs_containers)} job containers.")

# Print first 1000 characters of each container (to inspect their content)
for i, container in enumerate(jobs_containers):
    print(f"\n--- Jobs Container {i+1} ---")
    print(container.prettify())  # Print first 1000 chars to inspect