import requests
import pandas as pd

def fetch_python_repositories():

    url = "https://api.github.com/search/repositories"

    params = {
        "q": "language:Python",
        "sort": "stars",
        "order": "desc",
        "per_page": 100
    }

    response = requests.get(url, params=params)

    data = response.json()

    repositories = []

    for repo in data["items"]:
        repositories.append({
            "Repository": repo["name"],
            "Owner": repo["owner"]["login"],
            "Stars": repo["stargazers_count"],
            "Forks": repo["forks_count"],
            "Issues": repo["open_issues_count"],
            "Language": repo["language"],
            "Created": repo["created_at"],
            "Updated": repo["updated_at"]
        })

    df = pd.DataFrame(repositories)

    df.to_csv(
        "data/python_repositories.csv",
        index=False,
        encoding="utf-8-sig"
    )

    return df