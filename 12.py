import pandas as pd

def analyze_following_difference(users_csv_path='users.csv'):
    # Read the data
    df = pd.read_csv(users_csv_path)
    
    # Calculate average following for hireable users
    hireable_following = df[df['hireable'] == True]['following'].mean()
    
    # Calculate average following for non-hireable users
    non_hireable_following = df[df['hireable'] != True]['following'].mean()
    
    # Calculate the difference rounded to 3 decimal places
    difference = round(hireable_following - non_hireable_following, 3)
    
    # Print debug information
    print(f"Number of hireable users: {len(df[df['hireable'] == True])}")
    print(f"Number of non-hireable users: {len(df[df['hireable'] != True])}")
    print(f"Average following for hireable users: {hireable_following:.3f}")
    print(f"Average following for non-hireable users: {non_hireable_following:.3f}")
    
    return difference

# Calculate the difference
result = analyze_following_difference()
print(f"\nDifference in average following: {result:.3f}")