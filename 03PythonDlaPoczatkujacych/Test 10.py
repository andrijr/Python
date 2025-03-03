import requests
from bs4 import BeautifulSoup
import pandas as pd
from pytrends.request import TrendReq


def get_related_keywords(keyword):
    url = f"https://suggestqueries.google.com/complete/search?output=toolbar&hl=pl&q={keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    suggestions = [suggestion['data'] for suggestion in soup.find_all('suggestion')]
    return suggestions


def get_monthly_searches(keywords):
    pytrends = TrendReq(hl='pl-PL', tz=360)
    pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='PL', gprop='')
    data = pytrends.interest_over_time()
    monthly_searches = data.mean().round().astype(int)
    return monthly_searches


def main():
    user_keyword = input("Podaj słowo kluczowe: ")
    related_keywords = get_related_keywords(user_keyword)

    print(f"\nNajlepiej dopasowane słowa kluczowe dla '{user_keyword}':")
    for i, keyword in enumerate(related_keywords, 1):
        print(f"{i}. {keyword}")

    print("\nPobieram dane o miesięcznych wyszukiwaniach...")
    monthly_searches = get_monthly_searches([user_keyword] + related_keywords[:4])

    results = pd.DataFrame({
        'Słowo kluczowe': [user_keyword] + related_keywords[:4],
        'Średnia miesięczna liczba wyszukiwań': monthly_searches
    })

    print("\nWyniki:")
    print(results.to_string(index=False))


if __name__ == "__main__":
    main()

    ka