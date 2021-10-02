import abc
import requests

class http(abc.ABC):
    def __init__(self):
        self.__url = None

    def api(self, url):
        url_api = self.__url = requests.get(url)
        try:
            url_api.raise_for_status()
        except Exception as e:
            print(f"erro : {e}")


    def response(self):
        #self.__url.status_code == requests.codes.ok
        return self.__url.json()