import pandas as pd
from scipy.stats import linregress

# Load the CSV file
csv_file = 'users.csv'  # Replace with the correct path

# Load the CSV into a DataFrame
df = pd.read_csv(csv_file)

# Filter out users without bios
df = df[df['bio'].notna()]

# Calculate word count for each bio
df['bio_word_count'] = df['bio'].apply(lambda x: len(x.split()))

# Perform linear regression with followers on bio word count
slope, intercept, r_value, p_value, std_err = linregress(df['bio_word_count'], df['followers'])

print(f"Regression Slope of Followers on Bio Word Count: {slope:.3f}")
