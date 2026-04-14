import requests
from typing import Dict, List, Optional
import time


VALID_CATEGORIES = {
    "sports": "sports",
    "technology": "technology",
    "health": "health",
    "business": "business",
    "entertainment": "entertainment",
    "science": "science",
}

MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds


class NewsAggregator:
    """Fetches and displays top headlines from a news API."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the News Aggregator.

        Args:
            api_key: Optional API key for NewsAPI. If not provided, uses a limited demo.
        """
        self.api_key = api_key or "demo"
        self.base_url = "https://newsapi.org/v2"
        self.session = requests.Session()
        self.session.timeout = 10

    def validate_category(self, category: str) -> bool:
        """
        Validate if the category is supported.

        Args:
            category: The news category to validate.

        Returns:
            True if category is valid, False otherwise.
        """
        return category.lower() in VALID_CATEGORIES

    def fetch_headlines(
        self,
        category: str,
        max_articles: int = 5,
        retry_count: int = 0,
    ) -> List[Dict[str, str]]:
        """
        Fetch top headlines for a given category with retry mechanism.

        Args:
            category: News category (sports, technology, health, business, entertainment, science).
            max_articles: Number of headlines to fetch.
            retry_count: Current retry attempt (used internally).

        Returns:
            List of dictionaries containing headline information.

        Raises:
            ValueError: If category is invalid or API key is missing.
            RuntimeError: If API request fails after all retries.
        """
        if not category or not isinstance(category, str):
            raise ValueError("Category must be a non-empty string")

        if not self.validate_category(category):
            raise ValueError(
                f"Invalid category: {category}. "
                f"Supported categories: {', '.join(VALID_CATEGORIES.keys())}"
            )

        if not self.api_key or self.api_key == "demo":
            # Use fallback for demo mode
            return self._get_fallback_headlines(category, max_articles)

        url = f"{self.base_url}/top-headlines"
        params = {
            "category": VALID_CATEGORIES[category.lower()],
            "pageSize": max_articles,
            "apiKey": self.api_key,
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

        except requests.exceptions.Timeout:
            if retry_count < MAX_RETRIES:
                print(f"Request timeout. Retrying ({retry_count + 1}/{MAX_RETRIES})...")
                time.sleep(RETRY_DELAY)
                return self.fetch_headlines(category, max_articles, retry_count + 1)
            raise RuntimeError("Request failed: API did not respond within timeout period")

        except requests.exceptions.ConnectionError:
            if retry_count < MAX_RETRIES:
                print(f"Connection error. Retrying ({retry_count + 1}/{MAX_RETRIES})...")
                time.sleep(RETRY_DELAY)
                return self.fetch_headlines(category, max_articles, retry_count + 1)
            raise RuntimeError("Request failed: Unable to connect to the news API")

        except requests.exceptions.RequestException as exc:
            raise RuntimeError(f"Request failed: {exc}")

        try:
            data = response.json()
        except ValueError as exc:
            raise RuntimeError("API returned invalid JSON response") from exc

        if not data.get("articles"):
            raise RuntimeError("API returned no articles for the requested category")

        articles = data["articles"][:max_articles]
        return [
            {
                "title": article.get("title", "No title"),
                "description": article.get("description", "No description"),
                "source": article.get("source", {}).get("name", "Unknown"),
                "url": article.get("url", ""),
                "published_at": article.get("publishedAt", "Unknown"),
            }
            for article in articles
        ]

    def _get_fallback_headlines(self, category: str, max_articles: int) -> List[Dict[str, str]]:
        """
        Return fallback headlines when API key is missing or demo mode is active.

        Args:
            category: The news category.
            max_articles: Number of fallback headlines to return.

        Returns:
            List of fallback headline dictionaries.
        """
        fallback_data = {
            "sports": [
                {
                    "title": "Football Championship Live Updates",
                    "description": "Latest updates from the international football championship",
                    "source": "Sports Hub",
                    "url": "https://example.com/sports1",
                    "published_at": "2026-04-14T10:00:00Z",
                },
                {
                    "title": "Tennis Ranking Updates",
                    "description": "Top 10 players announce new rankings",
                    "source": "Tennis News",
                    "url": "https://example.com/sports2",
                    "published_at": "2026-04-14T09:30:00Z",
                },
                {
                    "title": "Basketball Finals Begin",
                    "description": "Season finals kick off with exciting matchups",
                    "source": "Sports Daily",
                    "url": "https://example.com/sports3",
                    "published_at": "2026-04-13T18:00:00Z",
                },
            ],
            "technology": [
                {
                    "title": "AI Breakthrough in Language Models",
                    "description": "New developments in artificial intelligence technology",
                    "source": "Tech Weekly",
                    "url": "https://example.com/tech1",
                    "published_at": "2026-04-14T11:00:00Z",
                },
                {
                    "title": "Quantum Computing Progress",
                    "description": "Scientists achieve major milestone in quantum computing",
                    "source": "Tech Today",
                    "url": "https://example.com/tech2",
                    "published_at": "2026-04-14T08:00:00Z",
                },
                {
                    "title": "New Smartphone Release",
                    "description": "Leading manufacturer announces latest flagship model",
                    "source": "Mobile Tech",
                    "url": "https://example.com/tech3",
                    "published_at": "2026-04-13T15:00:00Z",
                },
            ],
            "health": [
                {
                    "title": "New Treatment for Common Disease",
                    "description": "Medical researchers develop promising new treatment",
                    "source": "Health News",
                    "url": "https://example.com/health1",
                    "published_at": "2026-04-14T12:00:00Z",
                },
                {
                    "title": "Mental Health Awareness Campaign",
                    "description": "Global initiative to promote mental wellness",
                    "source": "Wellness Daily",
                    "url": "https://example.com/health2",
                    "published_at": "2026-04-14T10:00:00Z",
                },
                {
                    "title": "Exercise Benefits Confirmed",
                    "description": "Study shows regular exercise improves longevity",
                    "source": "Health Journal",
                    "url": "https://example.com/health3",
                    "published_at": "2026-04-13T14:00:00Z",
                },
            ],
        }

        category_key = category.lower()
        articles = fallback_data.get(category_key, [])
        return articles[:max_articles]

    def display_headlines(self, headlines: List[Dict[str, str]], category: str) -> None:
        """
        Display headlines in a user-friendly numbered list format.

        Args:
            headlines: List of headline dictionaries to display.
            category: The category of the headlines.
        """
        print("\n" + "=" * 80)
        print(f"TOP {len(headlines)} HEADLINES - {category.upper()}")
        print("=" * 80)

        if not headlines:
            print("No headlines found for this category.")
            print("=" * 80 + "\n")
            return

        for idx, article in enumerate(headlines, 1):
            print(f"\n{idx}. {article['title']}")
            print(f"   Source: {article['source']}")
            print(f"   Published: {article['published_at']}")
            print(f"   Description: {article['description']}")
            if article.get("url"):
                print(f"   URL: {article['url']}")

        print("\n" + "=" * 80 + "\n")


def main() -> None:
    """Main function to demonstrate the news aggregator."""
    # Initialize the news aggregator
    aggregator = NewsAggregator()

    # Test different categories
    test_categories = ["sports", "technology", "health"]

    for category in test_categories:
        try:
            print(f"\nFetching {category} headlines...")
            headlines = aggregator.fetch_headlines(category, max_articles=5)
            aggregator.display_headlines(headlines, category)

        except ValueError as exc:
            print(f"Input Error: {exc}")
        except RuntimeError as exc:
            print(f"API Error: {exc}")

    # Interactive mode
    print("\n" + "=" * 80)
    print("INTERACTIVE NEWS AGGREGATOR")
    print("=" * 80)

    while True:
        try:
            category = input(
                "\nEnter news category (sports/technology/health) or 'quit' to exit: "
            ).strip()

            if category.lower() == "quit":
                print("Thank you for using the News Aggregator!")
                break

            headlines = aggregator.fetch_headlines(category, max_articles=5)
            aggregator.display_headlines(headlines, category)

        except ValueError as exc:
            print(f"Input Error: {exc}")
        except RuntimeError as exc:
            print(f"API Error: {exc}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()
