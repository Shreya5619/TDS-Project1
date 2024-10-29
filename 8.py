import csv

# Define a list to store users and their leader strength
leader_strengths = []

# Read the CSV file with UTF-8 encoding
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Get followers and following counts
        followers = int(row.get('followers', 0).strip())
        following = int(row.get('following', 0).strip())
        
        # Calculate leader strength
        leader_strength = followers / (1 + following)
        
        # Store the user's login and their leader strength
        leader_strengths.append((row.get('login', ''), leader_strength))

# Sort users by leader strength in descending order
leader_strengths.sort(key=lambda x: x[1], reverse=True)

# Get the top 5 users
top_5_leaders = [login for login, strength in leader_strengths[:5]]

# Print the result as a comma-separated list
print(','.join(top_5_leaders))
