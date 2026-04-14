import requests
import json
from typing import Dict, Optional, List, Tuple
from datetime import datetime

class CurrencyExchangeAPI:
    """
    A class to interact with Currency Exchange APIs for currency conversion.
    This implementation uses ExchangeRate-API for demonstration.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Currency Exchange API client.

        Args:
            api_key: Optional API key for authentication (not required for free tier)
        """
        self.api_key = api_key
        self.base_url = "https://api.exchangerate-api.com/v4/latest/INR"
        self.session = requests.Session()
        self.last_update = None

    def get_exchange_rates(self) -> Dict[str, float]:
        """
        Fetch current exchange rates for INR.

        Returns:
            Dictionary containing exchange rates

        Raises:
            ConnectionError: If API is down or unreachable
            ValueError: If API returns invalid response
        """
        try:
            response = self.session.get(self.base_url, timeout=10)
            response.raise_for_status()

            data = response.json()

            # Validate response structure
            if 'rates' not in data:
                raise ValueError("Invalid API response: missing 'rates' field")

            rates = data['rates']
            self.last_update = datetime.fromtimestamp(data.get('time_last_updated', 0))

            return rates

        except requests.exceptions.Timeout:
            raise ConnectionError("API request timed out. Please check your internet connection.")
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Unable to connect to currency exchange API. Service may be down.")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                raise ConnectionError("API rate limit exceeded. Please try again later.")
            else:
                raise ConnectionError(f"API returned error {e.response.status_code}: {e.response.text}")
        except json.JSONDecodeError:
            raise ValueError("Invalid response format from API. Unable to parse JSON.")

    def convert_currency(self, amount: float, from_currency: str = "INR",
                        to_currencies: List[str] = None) -> Dict[str, float]:
        """
        Convert currency amount to specified currencies.

        Args:
            amount: Amount to convert
            from_currency: Source currency (default: INR)
            to_currencies: List of target currencies (default: USD, EUR, GBP)

        Returns:
            Dictionary with conversion results

        Raises:
            ValueError: If amount is invalid or currencies not supported
            ConnectionError: If API is unavailable
        """
        if to_currencies is None:
            to_currencies = ["USD", "EUR", "GBP"]

        # Validate input
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")

        try:
            rates = self.get_exchange_rates()
        except (ConnectionError, ValueError) as e:
            raise e

        results = {}

        for target_currency in to_currencies:
            if target_currency not in rates:
                raise ValueError(f"Currency '{target_currency}' is not supported by the API")

            # Convert amount
            converted_amount = amount * rates[target_currency]
            results[target_currency] = round(converted_amount, 2)

        return results

def display_conversion_results(amount: float, conversions: Dict[str, float],
                             last_update: Optional[datetime] = None) -> None:
    """
    Display currency conversion results in a structured format.

    Args:
        amount: Original amount in INR
        conversions: Dictionary of converted amounts
        last_update: Timestamp of last rate update
    """
    print("\n" + "="*60)
    print("CURRENCY EXCHANGE RESULTS")
    print("="*60)
    print(f"Amount in INR: ₹{amount:,.2f}")
    print("-"*60)

    for currency, converted_amount in conversions.items():
        currency_symbols = {
            "USD": "$",
            "EUR": "€",
            "GBP": "£"
        }
        symbol = currency_symbols.get(currency, currency)
        print(f"{currency:>3}: {symbol}{converted_amount:,.2f}")

    print("-"*60)
    if last_update:
        print(f"Last updated: {last_update.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    else:
        print("Exchange rates fetched in real-time")
    print("="*60 + "\n")

def main():
    """
    Main function to demonstrate the Currency Exchange API integration.
    """
    # Initialize API client
    api = CurrencyExchangeAPI()

    # Test cases
    test_amounts = [1000, 5000, 10000, 50000]

    print("Testing Currency Exchange API Integration")
    print("="*50)

    for amount in test_amounts:
        try:
            print(f"\nConverting ₹{amount:,.0f} INR...")
            conversions = api.convert_currency(amount)
            display_conversion_results(amount, conversions, api.last_update)

        except (ValueError, ConnectionError) as e:
            print(f"Error: {e}")
            print("Continuing with next test case...\n")

    # Interactive mode
    print("\n" + "="*60)
    print("INTERACTIVE CURRENCY CONVERTER")
    print("="*60)
    print("Convert INR to USD, EUR, and GBP")
    print("Type 'quit' to exit")
    print("="*60)

    while True:
        try:
            amount_input = input("\nEnter amount in INR (or 'quit' to exit): ").strip()

            if amount_input.lower() == 'quit':
                print("Thank you for using the Currency Converter!")
                break

            try:
                amount = float(amount_input)
            except ValueError:
                print("Please enter a valid number.")
                continue

            conversions = api.convert_currency(amount)
            display_conversion_results(amount, conversions, api.last_update)

        except (ValueError, ConnectionError) as e:
            print(f"Error: {e}")
            print("Please try again.")
        except KeyboardInterrupt:
            print("\n\nExiting Currency Converter...")
            break

if __name__ == "__main__":
    main()
