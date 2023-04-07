# Open-API-for-Public-Transport-Data-for-Commuter-Mobile-App-Developers
# Public Transport Information System API for Commuter Apps

This is an open-source project that aims to improve the bus information system in the Philippines through mobile apps and the integration of Google Transit and GTFS by government agencies and local government units.

## Getting Started
Prerequisites
- Python 3.6 or higher

## Installation
1. Clone the repository:

git clone https://github.com/your_username/bus-information-system.git

2. Install the dependencies:

pip install -r requirements.txt

3. Create a .env file in the root directory and add the following environment variables:

DB_HOST=<database host>
DB_PORT=<database port>
DB_NAME=<database name>
DB_USERNAME=<database username>
DB_PASSWORD=<database password>

## Usage
  
1. Run the API server:
  
  python api/run.py
  
2. Use the API endpoints to get bus information.
  
# API Endpoints

  ## GET /routes
  
  Returns a list of all bus routes.

  Query Parameters
    - page: The page number of the results.
    - per_page: The number of results per page.

  ## GET /routes/{id}

   Returns the details of a specific bus route.

  ## GET /stops
  
  Returns a list of all bus stops.

  Query Parameters
    - page: The page number of the results.
    - per_page: The number of results per page.

  ## GET /stops/{id}

   Returns the details of a specific bus stop.

  ## GET /arrivals/{stop_id}

  Returns the estimated time of arrival for buses at a specific stop.

# Contributing

  Contributions are welcome! If you find a bug or have a feature request, please create an issue in the repository.
  
## Running tests
  
  1. Create a test database
  
  createdb bus_information_system_test

  2. Run the tests
  
  python -m unittest discover tests

## License
This project is licensed under the {} License - see the LICENSE file for details.
  
## Acknowledgements
This project was inspired by the need for better bus information systems in the Philippines.
Thanks to the Google Transit Partner Program for providing access to the GTFS feed specification.
