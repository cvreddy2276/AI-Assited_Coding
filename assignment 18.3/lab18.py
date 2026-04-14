
import requests
import time

API_KEY = "YOUR_API_KEY"

def get_news(category):
    url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}"

    for attempt in range(2):  # retry mechanism
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                data = response.json()
                articles = data['articles'][:5]

                print("\n--- Top Headlines ---")
                for i, article in enumerate(articles, 1):
                    print(f"{i}. {article['title']}")
                return

            elif response.status_code == 401:
                print("Invalid API Key.")
                return
            else:
                print("Error fetching news.")

        except requests.exceptions.RequestException:
            print("Retrying...")
            time.sleep(2)

    print("Failed after retry.")

# Example
get_news("technology")
""" Write Python code to fetch country-wise COVID-19 statistics using an API. Handle invalid country input, rate limits, and network errors with retry logic.""""


import requests
import time

def get_covid_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"

    for attempt in range(2):
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                data = response.json()

                print("\n--- COVID Stats ---")
                print("Country:", data['country'])
                print("Total Cases:", data['cases'])
                print("Deaths:", data['deaths'])
                print("Recovered:", data['recovered'])
                print("Active:", data['active'])
                return

            elif response.status_code == 404:
                print("Invalid country name.")
                return
            elif response.status_code == 429:
                print("Rate limit exceeded. Waiting...")
                time.sleep(2)
            else:
                print("Error fetching data.")

        except requests.exceptions.RequestException:
            print("Network error. Retrying...")
            time.sleep(2)

    print("Failed after retries.")

# Example
get_covid_data("India")