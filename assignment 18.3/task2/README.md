# Currency Exchange API Integration

This Python script integrates with a Currency Exchange API to convert Indian Rupees (INR) to US Dollars (USD), Euros (EUR), and British Pounds (GBP). It includes comprehensive error handling for API downtime and invalid responses.

## Features

- **Real-time Exchange Rates**: Fetches current exchange rates from ExchangeRate-API
- **Multi-currency Conversion**: Converts INR to USD, EUR, and GBP simultaneously
- **Comprehensive Error Handling**: Handles API downtime, invalid responses, and network issues
- **Input Validation**: Validates user input and API responses
- **Structured Display**: Presents conversion results in a clear, formatted output

## Installation

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Script

```bash
python task2.py
```

The script will:
1. Run predefined test cases with different amounts
2. Enter interactive mode for custom currency conversions

### Interactive Mode

In interactive mode, you can:
- Enter any amount in INR to convert
- Get conversions to USD, EUR, and GBP
- Type 'quit' to exit

### Example Output

```
============================================================
CURRENCY EXCHANGE RESULTS
============================================================
Amount in INR: ₹1,000.00
------------------------------------------------------------
USD: $10.70
EUR: €9.31
GBP: £8.12
------------------------------------------------------------
Last updated: 2026-04-08 05:30:01 UTC
============================================================
```

## API Integration

The script uses the ExchangeRate-API (https://exchangerate-api.com/), which provides:
- Free tier with no API key required
- Real-time exchange rates
- Reliable service with good uptime

For production use with higher rate limits, you can:
1. Sign up for an API key at https://exchangerate-api.com/
2. Pass the API key when initializing the `CurrencyExchangeAPI` class:
   ```python
   api = CurrencyExchangeAPI(api_key="your_api_key_here")
   ```

## Error Handling

The script handles the following error scenarios:

- **API Downtime**: Connection errors with user-friendly messages
- **Invalid Responses**: JSON parsing errors and malformed API responses
- **Rate Limiting**: Handles API rate limit exceeded errors
- **Network Issues**: Timeout and connection problems
- **Invalid Input**: Validates user input amounts
- **Unsupported Currencies**: Checks if requested currencies are available

## Code Structure

- `CurrencyExchangeAPI`: Main class for API interactions
- `get_exchange_rates()`: Fetches current exchange rates with error handling
- `convert_currency()`: Performs currency conversion with validation
- `display_conversion_results()`: Formats and displays conversion results
- `main()`: Entry point with test cases and interactive mode

## Testing

The script includes built-in test cases covering:
- Various INR amounts (1000, 5000, 10000, 50000)
- Real-time API calls
- Error handling scenarios
- Interactive user input

## Dependencies

- `requests`: For HTTP API calls
- `datetime`: For timestamp handling
- `json`: For response parsing
- `typing`: For type hints