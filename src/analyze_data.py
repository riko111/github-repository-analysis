import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = "data/python_repositories.csv"

def plot_top10_stars():
    df = pd.read_csv(CSV_PATH)
    df.sort_values('Stars')
    top10 = df.head(10)

    x = top10['Repository']
    y = top10["Stars"]

    fig, ax = plt.subplots(figsize=(12, 6))
    plt.bar(x,y)
    plt.title('Top 10 Python Repositories by GitHub Stars')
    plt.xlabel('Repository Name')
    plt.ylabel('Number of Stars')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(r'.\graphs\top10_stars.png')
