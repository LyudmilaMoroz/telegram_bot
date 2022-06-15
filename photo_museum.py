import requests
import bs4


def get_current_exhibition(url):
    response = requests.get(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                               'Chrome/99.0.4844.74 Safari/537.36'
                 }
    )
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")

    events = soup.select('h3 a')
    event_names_list = [event.text for event in events]

    event_dates = soup.find_all(class_="date-display-range")
    event_dates_list = [date.text for date in event_dates]

    event_descriptions = soup.find_all(class_="field-name-field-liftup-text")
    event_descriptions_list = [description.text for description in event_descriptions]

    all_events = ""
    for n in range(len(event_names_list)):
        all_events += f"Name: {event_names_list[n]}.\nDate: {event_dates_list[n]}\nDescription: {event_descriptions_list[n]} \n\n"

    return all_events


