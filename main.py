import requests
from bs4 import BeautifulSoup

url = "https://pypi.org/search/?c=Programming+Language+%3A%3A+Python&o=&q=&page="
host_url = "https://pypi.org"

class WebParser:
    def __init__(self, url):
        self.url = url
        self.html_page = ''
        self.subpage_url = []
        self.library_name = []
        self.author = []
        self.stars = []
        self.forks = []
        self.requires = []
        self.size = []
        self.all_info = {'library_name':[], 'Author':[], 'Stars':[], 'Forks':[], 'Requires':[], 'Size':[]}

    def get_html_page(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.html_page = response.text
            print('got page! status code:', response.status_code)
        else:
            print('get html failed, failed code:', response.status_code)
            return None
    def parse_main_page(self):
        self.get_html_page()
        # Use BeautifulSoup to parse the HTML response
        soup = BeautifulSoup(self.html_page, "html.parser")
        a_tags = soup.find_all('a', {'class': 'package-snippet'})
        for a_tag in a_tags:
            href = a_tag.get('href')
            self.subpage_url.append(host_url + href)
        print(self.subpage_url)
    def get_subpage_info(self):

        pass


class Downloader:
    def __init__(self, url):
        pass

def get_pkg_url(url, page_num):
    pkg_urls = []
    pass
    return pkg_urls

def get_parsed_info(WebParser):
    pass
# Loop through each library element and extract its information
# for i in range(100):
#     library = library_elements[i]
#     name = library.find("span", class_="package-snippet__name").text
#     author = library.find("span", class_="package-snippet__user").text
#     date = library.find("span", class_="package-snippet__released").text
#     size = library.find("span", class_="package-snippet__size").text
#     library_info.append((name, author, date, size))
#
# # Print the information of the first 100 libraries
# for i, library in enumerate(library_info):
#     print(f"Library {i+1}:")
#     print(f"Name: {library[0]}")
#     print(f"Author: {library[1]}")
#     print(f"Date: {library[2]}")
#     print(f"Size: {library[3]}")
#     print()
#
if __name__ == '__main__':
    num_page = 1
    for i in range(num_page):
        parser = WebParser(url+str(i+1))
        parser.parse_main_page()