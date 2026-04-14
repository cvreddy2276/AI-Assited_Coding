# Public Transport Fare Lookup

This Python script integrates with a Public Transport API to retrieve fare details between two stations. It includes input validation, error handling, and structured display of fare information.

## Features

- **API Integration**: Connects to Transport for London (TfL) API for fare information
- **Input Validation**: Validates source and destination station names
- **Error Handling**: Handles API downtime and invalid station names gracefully
- **Structured Display**: Presents fare details in a clear, formatted output

## Installation

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Script

```bash
python task1.py
```

The script will:
1. Run predefined test cases to demonstrate functionality
2. Enter interactive mode for custom fare lookups

### Interactive Mode

In interactive mode, you can:
- Enter source and destination stations
- Get fare details displayed in a structured format
- Type 'quit' to exit

### Example Output

```
==================================================
PUBLIC TRANSPORT FARE DETAILS
==================================================
From: London Bridge
To: Oxford Circus
Source Zone: 1
Destination Zone: 2
Fare Type: Adult single
Amount: GBP 3.20
Validity: Single journey
Peak Hours: Yes
==================================================
```

## API Integration

The script uses the Transport for London (TfL) API. For production use:

1. Register for a TfL API key at https://api.tfl.gov.uk/
2. Pass the API key when initializing the `PublicTransportAPI` class:
   ```python
   api = PublicTransportAPI(api_key="your_api_key_here")
   ```

## Error Handling

The script handles the following error scenarios:

- **Invalid Station Names**: Returns validation error with message
- **API Downtime**: Catches connection errors and displays user-friendly message
- **Same Source/Destination**: Prevents queries where source equals destination
- **Empty Inputs**: Validates that station names are provided

## Code Structure

- `PublicTransportAPI`: Main class for API interactions
- `validate_station()`: Validates station names
- `get_fare_details()`: Retrieves fare information
- `display_fare_details()`: Formats and displays fare data
- `main()`: Entry point with test cases and interactive mode

## Testing

The script includes built-in test cases covering:
- Valid station pairs
- Invalid station names
- Same source/destination validation
- API error simulation