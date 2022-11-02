import random
import json

with open('shopkeeper\shopkeeper.json', encoding="utf8") as f:
   data = json.load(f)


class Shop:
    def __init__(self,open_hours):
        self.open_hours = open_hours
