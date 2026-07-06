from fetch_data import fetch_python_repositories
from analyze_data import plot_top10_stars

def main():
    df = fetch_python_repositories()
    print(f"{len(df)}件のリポジトリを取得しました。")
    plot_top10_stars()

if __name__ == "__main__":
    main()