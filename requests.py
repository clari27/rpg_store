import requests
import json

BASE_URL="http://127.0.0.1:5000/"

response=requests.put(BASE_URL + "/stock/36", {'shop_id': 0, 'shop_name': "Pierre's General Store", 'product_id': 36, 'product_name': 'Pepper Seeds', 'quantity': 1, 'price': 40,  'description': 'Plant these in the summer. Takes 5 days to mature, and continues to produce after first harvest.', 'avaliability_start': '', 'avaliability_period': 'summer'})
input()
response=requests.get(BASE_URL + "stock/36")

print(response.json())

