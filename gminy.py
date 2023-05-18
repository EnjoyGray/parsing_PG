import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from time import sleep
from random import randint


def start_url():
    """
    Function to set the starting URL and initiate the page processing for each city.
    """
    link = r'https://www.polskawliczbach.pl/'

    # Load city data from a JSON file
    with open('files/data_base_url.json', 'r') as f:
        city = json.load(f)

    # Load existing project data
    project_data_list = read_existing_data()

    # Iterate over cities
    for i in city:
        sleep(randint(1, 3))
        url = link + i
        headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; C6503)"
                                 "AppleWebKit/537.36 (KHTML, like Gecko)"
                                 "Chrome/81.0.4044.117 Mobile Safari/537.36"}

        req = requests.get(url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
        parse_miasta(soup, project_data_list)


def read_existing_data():
    """
    Function to read existing project data from a JSON file.
    If the file is not found, an empty list is returned.
    """
    try:
        with open('pliki/data_base.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def parse_miasta(soup, project_data_list):
    """
    Function to parse the HTML page of a city and save the relevant project data.
    """
    sleep(randint(1, 2))
    miasta = soup.find_all("div", class_="panel panel-primary cp-main")
    gps = soup.find_all("div", class_="panel panel-primary cp-main")
    spans = []

    for item in miasta:
        try:
            miasto_name = item.find("li", class_="hdr").find("b")
        except Exception:
            miasto_name = "ERROR BS4 miasto!!!"

    for cords in gps:
        try:
            x = cords.find("ul", class_="list-group",
                           style="text-align:left;margin-bottom:0").find("li")
            y = cords.find("ul", class_="list-group",
                           style="text-align:left;margin-bottom:0").find_next("li")
            teryt = cords.find("ul", class_="list-group",
                               style="text-align:left;margin-bottom:0") \
                .find_next("li", class_="gray").find('span')
        except Exception:
            print("ERROR in GSP!!!")

    for span in soup.find_all('span'):
        spans.append(span.text.strip())

    project_data_list.append(
        {
            "nazwa gminy": miasto_name.text.strip(),
            "Liczba mieszkancow": spans[6],
            "Powierzchnia": spans[7].replace('km²', '').strip(),
            "x": x.text.strip()[7:14],
            "y": y.text.strip()[:7],
            "TERYT (TERC)": teryt.text.strip(),
        }
    )

    df = pd.DataFrame(project_data_list)
    df.to_excel('pliki/data_base.xlsx')
    df.to_json("pliki/data_base.json", orient="records", indent=4)
    print(df)


def main():
    """
    Main function of the program that initiates the data processing.
    """
    start = time.time()
    start_url()
    end = time.time()
    total = end - start
    print("Elapsed time: ", "%.2f" % total)


if __name__ == '__main__':
    main()
