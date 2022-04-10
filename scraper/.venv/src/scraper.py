import urllib.request
from bs4 import BeautifulSoup

# data items
# {
#   name: string
#   deprecated:boolean
#   non-standard: boolean
#   experimental: boolean
# }

# selector
# '.sidebar-inner > div > ol > li:nth-child(7) ol'
data = []

with urllib.request.urlopen('https://developer.mozilla.org/en-US/docs/Web/HTML/Element') as response:
   html = response.read()
   soup = BeautifulSoup(html, 'html.parser')

   sidebar_heading = soup.find("h4", class_='sidebar-heading')
   sidebar_ol = sidebar_heading.find_next_sibling('div').ol

  #  print(sidebar_ol)

   html_elements_list = None
   for index, list_item in enumerate(sidebar_ol):
      if index == 6:
        print(list_item)
        html_elements_list = list_item
        break

  #  print(html_elements_list)
