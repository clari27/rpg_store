import random
import json

with open('shopkeeper\shopkeeper.json', encoding="utf8") as f:
   data = json.load(f)

class Shopkeeper:
    def __init__(self, greetings, barter_lvl):
        self.name = data["name"]
        self.greetings =greetings
        self.barter_lvl = barter_lvl

    @property
    def greetings(self):
        return self._greetings
    
    @property
    def barter_lvl(self):
        return self._barter_lvl

    @barter_lvl.setter
    def barter_lvl(self,barter_lvl):
        self._barter_lvl =barter_lvl

    @greetings.setter
    def greetings(self,greetings):
        self._greetings =greetings

shopkeeper=Shopkeeper(random.choice(data['greetings']), '5')

print(shopkeeper.barter_lvl)


