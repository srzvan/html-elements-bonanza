import json
import urllib.request
from bs4 import BeautifulSoup


def scraper():
    """
        Scrape https://developer.mozilla.org/en-US/docs/Web/HTML/Element
        for the list of all HTML elements and the categories they're a part
        of (non-standard, deprecated, experimental)
    """
    elements = []
    element_categories = None

    with urllib.request.urlopen(
            'https://developer.mozilla.org/en-US/docs/Web/HTML/Element'
    ) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

    sidebar_heading = soup.find("summary", string="HTML elements")
    html_elements_list = sidebar_heading.find_next_sibling('ol')

    element_categories = populate_category_list(html_elements_list)

    for _, list_item in enumerate(html_elements_list):
        elements.append(create_data_item(list_item))

    return {"categories": element_categories, "elements": elements}


def create_data_item(soup_element):
    html_element = {"name": soup_element.a['href'].split('/')[-1]}

    categories = soup_element.find_all('abbr')
    for category in categories:
        key = category['title'].split('.')[0].lower()
        html_element[key] = True

    return html_element


def populate_category_list(soup_element):
    categories = [{
        "description": category['title'],
        "name": category['title'].split('.')[0].lower()
    } for category in soup_element.find_all('abbr')]

    return [
        dict(t) for t in {tuple(category.items())
                          for category in categories}
    ]


def write_to_json(data):
    with open('../../../json/htmlElementReference.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)


write_to_json(scraper())

scraper()
