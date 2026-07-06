import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CSV_PATH = "data/python_repositories.csv"

def plot_top10_stars():
    df = pd.read_csv(CSV_PATH)
    df.sort_values('Stars')
    top10 = df.head(10)

    x = top10['Repository']
    y = top10["Stars"]

    plt.subplots(figsize=(12, 6))
    plt.bar(x,y)
    plt.title('Top 10 Python Repositories by GitHub Stars')
    plt.xlabel('Repository Name')
    plt.ylabel('Number of Stars')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(r'.\graphs\top10_stars.png')


def analyze_star_fork_correlation():
    df = pd.read_csv(CSV_PATH)
    stars = df['Stars']
    forks = df['Forks']
    plt.figure(figsize=(10, 6))
    sns.regplot(
        x=stars,
        y=forks, 
        ci=None,
        scatter_kws={'s': 50, 'alpha': 0.7}, 
        line_kws={'color': 'red'}
    )
    plt.xlabel('Number of Stars')
    plt.ylabel('Number of Forks')
    plt.title('Correlation between Stars and Forks')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(r'.\graphs\star_fork_correlation.png')
    correlation = stars.corr(forks)
    print(f"Correlation between Stars and Forks: {correlation:.2f}")

def analyze_repository_creation_year():
    df = pd.read_csv(CSV_PATH)
    df['created_at'] = pd.to_datetime(df['Created'], errors='coerce')
    df['created_year'] = df['created_at'].dt.year
    year_counts = df['created_year'].value_counts().sort_index()
    
    plt.figure(figsize=(10, 6))
    year_counts.plot(kind='bar')
    plt.title('Number of Popular Python Repositories by Creation Year')
    plt.xlabel('Creation Year')
    plt.ylabel('Number of Repositories')
    plt.xticks(rotation=45)
    plt.bar_label(plt.gca().containers[0], label_type='edge', fontsize=8)
    plt.tight_layout()
    plt.savefig(r'.\graphs\repository_creation_year.png')
