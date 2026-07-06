from fetch_data import fetch_python_repositories

def main():
    df = fetch_python_repositories()
    print(f"{len(df)}件のリポジトリを取得しました。")

if __name__ == "__main__":
    main()