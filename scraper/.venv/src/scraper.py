import urllib.request
from bs4 import BeautifulSoup


def scraper():
    """
      Scrape https://developer.mozilla.org/en-US/docs/Web/HTML/Element
      for the list of all HTML elements and the categories they're a part
      of (non-standard, deprecated, experimental)
    """
    data = []

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
        print(index, list_item)


scraper()
