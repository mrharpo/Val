from fastapi import FastAPI, Body
from requests import get
from pydantic import AnyHttpUrl
from xmlschema import XMLSchema

app = FastAPI()

pbcore = XMLSchema('pbcore-2.1.xsd')


@app.post('/validate')
def validatePBCore(url: AnyHttpUrl = Body(...)):
    xml = get(url).text
    return pbcore.is_valid(xml)


if __name__ == '__main__':
    from uvicorn import run

    run(app)
