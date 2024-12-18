<a id="BadgerDevs-Top"></a>


<!-- PROJECT SHIELDS -->

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  
  <p align="center">
    Data pipeline that integrates with Google Sheets to populate product data and related multimedia content based on user-input keywords.<br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#built-with">Built With</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
This project has been built with flask v3.0.3 and python v3.11.4

* [![Flask][Flask.com]][Flask-url]
* [![Python][Python]][Python-url]
<p align="right">(<a href="#BadgerDevs-Top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In order to be able to run and use the project you need to follow the steps below.
### Prerequisites

* Python 3.11.4


### Installation

_In order to run the application you need to have access to the API keys utilized ( or create your own ) and the environment variables to the project._


1. Access Google cloud console and create a new project
2. Enable the Google Sheets API
3. Create a new service account and download the credentials file
4. Share the Google Sheet with the service account email
5. Enable the YouTube data v3 service
6. Create a new API key

7. Clone the repo
   ```sh
   git clone https://github.com/hshibli2002/BadgerDevs.git
   ```
8. Create a virtual environment
   ```sh
   python -m venv venv
   ```
9. Activate the virtual environment
   ```sh
    venv/Scripts/activate.bat
    ```
10. Install the required libraries from requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
11. Create a .env file in the root directory and add the following variables
   ```sh
    GOOGLE_SHEETS_CREDENTIALS_PATH="path/to/your/credentials.json"
    GOOGLE_SHEETS_NAME="name_of_your_google_sheet"

    # Ecommerce Base URLs
    ALIBABA_BASE_URL="https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&SearchText="
    ASOS_BASE_URL="https://www.asos.com/search/?q="

    # User-Agent for Web Scraping Headers
    USER_AGENT=""

    # Youtube API Key
    YOUTUBE_API_KEY="your_youtube_api_key"
    YOUTUBE_API_SERVICE_NAME='youtube'
    YOUTUBE_API_VERSION='v3'
    YOUTUBE_BASE_URL='https://www.youtube.com/watch?v='

    # Local Base URL
    LOCAL_BASE_URL="http://localhost:port"
   ```

<p align="right">(<a href="#BadgerDevs-Top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
# Usage

### **1. Running the Server**
Before accessing the endpoints, make sure the server is running:
```bash
python run.py
```

### **2. Accessing the Endpoints**
The API has the following endpoints:

#### **API Endpoints**

The application provides several API endpoints under the root URL `/api/badgerdevs/`. These endpoints are organized into subroutes for Google Sheets, Alibaba, ASOS, and YouTube.
<br/> All the blueprints are registered into the main app through the `app/routes/blueprints.py` file.

---

### **I. Google Sheets API**
- **Base URL**: `/api/badgerdevs/google-sheets`

#### **a. Add Keyword API**
- **Description**: Adds a keyword to Google Sheets and optionally triggers data processing from selected platforms.
- **Method**: `POST`
- **Endpoint**: `/api/badgerdevs/google-sheets/input`

**Request Payload**:
```json
{
  "keyword": "Any keyword",
  "website": "asos"  # Options: "asos", "alibaba", "youtube", or "" for all
}
```

### **II. E-commerce APIs**

#### **a. Get Alibaba API**
- **Description**: Adds a product to Google Sheets from Alibaba.
- **Method**: `POST`
- **Endpoint**: `/api/badgerdevs/google-sheets/alibaba/search`

**Request Payload**:
```json
{
  "keyword": "Any keyword"
}
```

#### **b. Post ASOS API**
- **Description**: Adds a product to Google Sheets from ASOS.
- **Method**: `POST`
- **Endpoint**: `/api/badgerdevs/google-sheets/asos/search`
- **Request Payload**:
```json
{
  "keyword": "Any keyword"
}
```

### **III. YouTube API**

#### **a. Get YouTube API**
- **Description**: Adds a video to Google Sheets from YouTube.
- **Method**: `POST`
- **Endpoint**: `/api/badgerdevs/google-sheets/youtube/search`

**Request Payload**:
```json
{
  "keyword": "Any keyword"
}
```

### **2. Testing the API Endpoints**
To test the API endpoints, you can use the `test.py` script in the root directory. The script sends requests to the API endpoints and prints the responses.

```bash
python app/tests/
```

### **3. Project Structure**
This document describes the project structure, its components, and the reasoning behind the design.
<br/>
```plaintext
.
├── app
│   ├── ecommerce
│   │   ├── controllers
│   │   │   ├── alibaba_controller.py    # Handles Alibaba API routes.
│   │   │   ├── asos_controller.py       # Handles ASOS API routes.
│   │   ├── handlers
│   │   │   ├── alibaba_handler.py       # Implements data scraping for Alibaba.
│   │   │   ├── asos_handler.py          # Implements data scraping for ASOS.
│   ├── google_sheets
│   │   ├── controllers
│   │   │   ├── google_sheets_controller.py  # Handles Google Sheets API routes.
│   │   ├── handlers
│   │   │   ├── google_sheets_handler.py     # Handles interactions with Google Sheets.
│   ├── models
│   │   ├── ecommerce_product.py         # Defines the structure for e-commerce product data.
│   │   ├── youtube_video.py             # Defines the structure for YouTube video data.
│   ├── routes
│   │   ├── blueprints.py                # Registers and organizes application blueprints.
│   ├── streaming
│   │   ├── controllers
│   │   │   ├── youtube_api_controller.py  # Handles YouTube API routes.
│   │   ├── handlers
│   │   │   ├── youtube_api_handler.py     # Implements YouTube video data fetching logic.
│   ├── Utils
│   │   ├── api_Mapping.py               # Maps API endpoints to processing functions.
│   │   ├── config.py                    # Configures application-level settings and environment variables.
│   │   ├── formattingData.py            # Formats and processes fetched data for storage.
│   │   ├── img.png                      # Placeholder image or utility file for the project.
│   │   ├── similarity_algorithm.py      # Implements TF-IDF cosine similarity for text comparison.
│   │   ├── testfile.py                  # Temporary file for testing functionality during development.
│   │   ├── website_processor.py         # Centralized processor for handling API calls for multiple websites.
├── tests
│   ├── test_endpoints.py                # Contains endpoint-specific test cases.
├── .gitignore                           # Specifies files and directories to be ignored by Git.
├── .pre-commit-config.yaml              # Configuration for pre-commit hooks.
├── README.md                            # Documentation for the project.
├── requirements.txt                     # Specifies project dependencies.
├── run.py                               # Main entry point for running the Flask server.
```

## **Benefits of This Structure**

### **1. Modularity**
- Each functionality, such as e-commerce scraping, Google Sheets integration, and YouTube processing, is encapsulated within its own module.
- Makes the project easy to navigate and manage.

### **2. Separation of Concerns**
- Business logic, API routing, and data processing are separated into controllers, handlers, and utility files, ensuring maintainability.

### **3. Scalability**
- The project is designed to accommodate new features, APIs, or platforms without impacting existing code.

### **4. Reusability**
- Centralized utility functions and configurations are shared across the project, reducing code duplication.

### **5. Maintainability**
- Clear organization and descriptive naming conventions make it easy for developers to debug and extend the project.

### **6. Testing**
- A dedicated `tests/` directory ensures all features are tested, maintaining the reliability of APIs.


<!-- ROADMAP -->
## Roadmap

- [x] Create a Flask API
- [x] Connect to Google Sheets API
- [x] Add API Key for Google Sheets API
- [x] Add User-Agent Headers for Web Scraping
- [x] Scrape Ecommerce Websites
- [x] Initialize API endpoints for Ecommerce data retrieval
- [x] Use Similarity Algorithm to filter products:
  - [x] Use TF-IDF for keyword extraction and similarity
  - [x] Use Cosine Similarity for similarity calculation
- [x] Utilize YouTube Data v3 API for media metadata
- [x] Add API Key for YouTube Data v3 API
- [x] Testing Script for API endpoints
- [x] Adding pre-commit hooks for code quality
- [x] GitHub Actions for linting

### Future Enhancements
- [ ] Add more Ecommerce websites:
    - [ ] Allowing Ethical Web Scraping
    - [ ] Granting API access through subscription
    - [ ] Offer a public API for data retrieval
    - [ ] Implement a rate limiter for API requests
    - [ ] Implement a caching mechanism for API responses
- [ ] Implement a front-end for user interaction
- [ ] Add more streaming platforms:
  - [ ] TikTok

<p align="right">(<a href="#BadgerDevs-Top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

[Twitter](https://twitter.com/shiblihashem) - [Email](mailto:hshibli2002@gmail.com)

[BadgerDevs Assessment](https://github.com/hshibli2002/badgerdevs)

<p align="right">(<a href="#BadgerDevs-Top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Throughout this assessment, I have utilized the following resources:

* [Flask Documentation](https://flask.palletsprojects.com/en/stable)
* [AliBaba](https://www.alibaba.com)
* [ASOS](https://www.asos.com)
* [ASOS Terms & Services](https://www.asos.com/terms-and-conditions/)
* [Google Cloud Console](https://console.cloud.google.com)
* [Google Sheets API](https://developers.google.com/sheets/api)
* [YouTube Data API v3](https://developers.google.com/youtube/v3)
* [TF-IDF Cosine Similarity](https://towardsdatascience.com/natural-language-processing-feature-engineering-using-tf-idf-e8b9d00e7e76)
* [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
* [Python Requests Library](https://docs.python-requests.org/en/master/)
* [Python Selenium Library](https://pypi.org/project/selenium/)


<p align="right">(<a href="#BadgerDevs-Top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/hashemshibli
[Flask.com]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/stable/
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
