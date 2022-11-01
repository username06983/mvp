import requests
import pandas as pd
from requests import get

req = get(
  url = "https://www1.nseindia.com/content/historical/EQUITIES/2022/OCT/cm11OCT2022bhav.csv.zip",
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
webpage = req.text
webpage
