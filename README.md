# Parsing_BeautifulSoup
# Polskawliczbach Data Scraper

This is a Python script that scrapes data from the website "https://www.polskawliczbach.pl/" and extracts information about cities in Poland, including population, area, and GPS coordinates. The scraped data is then stored in JSON and Excel files.

## Usage

1. Clone the repository or download the code.
2. Install the required Python packages by running the following command:
3. Prepare the necessary input files:
- Create a JSON file named `data_base_url.json` in the `files` directory and populate it with the list of city codes to scrape data for.
- (Optional) If you have existing project data, create a JSON file named `data_base.json` in the `pliki` directory and populate it with the existing data in JSON format.

4. Run the script `main.py` using the following command:

This will start the data scraping process, where the script will visit each city's page, extract the relevant information, and save it in JSON and Excel files (`data_base.json` and `data_base.xlsx`, respectively).

5. Once the script finishes running, you can find the scraped data in the `pliki` directory.

## Additional Notes

- The script utilizes the `requests`, `beautifulsoup4`, and `pandas` libraries, which can be installed using the provided `requirements.txt` file.
- Make sure to respect the website's terms of use and avoid sending too many requests in a short period of time. The script includes random delays between requests to prevent excessive traffic.
- Feel free to modify the code according to your specific requirements or use it as a starting point for your own data scraping projects.

Please note that this script is provided as-is and the usage is at your own risk. Refer to the license file for more information.

