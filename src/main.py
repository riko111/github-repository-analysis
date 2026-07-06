from fetch_data import fetch_python_repositories
from analyze_data import plot_top10_stars, analyze_star_fork_correlation

def main():
    df = fetch_python_repositories()
    plot_top10_stars()
    analyze_star_fork_correlation()

if __name__ == "__main__":
    main()