import csv
from collections import Counter
from datetime import datetime

# Counter to store the number of repositories created by each user on weekends
weekend_repo_counts = Counter()

# Open the repositories.csv file and read data
with open('repositories.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        created_at = row.get('created_at', '')
        if created_at:
            # Convert created_at string to a datetime object
            created_date = datetime.fromisoformat(created_at[:-1])  # Remove 'Z' and convert
            
            # Check if the day is Saturday (5) or Sunday (6)
            if created_date.weekday() in [5, 6]:
                user_login = row['login']
                weekend_repo_counts[user_login] += 1  # Increment the count for the user

# Get the top 5 users who created the most repositories on weekends
top_users = weekend_repo_counts.most_common(5)

# Extract the logins of the top users
top_logins = [user[0] for user in top_users]

# Output the top users' logins as a comma-separated string
print(','.join(top_logins))
