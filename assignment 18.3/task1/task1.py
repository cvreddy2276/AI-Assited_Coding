import requests
import json
from typing import Dict, Optional, Tuple

class PublicTransportAPI:
    """
    A class to interact with a Public Transport API for fare information.
    This implementation uses a mock API for demonstration purposes.
    In a real implementation, replace with actual API endpoints.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the API client.

        Args:
            api_key: Optional API key for authentication
        """
        self.api_key = api_key
        self.base_url = "https://api.tfl.gov.uk"  # Example: Transport for London API
        self.session = requests.Session()

    def validate_station(self, station_name: str) -> bool:
        """
        Validate if a station name exists.

        Args:
            station_name: Name of the station to validate

        Returns:
            True if station is valid, False otherwise
        """
        try:
            # For TfL API, we can check if station exists by searching
            # In a real implementation, this would call the API
            url = f"{self.base_url}/StopPoint/Search/{station_name}"
            params = {'app_key': self.api_key} if self.api_key else {}

            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            return len(data.get('matches', [])) > 0

        except requests.exceptions.RequestException:
            # For demo purposes, accept common station names
            valid_stations = [
                'london bridge', 'waterloo', 'victoria', 'kings cross',
                'paddington', 'liverpool street', 'euston', 'charing cross',
                'oxford circus', 'piccadilly circus', 'baker street'
            ]
            return station_name.lower() in valid_stations

    def get_fare_details(self, source: str, destination: str) -> Dict:
        """
        Get fare details between two stations.

        Args:
            source: Source station name
            destination: Destination station name

        Returns:
            Dictionary containing fare information

        Raises:
            ValueError: If stations are invalid
            ConnectionError: If API is down
        """
        # Validate inputs
        if not source or not destination:
            raise ValueError("Source and destination stations cannot be empty")

        if not self.validate_station(source):
            raise ValueError(f"Invalid source station: {source}")

        if not self.validate_station(destination):
            raise ValueError(f"Invalid destination station: {destination}")

        if source.lower() == destination.lower():
            raise ValueError("Source and destination stations cannot be the same")

        try:
            # In a real implementation, this would call the actual API
            # For demo, we'll simulate API responses
            fare_data = self._mock_api_call(source, destination)

            return fare_data

        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"API is currently unavailable: {str(e)}")

    def _mock_api_call(self, source: str, destination: str) -> Dict:
        """
        Mock API call for demonstration purposes.
        Replace with actual API integration.

        Args:
            source: Source station
            destination: Destination station

        Returns:
            Mock fare data
        """
        # Simulate different fare zones and distances
        zones = {
            'london bridge': 1,
            'waterloo': 1,
            'victoria': 1,
            'kings cross': 1,
            'paddington': 1,
            'liverpool street': 1,
            'euston': 1,
            'charing cross': 1,
            'oxford circus': 2,
            'piccadilly circus': 2,
            'baker street': 2
        }

        source_zone = zones.get(source.lower(), 1)
        dest_zone = zones.get(destination.lower(), 1)

        # Calculate fare based on zones (simplified)
        base_fare = 2.70  # Base fare for zone 1
        zone_difference = abs(source_zone - dest_zone)
        fare = base_fare + (zone_difference * 0.50)

        return {
            'source': source,
            'destination': destination,
            'source_zone': source_zone,
            'destination_zone': dest_zone,
            'fare_amount': round(fare, 2),
            'currency': 'GBP',
            'fare_type': 'Adult single',
            'validity': 'Single journey',
            'peak_hours': True if zone_difference > 0 else False
        }

def display_fare_details(fare_data: Dict) -> None:
    """
    Display fare details in a structured format.

    Args:
        fare_data: Dictionary containing fare information
    """
    print("\n" + "="*50)
    print("PUBLIC TRANSPORT FARE DETAILS")
    print("="*50)
    print(f"From: {fare_data['source'].title()}")
    print(f"To: {fare_data['destination'].title()}")
    print(f"Source Zone: {fare_data['source_zone']}")
    print(f"Destination Zone: {fare_data['destination_zone']}")
    print(f"Fare Type: {fare_data['fare_type']}")
    print(f"Amount: {fare_data['currency']} {fare_data['fare_amount']}")
    print(f"Validity: {fare_data['validity']}")
    print(f"Peak Hours: {'Yes' if fare_data['peak_hours'] else 'No'}")
    print("="*50 + "\n")

def main():
    """
    Main function to demonstrate the Public Transport API integration.
    """
    # Initialize API client (no API key needed for demo)
    api = PublicTransportAPI()

    # Example usage
    test_cases = [
        ("London Bridge", "Oxford Circus"),
        ("Waterloo", "Victoria"),
        ("Paddington", "Baker Street"),
        ("Invalid Station", "London Bridge"),  # Should fail validation
        ("London Bridge", "London Bridge"),     # Should fail validation
    ]

    for source, destination in test_cases:
        try:
            print(f"\nQuerying fare from {source} to {destination}...")
            fare_data = api.get_fare_details(source, destination)
            display_fare_details(fare_data)

        except ValueError as e:
            print(f"Validation Error: {e}")
        except ConnectionError as e:
            print(f"API Error: {e}")

    # Interactive mode
    print("\n" + "="*50)
    print("INTERACTIVE FARE LOOKUP")
    print("="*50)

    while True:
        try:
            source = input("Enter source station (or 'quit' to exit): ").strip()
            if source.lower() == 'quit':
                break

            destination = input("Enter destination station: ").strip()

            fare_data = api.get_fare_details(source, destination)
            display_fare_details(fare_data)

        except ValueError as e:
            print(f"Validation Error: {e}")
        except ConnectionError as e:
            print(f"API Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
