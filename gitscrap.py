import requests
from google.colab import userdata
import pandas as pd
import os
from dotenv import load_dotenv

API=userdata.get('API')

load_dotenv()
GITHUB_TOKEN = os.getenv(API)
headers = {
    "Authorization": f"Bearer {API}",
    "X-GitHub-Api-Version": "2022-11-28"
}
page = 1 
users=[]
while True:
    
    params = {
        'q': 'location:Austin followers:>100',
        'per_page': 100,
        'page': page
    }
    
    response = requests.get(url = 'https://api.github.com/search/users'
, headers=headers, params=params)
    data = response.json()
    
    
    if 'items' not in data or not data['items']:
        break
    
    
    for item in data['items']:
        user_url = item['url']
        user_data = requests.get(user_url, headers=headers).json()
        users.append(user_data)
    
    
    print(f"Fetched page {page}, total users collected: {len(users)}")
    page += 1

    
    if response.headers.get('X-RateLimit-Remaining') == '0':
        reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
        sleep_time = max(reset_time - time.time(), 0) + 1
        print(f"Rate limit hit. Sleeping for {sleep_time} seconds.")
        time.sleep(sleep_time)

def clean_company_name(name):
    if name:
        return name.strip().lstrip("@").upper()
    return ""

def format_user_data(users):
    formatted_users = []
    for user in users:
        formatted_users.append({
            "login": user.get("login", ""),
            "name": user.get("name", ""),
            "company": clean_company_name(user.get("company", "")),
            "location": user.get("location", ""),
            "email": user.get("email", ""),
            "hireable": user.get("hireable", ""),
            "bio": user.get("bio", ""),
            "public_repos": user.get("public_repos", 0),
            "followers": user.get("followers", 0),
            "following": user.get("following", 0),
            "created_at": user.get("created_at", "")
        })
    return formatted_users
formatted_users = format_user_data(users)

logins = [item['login'] for item in formatted_users]

def get_user_repositories(logins):
    repo_data = []
    for login in logins:
      repos_url = f"https://api.github.com/users/{login}/repos?per_page=500"
      repos_response = requests.get(repos_url, headers=headers)
      repos = repos_response.json()
      for repo in repos:
          license_name = repo["license"]["key"] if repo["license"] else ""
          repo_data.append({
              "login": login,
              "full_name": repo.get("full_name", ""),
              "created_at": repo.get("created_at", ""),
              "stargazers_count": repo.get("stargazers_count", 0),
              "watchers_count": repo.get("watchers_count", 0),
              "language": repo.get("language", ""),
              "has_projects": repo.get("has_projects", False),
              "has_wiki": repo.get("has_wiki", False),
              "license_name": license_name
          })
    return repo_data
rep=get_user_repositories(logins)

users_df = pd.DataFrame(formatted_users)
repos_df = pd.DataFrame(rep)

from matplotlib import pyplot as plt
import seaborn as sns

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))  # Adjust size as needed

# 1. Histogram of followers
axs[0].hist(users_df['followers'], bins=20, color='skyblue', edgecolor='black')
axs[0].set_title('Distribution of Followers')
axs[0].set_xlabel('Number of Followers')
axs[0].set_ylabel('Frequency')
axs[0].spines[['top', 'right']].set_visible(False)

# 2. Horizontal bar chart of hireable status
users_df.groupby('hireable').size().plot(kind='barh', color=sns.color_palette('Dark2'), ax=axs[1])
axs[1].set_title('Number of Hireable Users')
axs[1].set_xlabel('Count')
axs[1].spines[['top', 'right']].set_visible(False)

# 3. Histogram of public repositories
axs[2].hist(users_df['public_repos'], bins=20, color='salmon', edgecolor='black')
axs[2].set_title('Distribution of Public Repositories')
axs[2].set_xlabel('Number of Public Repositories')
axs[2].set_ylabel('Frequency')
axs[2].spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.show()

from matplotlib import pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(1, 2, figsize=(18, 6))

# 1. Scatterplot of stargazers count vs watchers count
stargazers = repos_df['stargazers_count']
watchers = repos_df['watchers_count']
axs[0].scatter(stargazers, watchers, alpha=0.5, color='purple')
axs[0].set_title('Stargazers vs Watchers')
axs[0].set_xlabel('Number of Stargazers')
axs[0].set_ylabel('Number of Watchers')
axs[0].set_xscale('log')
axs[0].set_yscale('log')
axs[0].grid()

# 2. Pie chart for programming languages
language_counts = repos_df['language'].value_counts()

axs[1].pie(language_counts, labels=language_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set2"))
axs[1].set_title('Distribution of Programming Languages in Repositories')
axs[1].axis('equal')


plt.tight_layout()
plt.show()
#converting dataframe to csv and then saving
users_df.to_csv("users.csv", index=False)
repos_df.to_csv("repositories.csv", index=False)