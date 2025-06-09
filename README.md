🏡 Zillow-Style Rental Scraper

This Python web scraper extracts rental property information from a Zillow-style clone site and automatically submits the data to a Google Form. It uses Selenium for browser automation and BeautifulSoup for parsing HTML content.
🚀 Features

    Scrapes address, rental price, and listing URL from a property listings site.

    Automatically fills out and submits a Google Form for each rental entry.

    Combines static scraping with Selenium-driven form interaction.

    ChromeDriver is set to detach, keeping the browser open for debugging.

🧰 Technologies Used

    Python 3

    Selenium

    BeautifulSoup (bs4)

    Requests

    Google Forms

🗂️ Project Structure

scraper/
├── scraper.py       # Main scraping and automation script
├── requirements.txt # Python dependencies
└── README.md        # Project documentation

🛠️ Setup Instructions
1. Clone the Repository

git clone https://github.com/yourusername/zillow-scraper.git
cd zillow-scraper

2. Install Dependencies

pip install -r requirements.txt

3. Add Your Google Form Link

Update the google_form_URL variable in your script:

google_form_URL = "https://forms.gle/your-form-id"

Make sure the form has fields that match the scraped data (e.g., address, price, link).
4. Run the Scraper

python scraper.py

The script will:

    Scrape property data.

    Open your Google Form in Chrome.

    Autofill the form for each property and submit it.

⚙️ Notes

    ChromeDriver must be installed and added to your system's PATH.

    The Chrome browser will stay open after execution due to detach=True.

    The target site used for scraping is a static mock page, ideal for practice.

