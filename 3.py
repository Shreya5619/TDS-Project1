import csv
from collections import Counter

# Define the list to store license names
licenses = []

# Read the CSV file with UTF-8 encoding
with open('repositories.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Check if the license_name field is present and not empty
        license_name = row.get('license_name', '').strip()
        if license_name:
            licenses.append(license_name)

# Count the occurrence of each license
license_counts = Counter(licenses)

# Get the 3 most common licenses
top_3_licenses = [license for license, count in license_counts.most_common(3)]

# Print the result as a comma-separated list
print(','.join(top_3_licenses))
