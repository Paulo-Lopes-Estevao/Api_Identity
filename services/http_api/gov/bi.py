from services.http_api.http_service import http
import services.http_api.point_url as url

class bi_service():

    Q ="/bi/?bi="

    def __init__(self):
        self.api_service = http()

    def verification_bi(self,bi):
        url_= f"{url.endPointGov()}{self.Q}{bi}"
        self.api_service.api(url_)
        return self.api_service.response()