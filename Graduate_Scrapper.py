import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re
# import pandas as pd

# Dictionary of job categories and their respective URLs
job_categories = {
    "Banking and Finance": "https://au.gradconnection.com/graduate-jobs/banking-and-finance/melbourne/",
    "Business and Commerce": "https://au.gradconnection.com/graduate-jobs/business-and-commerce/melbourne/",
    "Computer Science": "https://au.gradconnection.com/graduate-jobs/computer-science/melbourne/",
    "Consulting": "https://au.gradconnection.com/graduate-jobs/consulting/melbourne/",
    # "Data Science and Analytics": "https://au.gradconnection.com/graduate-jobs/data-science-and-analytics/melbourne/",
    # "Information Systems": "https://au.gradconnection.com/graduate-jobs/information-systems/melbourne/",
}
# User-Agent header to bot detection
headers = {'User-Agent': "Mozilla/5.0}"}

def convert_closing_dates(text):
    """
    Converts relative closing date into an actual date
    """
    today = datetime.today() # get today's date
    print(text)

    # Match patterns using regular exressions and pattern location
    match = re.search(r"Closing in (\d+) (days|months)", text)

    if match:
        num = int(match.group(1)) # #xtrac the number
        unit = match.group(2) #extract the "days" or "month" component

        # Calculate the new date based on days or months
        if unit == "days":
            closing_date = today + timedelta(days=num)
        elif unit == "months":
            new_month = (today.month + num) % 12 or 12  # Ensure valid month (1-12)
            new_year = today.year + (today.month + num - 1) // 12  # Handle year rollover
            
            closing_date = today.replace(year=new_year, month=new_month)

        return closing_date.strftime("%Y-%m-%d")  # Convert to YYYY-MM-DD format
            
        # Handle "Closing in a month" case
    if "Closing in a month" in text:
        new_month = (today.month + 1) % 12 or 12
        new_year = today.year + (today.month == 12)  # Increment year if current month is December
        closing_date = today.replace(year=new_year, month=new_month)
        return closing_date.strftime("%Y-%m-%d")
    
    return "N/A"

all_jobs = []

# Loop through each job category
for category, url in job_categories.items():
    print(f"Scraping {category} jobs...")

    # Fetch and parse the HTML content
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract job details
    job_listings = soup.find("div", class_="jobs-container")

    relavent_jobs = job_listings.find("div")

    relevant_jobs_all = relavent_jobs.find_all("div", class_="outer-container")

    # List to store job_list per category
    job_list = []

    for job in relevant_jobs_all:
    #     # Extract job title
        job_element = job.find("a", class_="box-header-title")

        #Extract role title
        job_title = job_element.find("h3").text

        # Extract application link
        application_link = job_element["href"]
        full_application_link = f"https://au.gradconnection.com{application_link}"

        # Extract company name
        company_name = job.find("div", class_="box-employer-name").text

        # Days till applications close
        time_left = job.find("div", class_="box-closing-interval").text
        closing_date = convert_closing_dates(time_left)

        print(closing_date)