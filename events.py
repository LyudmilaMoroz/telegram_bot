import requests
import bs4

# with open("event.html", "w", encoding="utf-8") as file:
#   file.write(response.text)
# with open("event.html", "r", encoding="utf-8") as file:
#    text = file.read()
main_link = "https://allevents.in/helsinki/"


def get_events(choice):
    url = main_link + choice
    response = requests.get(
        url,
        headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                               'Chrome/99.0.4844.74 Safari/537.36'
                 }
    )
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")

    if choice == 'business' or choice == 'health-wellness' or choice == 'sports' or choice == 'performances':
        events = soup.select("div.title a[href] h3")
        event_names_list = [event.text for event in events]

        event_addresses = soup.find_all(class_="up-venue toh")
        event_address_list = [address.text.strip() for address in event_addresses]

        links = soup.select("div.title a[href]")
        event_links = [link["href"] for link in links]

        all_events = ""
        for n in range(len(event_names_list) - 1):
            all_events += f"Name: {event_names_list[n]}.\nAddress: {event_address_list[n]}.\nRead more: {event_links[n]}\n\n"

        return all_events

    else:
        events = soup.select("div.title a[href] h3")
        event_names_list = [event.text for event in events]

        event_dates = soup.find_all(class_="up-time-display")
        event_dates_list = [date.text.strip() for date in event_dates]

        event_addresses = soup.find_all(class_="up-venue toh")
        event_address_list = [address.text.strip() for address in event_addresses]

        links = soup.select("div.title a[href]")
        event_links = [link["href"] for link in links]

        all_events = ""
        for n in range(len(event_names_list) - 1):
            all_events += f"Name: {event_names_list[n]}.\nDate: {event_dates_list[n]}." \
                          f"\nAddress: {event_address_list[n]}.\nRead more: {event_links[n]}\n\n"

        return all_events


if __name__ == '__main__':
    import sys
    choice = ' '.join(sys.argv[1:])
    if not choice:
        choice = 'events'
