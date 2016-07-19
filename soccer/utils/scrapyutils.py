import json
from scrapy import Item
def extract(sel):
    return "".join(sel.extract()).strip();


class ItemEncoder(json.JSONEncoder):
    def default(self, obj):  
        if isinstance(obj, Item) :
            return dict(obj)
        return json.JSONEncoder.default(self, obj)  