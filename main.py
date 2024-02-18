from datetime import datetime
import requests
from pydantic import BaseModel
from typing import Union
from fastapi import FastAPI
from get_html_data import get_data


app = FastAPI()

#ip = '10.222.53.38'

@app.get("/get/{ip}")

async def read_get(ip):
    now = datetime.now()
    return {
        "IP": [ip],
        "Date": [now],
        "AKB": [get_data(ip, 'AKB')],
        "V": [get_data(ip, 'V')],
        "Temperature": [get_data(ip, 'T')]
           }
