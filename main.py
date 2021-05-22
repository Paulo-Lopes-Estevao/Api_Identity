from fastapi import FastAPI
from services.http_api.gov.bi import bi_service
from services.http_api.gov.nif import nif_service
from domain.validation.bi import Bi

app = FastAPI()

valid_bi = Bi()
service_bi = bi_service()
service_nif = nif_service()

def instance_bi(bi):
    verify_validation = valid_bi.rules(bi)
    if verify_validation is not False:
        verify_service = service_bi.verification_bi(bi)
        return verify_service


def instance_nif(nif):
    verify_validation = valid_bi.rules(nif)
    if verify_validation is not False:
        verify_service = service_nif.verification_nif(nif)
        return bool(verify_service)


    

@app.get("/")
def read_root():
    return {
        "Name": "Paulo Lopes Estevão",
        "Developer": "Back-End Developer",
        "Repository": "https://github.com/Paulo-Lopes-Estevao/Api_Identity",
        "Midia Social":{
            "Github":"https://github.com/Paulo-Lopes-Estevao",
            "Facebook":"https://facebook.com/paulodoposter.poster.1",
            "Linkedin":"https://www.linkedin.com/in/paulo-lopes-estev%C3%A3o-7a70881b4/",
            "Telegram":"https://t.me/Paulo_LopesEstevao"
    },


    }



@app.get("/bi/{bi}")
def read_bi(bi : str):
    return instance_bi(bi)

@app.get("/nif/{nif}")
def read_nif(nif : str):
    return instance_nif(nif)