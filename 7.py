import csv
from collections import defaultdict

# Define a dictionary to store total stars and repository count per language
language_stats = defaultdict(lambda: {'stars': 0, 'repos': 0})

# Read the CSV file with UTF-8 encoding
with open('repositories.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Get the language and stargazers_count field
        language = row.get('language', '').strip()
        stars = row.get('stargazers_count', '0').strip()

        # Only process if language and stars are available
        if language and stars.isdigit():
            language_stats[language]['stars'] += int(stars)
            language_stats[language]['repos'] += 1

# Calculate average stars for each language
average_stars_per_language = {
    language: stats['stars'] / stats['repos']
    for language, stats in language_stats.items()
    if stats['repos'] > 0
}

# Find the language with the highest average stars
if average_stars_per_language:
    most_popular_language = max(average_stars_per_language, key=average_stars_per_language.get)
    print(most_popular_language)
else:
    print("No language data found.")
