import abc
import requests

class http(abc.ABC):

    __url = None

    def __init__(self):
        pass

    def api(self,url):

        url_api = self.__url = requests.get(url)

        try:

            url_api.raise_for_status()

        except Exception as e:
            print("erro : %s" % (e))


    def response(self):
        #self.__url.status_code == requests.codes.ok
        return self.__url.json()