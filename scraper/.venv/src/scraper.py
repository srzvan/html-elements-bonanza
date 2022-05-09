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
    element_categories = []

    with urllib.request.urlopen('https://developer.mozilla.org/en-US/docs/Web/HTML/Element') as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

    sidebar_heading = soup.find("h4", class_='sidebar-heading')
    sidebar_ol = sidebar_heading.find_next_sibling('div').ol

    nested_list_item = None
    for index, list_item in enumerate(sidebar_ol):
        if index == 13:
            nested_list_item = list_item
            break

    html_elements_list = nested_list_item.details.ol
    for index, list_item in enumerate(html_elements_list):
        elements.append(create_data_item(list_item))
        populate_category_list(element_categories, list_item)

    return {"categories": element_categories, "elements": elements}

def create_data_item(soup_element):
    html_element = {"name": soup_element.a['href'].split('/')[-1]}

    categories = soup_element.find_all('abbr')
    for category in categories:
        key = category['title'].split('.')[0].lower()
        html_element[key] = True

    return html_element

def populate_category_list(list, soup_element):
    categories = soup_element.find_all('abbr')

    for category in categories:
        description = category['title']
        name = description.split('.')[0].lower()
        category = {"name": name, "description": description}

        if(list.count(category) > 0):
            continue
        else:
            list.append(category)

def write_to_json(data):
    with open('../../../json/data.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

write_to_json(scraper())
