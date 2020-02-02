import requests as rq
import json

BASE_URL='https://www.foodrepo.org/api/v3'
API_KEY=''

def getProductByUPC(product_upc):

    ENDPOINT='/products/_search/'

    url = BASE_URL + ENDPOINT

    query = {
    "query": {
        "terms" : {
        "barcode" : [
            "%s" % product_upc
                    ]
                }
            }
    }

    headers = {
    'Authorization': "Token token=" + API_KEY,
    'Accept': 'application/json',
    'Content-Type': 'application/vnd.api+json',
    'Accept-Encoding': 'gzip,deflate'
    }

    r = rq.post(url, json=query, headers=headers)
    if r.status_code == 200:
        if len(r.json()['hits']['hits']) == 1:
            productInfo = {
                "id" : r.json()['hits']['hits'][0]['_source']['id'],
                "upc" : r.json()['hits']['hits'][0]['_source']['barcode'],
                "name" : r.json()['hits']['hits'][0]['_source']['display_name_translations']['de'],
                "quantity": r.json()['hits']['hits'][0]['_source']['quantity'],
                "unit" : r.json()['hits']['hits'][0]['_source']['unit']
            }

            print(productInfo)

            return productInfo

    return

