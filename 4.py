import csv
from collections import Counter

# Define the list to store company names
companies = []

# Read the CSV file with UTF-8 encoding
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Get and clean up the company field (ignore empty values)
        company = row.get('company', '').strip()
        if company:
            companies.append(company)

# Count the occurrence of each company
company_counts = Counter(companies)

# Find the most common company
most_common_company = company_counts.most_common(1)

# Print the result
if most_common_company:
    print(most_common_company[0][0])
else:
    print("No company data found.")
