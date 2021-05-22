from fastapi import FastAPI
#from services.http_api.gov.bi import bi_service
#from services.http_api.gov.nif import nif_service
from domain.validation.bi import Bi

app = FastAPI()


def instance_bi(bi):
    valid_bi = Bi()
    verify = valid_bi.rules(bi)
    if verify is True:
        return {"Hello": "World", "bi":bi}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/bi/{bi}")
async def read_bi(bi : str):
    await instance_bi(bi)