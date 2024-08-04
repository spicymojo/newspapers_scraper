import requests
import datetime
from bs4 import BeautifulSoup
import newspapers

# Define variables
web_base_url = 'https://fiuxy2.co/'
general_base_url = 'forums/prensa-diaria.12'
thread_prefix = '/threads/diarios-de-espa%C3%B1a-individuales-'
uncoded_n = '%C3%B1'

def fetch_and_parse_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print(f'Failed to retrieve the page. Status code: {response.status_code}')
        return None

def get_today_thread_link(soup):
    a_tags = soup.find_all('a', href=True)
    todays_day_number = datetime.datetime.now().strftime("%d").lstrip('0')
    for tag in a_tags:
        if tag['href'].startswith(thread_prefix + todays_day_number):
            return tag['href'].replace(uncoded_n, 'ñ')

def get_today_thread_url():
    soup = fetch_and_parse_url(web_base_url + general_base_url)
    if soup:
        return web_base_url + get_today_thread_link(soup)
def print_bbWrapper_contents(soup):
    if soup:
        bb_wrappers = soup.find_all(class_='bbWrapper')
        for wrapper in bb_wrappers:
            print(wrapper.get_text())

def main():
    today_thread_url = get_today_thread_url()
    if today_thread_url:
        soup = fetch_and_parse_url(today_thread_url)
        news_groups = newspapers.find_wanted_newspapers(soup)
        for group in news_groups:
            print(group)

if __name__ == "__main__":
    main()