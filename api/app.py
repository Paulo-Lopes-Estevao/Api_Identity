from fastapi import FastAPI
#from services.http_api.gov.bi import bi_service
#from services.http_api.gov.nif import nif_service
#from domain.validation.bi import Bi


app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/bi/{bi}")
async def read_bi(bi:str):
    return {"Hello": "World", "bi":bi}