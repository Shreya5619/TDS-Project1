import csv
import numpy as np

# Lists to store the followers and public repos of users from Delhi
followers = []
public_repos = []

# Open the users.csv file and read data
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Filter for users in Delhi
        location = row.get('location', '').strip().lower()
        if "delhi" in location:
            # Get followers and public repositories values
            try:
                followers_count = int(row['followers'])
                public_repos_count = int(row['public_repos'])
                
                # Append the valid values to the lists
                followers.append(followers_count)
                public_repos.append(public_repos_count)
            except ValueError:
                # Skip rows with invalid numerical values
                continue

# Ensure there is data to compute correlation
if len(followers) > 1 and len(public_repos) > 1:
    # Compute Pearson correlation coefficient
    correlation_matrix = np.corrcoef(followers, public_repos)
    correlation = correlation_matrix[0, 1]
    # Output correlation rounded to 3 decimal places
    print(f"{correlation:.3f}")
else:
    print("Insufficient data for correlation calculation.")
