import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd
from datetime import datetime

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

BASE_URL = "https://book.douban.com/tag/{}?start={}&type=T"


def crawl_year(year, max_books=100):
    books = []
    pages = max_books // 20

    for page in range(pages):
        start = page * 20
        url = BASE_URL.format(year, start)
        print(f"爬取 {year} 年，第 {page + 1} 页")

        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            print("请求失败:", resp.status_code)
            continue

        soup = BeautifulSoup(resp.text, "html.parser")
        items = soup.select("li.subject-item")

        for item in items:
            try:
                title = item.select_one("h2 a").get("title")
                link = item.select_one("h2 a").get("href")

                pub_info = item.select_one(".pub").text.strip()

                rating_tag = item.select_one(".rating_nums")
                rating = rating_tag.text if rating_tag else None

                people_tag = item.select_one(".pl")
                people = people_tag.text.strip("()") if people_tag else None

                books.append({
                    "year": year,
                    "title": title,
                    "rating": rating,
                    "rating_people": people,
                    "pub_info": pub_info,
                    "link": link
                })
            except Exception as e:
                print("解析失败:", e)

        time.sleep(random.uniform(2, 4))  # 防止被封

    return books


def main():
    current_year = datetime.now().year
    years = range(current_year - 5, current_year)

    all_books = []

    for year in years:
        all_books.extend(crawl_year(year))

    df = pd.DataFrame(all_books)
    df.to_csv("douban_books_last_5_years.csv", index=False, encoding="utf-8-sig")
    print("爬取完成，已保存为 douban_books_last_5_years.csv")


if __name__ == "__main__":
    main()