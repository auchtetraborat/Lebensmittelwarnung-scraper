import requests
import json
from bs4 import BeautifulSoup

class WarningFeedUrl:
    SOURCE_STRING = "https://www.lebensmittelwarnung.de/bvl-lmw-de/opensaga/feed/{0}/{1}.rss"

    @classmethod
    def create(self, type: str, region: str) -> str:
        return self.SOURCE_STRING.format(type, region)


class WarningFeed:

    def __init__(self, url: str):
        self.url = url
        self.output = []
        self.__parse()

    def export_to_json(self) -> str: 
        return json.dumps([x.get_warning() for x in self.output])

    def __parse(self) -> None:
        # TODO proper error handling
        rss_soup = BeautifulSoup(self.__download(), 'xml')
        warnings = rss_soup.find_all('item')
        for warning_raw in warnings:
            self.output.append(Warning(warning_raw))
            
    def __download(self) -> str:
        # TODO proper error handling
        req = requests.get(self.url)
        return req.text

class Warning:
    def __init__(self, warning_raw):
        self.dict = {}
        self.__parse(warning_raw)

    def __parse(self, warning_raw) -> str:
        guid = warning_raw.find('guid').text
        self.dict['id'] = int(guid.split('/')[-1])
        self.dict['guid'] = guid
        self.dict['pubDate'] = warning_raw.find('pubDate').text
        
        cdata_soup = BeautifulSoup(warning_raw.find('content:encoded').text, 'html.parser')
        content_attrs = cdata_soup.find_all('b')
        for attr in content_attrs:
            attr_name = attr.text
            attr_value = str(attr.next_sibling).strip()
            if(attr_name == "Produktbezeichnung:"):
                self.dict['title'] = attr_value
            elif(attr_name == "Typ:"):
                self.dict['manufacturer'] = attr_value
            elif(attr_name == "Grund der Warnung:"):
                self.dict['warning'] = attr_value
            elif(attr_name == "Betroffene Länder:"):
                affected_arr = [x.strip() for x in attr_value.split(',')]
                self.dict['affectedStates'] = affected_arr
    
    def get_warning(self) -> dict:
        return self.dict
    
