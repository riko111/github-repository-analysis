from fetch_data import fetch_python_repositories
from analyze_data import plot_top10_stars, analyze_star_fork_correlation,analyze_repository_creation_year,analyze_star_distribution

def main():
    fetch_python_repositories()
    plot_top10_stars()
    analyze_star_fork_correlation()
    analyze_repository_creation_year()
    analyze_star_distribution()

if __name__ == "__main__":
    main()