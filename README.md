# Notes from the project owner

To open up more innovation and research, SafeTravelPH Mobility Innovations Organization, Inc., has started this open-source project that aims to provide developers with access to public transport data through a public API. This makes it easier for software developers to create their own public transport apps (like SakayPH) and provide realtime updates, not just static information about the routes. Contact SafeTravelPH, a nonprofit organization based in UP Diliman, for more information and collaboration.

The project involves creating a public API that exposes public transport data in a standardized format. The data will come from drivers using a fleet driver monitoring app such the SafeTravelPH mobile app (available on Google Play and Apple PlayStore, allowing developers to query the data for real-time information such as PUV locations, estimated arrival times, and service alerts.

Public transport operators and regulators can provide real-time data to developers, which can lead to an increase in ridership and overall customer satisfaction. Developers can create innovative transit apps that improve the transit experience for commuters, such as apps that provide trip planning, providing customer/commuter feedbacks to operators, and recording trip milestones and getting incentives from operators like fare discount coupons.

# Public Transport Information System API for Commuter App Developers

This project aims to improve the availability and accessibility of transit data in the Philippines, with a focus on utilizing Google Transit and General Transit Feed Specification (GTFS) to facilitate the development of mobile applications and other tools for public transport information.

The intended users of this project are developers who want to create their own PUV information apps using the GTFS feeds published by the local government units, government agencies, or PUV Operators. SafeTravelPH, a nonprofit organization based in UP Diliman, is working with these stakeholders to be able to generate data from PUV trips using a mobile app to be used by drivers. They (the LGU, DOTr/LTFRB, operators or a consortium among them) are responsible for maintaining the GTFS feeds and publishing them through a public API, which developers can use to access the data for their own applications.

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

***
## Other similar open source projects outside the Philippine
Here are some open source projects related to public transit information systems:

1. Transitland - an open platform for accessing and sharing transit data from around the world: https://github.com/transitland/transitland

2. OneBusAway - an open-source platform for real-time transit information: https://github.com/OneBusAway/onebusaway-application-modules

3. OpenTripPlanner - a multi-modal trip planner that can be customized for a specific transit network: https://github.com/opentripplanner/OpenTripPlanner

4. GTFS-realtime-validator - a tool for validating GTFS-realtime feeds: https://github.com/CUTR-at-USF/gtfs-realtime-validator

5. GTFS Editor - a web-based editor for GTFS data: https://github.com/CUTR-at-USF/gtfs-editor

***
# Publishing the API

The API can be accessed by other developers who want to build their own applications that use the data and services provided by the transportation system. These applications could include bus tracking apps, trip planning tools, and fare calculators. In the case of this example we have been discussing, the API would provide access to the GTFS feeds being published by the transport provider or regulator in the Philippines. Other developers could use this API to retrieve the data and use it in their own applications. 

To use the API, developers would need to send HTTP requests to specific URLs provided by the API. These requests would include parameters such as the data and time of the request, the type of data being requested (e.g. bus locations), and any filters or options that the developer wants to apply. The API would then respond with the requested data in a structured format, such as JSON or XML. It is possible to make the API available publicly without requiring developers to register with the transit agency or Google Transit. However, the transit agency may choose to implement authentication and rate limiting to prevent abuse of the API and ensure that it is used responsibly.

This API can be deployed to a cloud provider like Heroku or Google Cloud Platform, and the public URL can be shared with developers who want to access the GTFS data for the transit agency. The developers can then build their own mobile apps or web applications that consume the API to display the transit information.

## Google Cloud Platform publishing of the API

Here are the high-level steps to publish your API on Google Cloud Platform and provide a URL for other developers:

1. Create a Google Cloud Project: Go to the Google Cloud Console and create a new project. This will be the project where you'll host your API.

2. Deploy your API code to a cloud provider: There are several cloud providers you can use to deploy your API, including Google App Engine, Google Kubernetes Engine, and Google Compute Engine. Choose the one that best fits your needs, and follow the documentation to deploy your API code to the cloud provider.

3. Set up an API Gateway: Google Cloud provides an API Gateway service that acts as a front-end to your API, handling authentication, rate limiting, and other common API management tasks. Follow the documentation to set up an API Gateway for your API.

4. Configure the API Gateway to route requests to your API: Once you've set up the API Gateway, you'll need to configure it to route requests to your API running in the cloud provider. You'll need to specify the URL for your API, along with any authentication and rate limiting settings.

5. To allow other developers to access your API, you'll need to create an API key. This key will be used to authenticate requests to your API. You can create an API key using the Google Cloud Console.

6. Publish the API documentation: To help other developers use your API, you'll want to publish the API documentation. You can use tools like Swagger or OpenAPI to generate the documentation, and then publish it on a public website.

7. Share the API URL and API key: Finally, you'll need to share the URL for your API along with the API key with other developers who want to use your API. You can share this information through your API documentation, or through other means like email or messaging apps.

These are just the high-level steps, and there are many details and configuration options to consider along the way. You'll want to refer to the documentation for each service to ensure you're configuring everything correctly.
