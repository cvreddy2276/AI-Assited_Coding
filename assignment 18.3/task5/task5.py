import requests
from typing import Dict, Optional
import time


MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds - used for rate limit waits


class COVID19Statistics:
    """Fetches and displays COVID-19 statistics for countries."""

    def __init__(self):
        """Initialize the COVID-19 statistics fetcher."""
        # Using disease.sh API - free, no API key required
        self.base_url = "https://disease.sh/v3/covid-19"
        self.session = requests.Session()
        self.session.timeout = 10

    def fetch_country_data(
        self,
        country_name: str,
        retry_count: int = 0,
    ) -> Dict[str, object]:
        """
        Fetch COVID-19 statistics for a specific country with retry logic.

        Args:
            country_name: Name of the country to fetch data for.
            retry_count: Current retry attempt (used internally for rate limits).

        Returns:
            Dictionary containing COVID-19 statistics.

        Raises:
            ValueError: If country name is invalid or empty.
            RuntimeError: If API request fails after retries or other API errors.
        """
        if not country_name or not isinstance(country_name, str):
            raise ValueError("Country name must be a non-empty string")

        country_name = country_name.strip()

        url = f"{self.base_url}/countries/{country_name}"

        try:
            response = requests.get(url, timeout=10)

            # Handle rate limiting (HTTP 429)
            if response.status_code == 429:
                if retry_count < MAX_RETRIES:
                    wait_time = RETRY_DELAY * (2 ** retry_count)  # Exponential backoff
                    print(
                        f"Rate limit exceeded. Waiting {wait_time} seconds "
                        f"before retry ({retry_count + 1}/{MAX_RETRIES})..."
                    )
                    time.sleep(wait_time)
                    return self.fetch_country_data(country_name, retry_count + 1)
                else:
                    raise RuntimeError(
                        "API rate limit exceeded. Maximum retries (3) reached. "
                        "Please try again later."
                    )

            # Handle country not found (HTTP 404)
            if response.status_code == 404:
                raise ValueError(
                    f"Country '{country_name}' not found. "
                    "Please check the spelling and try again."
                )

            # Handle server errors (HTTP 5xx)
            if response.status_code >= 500:
                if retry_count < MAX_RETRIES:
                    wait_time = RETRY_DELAY * (2 ** retry_count)
                    print(
                        f"Server error ({response.status_code}). "
                        f"Waiting {wait_time} seconds before retry "
                        f"({retry_count + 1}/{MAX_RETRIES})..."
                    )
                    time.sleep(wait_time)
                    return self.fetch_country_data(country_name, retry_count + 1)
                else:
                    raise RuntimeError(
                        f"Server error ({response.status_code}). "
                        "The API is temporarily unavailable. Please try again later."
                    )

            # Handle other HTTP errors
            if not response.ok:
                raise RuntimeError(f"API returned status {response.status_code}")

            response.raise_for_status()

        except requests.exceptions.Timeout:
            if retry_count < MAX_RETRIES:
                wait_time = RETRY_DELAY * (2 ** retry_count)
                print(
                    f"Request timeout. Waiting {wait_time} seconds before retry "
                    f"({retry_count + 1}/{MAX_RETRIES})..."
                )
                time.sleep(wait_time)
                return self.fetch_country_data(country_name, retry_count + 1)
            raise RuntimeError(
                "Network request timeout. The API did not respond in time. "
                "Please try again later."
            )

        except requests.exceptions.ConnectionError:
            if retry_count < MAX_RETRIES:
                wait_time = RETRY_DELAY * (2 ** retry_count)
                print(
                    f"Connection error. Waiting {wait_time} seconds before retry "
                    f"({retry_count + 1}/{MAX_RETRIES})..."
                )
                time.sleep(wait_time)
                return self.fetch_country_data(country_name, retry_count + 1)
            raise RuntimeError(
                "Unable to connect to the COVID-19 API. "
                "Please check your internet connection and try again."
            )

        except requests.exceptions.RequestException as exc:
            raise RuntimeError(f"Network error: {exc}")

        try:
            data = response.json()
        except ValueError as exc:
            raise RuntimeError("API returned invalid JSON response") from exc

        # Validate required fields
        required_fields = ["cases", "deaths", "recovered", "country"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise RuntimeError(
                f"API response missing required fields: {', '.join(missing_fields)}"
            )

        return data

    def get_covid_stats(self, country_name: str) -> Dict[str, object]:
        """
        Get formatted COVID-19 statistics for a country.

        Args:
            country_name: Name of the country.

        Returns:
            Dictionary with formatted statistics.
        """
        data = self.fetch_country_data(country_name)

        total_confirmed = data.get("cases", 0)
        total_deaths = data.get("deaths", 0)
        total_recovered = data.get("recovered", 0)
        active_cases = data.get("active", 0)

        # Calculate active cases if not provided
        if not active_cases:
            active_cases = total_confirmed - total_deaths - total_recovered

        return {
            "country": data.get("country", country_name),
            "total_confirmed": total_confirmed,
            "total_deaths": total_deaths,
            "total_recovered": total_recovered,
            "active_cases": active_cases,
            "population": data.get("population", "N/A"),
            "updated_at": data.get("updated", "N/A"),
        }

    def display_statistics(self, stats: Dict[str, object]) -> None:
        """
        Display COVID-19 statistics in a formatted table.

        Args:
            stats: Dictionary containing COVID-19 statistics.
        """
        print("\n" + "=" * 70)
        print(f"COVID-19 STATISTICS FOR {stats['country'].upper()}")
        print("=" * 70)

        print(f"Total Confirmed Cases: {stats['total_confirmed']:,}")
        print(f"Total Deaths: {stats['total_deaths']:,}")
        print(f"Total Recovered: {stats['total_recovered']:,}")
        print(f"Active Cases: {stats['active_cases']:,}")

        # Calculate and display percentages
        if stats["total_confirmed"] > 0:
            death_rate = (stats["total_deaths"] / stats["total_confirmed"]) * 100
            recovery_rate = (stats["total_recovered"] / stats["total_confirmed"]) * 100
            active_rate = (stats["active_cases"] / stats["total_confirmed"]) * 100

            print(f"\nDeath Rate: {death_rate:.2f}%")
            print(f"Recovery Rate: {recovery_rate:.2f}%")
            print(f"Active Rate: {active_rate:.2f}%")

        if stats["population"] != "N/A":
            population = stats["population"]
            cases_per_million = (
                (stats["total_confirmed"] / population) * 1_000_000
                if population > 0
                else 0
            )
            print(f"\nPopulation: {population:,}")
            print(f"Cases per Million: {cases_per_million:,.2f}")

        print(f"\nLast Updated: {stats['updated_at']}")
        print("=" * 70 + "\n")


def main() -> None:
    """Main function to demonstrate the COVID-19 statistics fetcher."""
    fetcher = COVID19Statistics()

    # Test with predefined countries
    test_countries = ["United States", "India", "Brazil"]

    print("Fetching COVID-19 statistics for sample countries...\n")
    for country in test_countries:
        try:
            print(f"Fetching data for {country}...")
            stats = fetcher.get_covid_stats(country)
            fetcher.display_statistics(stats)
        except ValueError as exc:
            print(f"Input Error: {exc}\n")
        except RuntimeError as exc:
            print(f"API Error: {exc}\n")

    # Interactive mode
    print("\n" + "=" * 70)
    print("INTERACTIVE COVID-19 STATISTICS CHECKER")
    print("=" * 70)

    while True:
        try:
            country = input(
                "\nEnter country name (or 'quit' to exit): "
            ).strip()

            if country.lower() == "quit":
                print("Thank you for using the COVID-19 Statistics checker!")
                break

            if not country:
                print("Please enter a valid country name.")
                continue

            print(f"\nFetching COVID-19 data for {country}...")
            stats = fetcher.get_covid_stats(country)
            fetcher.display_statistics(stats)

        except ValueError as exc:
            print(f"Input Error: {exc}")
        except RuntimeError as exc:
            print(f"API Error: {exc}")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break


if __name__ == "__main__":
    main()
