import csv
from datetime import datetime

# Define the list to store users from Delhi
users_in_delhi = []

# Read the CSV file with UTF-8 encoding
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        location = row['location'].strip().lower()
        # Check if the user is from Delhi
        if 'delhi' in location:
            users_in_delhi.append({
                'login': row['login'],
                'created_at': datetime.strptime(row['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            })

# Sort users based on created_at in ascending order
sorted_users = sorted(users_in_delhi, key=lambda x: x['created_at'])

# Extract the top 5 user logins
top_5_earliest_logins = [user['login'] for user in sorted_users[:5]]

# Print the result as a comma-separated list
print(','.join(top_5_earliest_logins))
