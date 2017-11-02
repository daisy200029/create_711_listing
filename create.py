#/usr/bin/env python
import requests

fd = open("OUT.png", "rb")

url = "https://stage.carousell.io/api/3.1/listings/"

payload = { 
 "mailing": "false",
 "meetup":"false",
 "shipping_tw_711":"true",
 "title":"ha6",
 "price":117.0,
 "condition":1,
 "collection_id":1113,
 "size": "WOMEN_BOTTOMS_FREESIZE",
}

files = {
    "photo_0": fd
}

headers = {
    'authorization': "Token 369e52be163522b9f4bb5ee27786d90112220fa4",
    'platform': "ios",
    }

response = requests.post(url, data=payload, files=files, headers=headers)

print response.json
