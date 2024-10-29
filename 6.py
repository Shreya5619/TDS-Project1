import csv
from collections import Counter
from datetime import datetime

# Define the list to store programming languages
languages = []

# Read the CSV file with UTF-8 encoding
with open('repositories.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows in the CSV
    for row in reader:
        # Parse the created_at field
        created_at = row.get('created_at', '').strip()
        
        # Convert the date string to a datetime object
        if created_at:
            user_join_date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
            
            # Check if the user joined after 2020
            if user_join_date.year > 2020:
                # Get the language field and clean it up
                language = row.get('language', '').strip()
                if language:
                    languages.append(language)

# Count the occurrence of each language
language_counts = Counter(languages)

# Find the two most common languages
most_common_languages = language_counts.most_common(2)

# Print the second most common language
if len(most_common_languages) >= 2:
    print(most_common_languages[1][0])  # Second most common language
else:
    print("Not enough language data found.")
