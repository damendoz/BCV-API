# Exchange Rate API

## Description

The Exchange Rate API provides the current USD exchange rate against the local currency, retrieved from the Central Bank of Venezuela (BCV) website. It also includes the date when the exchange rate was last updated.

## Requirements

- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

To set up and run the Exchange Rate API locally, follow these steps:

1. **Clone the Repository**

   First, clone the repository to your local machine:

git clone https://github.com/damendoz/BCV-API.git
cd BCV-API

2. **Create a Virtual Environment**

It's recommended to use a virtual environment to manage dependencies. Create and activate a virtual environment:

python -m venv venv

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

3. **Install Dependencies**

Install the required Python packages using pip. Ensure you have the requirements.txt file in the root directory of the project:

pip install -r requirements.txt

If requirements.txt is missing or outdated, you can manually install the dependencies:

pip install django djangorestframework requests beautifulsoup4

4. **Configure the Database**

The project uses SQLite by default, which does not require any additional configuration. If you need to use another database, update the DATABASES setting in exchange_rate_project/settings.py.

5. **Apply Migrations**

Apply the database migrations to set up the initial database schema:

python manage.py migrate

6. **Run the Development Server**

Start the Django development server to test the API locally:

python manage.py runserver

The server will start at http://127.0.0.1:8000/ by default.

7. **Access the API**

Open your web browser or use a tool like curl or Postman to access the API endpoint:

http://127.0.0.1:8000

You should see a JSON response with the current USD exchange rate and the date of the rate.

Response Example:

{
    "usd_rate": 36.67,
    "date_value": "2024-08-12"
}

Response Fields:

usd_rate (float): The current USD exchange rate against the local currency.
date_value (string): The date when the exchange rate was last updated, formatted as "YYYY-MM-DD".
