import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

CSV_PATH = "data/python_repositories.csv"
GRAPH_PATH = Path("graphs/")

def load_data():
    return pd.read_csv(CSV_PATH)

def plot_top10_stars():
    df = load_data()
    df.sort_values('Stars', ascending=False, inplace=True)
    top10 = df.head(10)

    x = top10['Repository']
    y = top10["Stars"]

    plt.figure(figsize=(12, 6))
    plt.bar(x,y)
    plt.title('Top 10 Python Repositories by GitHub Stars')
    plt.xlabel('Repository Name')
    plt.ylabel('Number of Stars')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(GRAPH_PATH / "top10_stars.png")
    plt.close()


def analyze_star_fork_correlation():
    df = load_data()
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
    plt.savefig(GRAPH_PATH / "star_fork_correlation.png")
    plt.close()
    correlation = stars.corr(forks)
    print(f"Correlation between Stars and Forks: {correlation:.2f}")

def analyze_repository_creation_year():
    df = load_data()
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
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig(GRAPH_PATH / "repository_creation_year.png")
    plt.close()


def analyze_star_distribution():
    df = load_data()
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Stars'], bins=15, kde=True)
    plt.title('Distribution of Stars in Popular Python Repositories')
    plt.xlabel('Number of Stars')
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig(GRAPH_PATH / "star_distribution.png")
    plt.close()

    print(df['Stars'].describe())
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df['Stars'])
    plt.title('Boxplot of Stars in Popular Python Repositories')
    plt.xlabel('Number of Stars')
    plt.grid(axis='x')
    plt.yticks([])
    plt.tight_layout()
    plt.savefig(GRAPH_PATH / "star_boxplot.png")
    plt.close()


def main():
    plot_top10_stars()
    analyze_star_fork_correlation()
    analyze_repository_creation_year()
    analyze_star_distribution()


if __name__ == "__main__":
    main()