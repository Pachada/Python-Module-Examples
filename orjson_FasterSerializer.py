#https://github.com/ijl/orjson
import orjson
from pprint import pprint
from datetime import datetime

def date_formatter(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%a, %d %b %Y %H:%M:%S GMT")
    raise TypeError


data = {
    "date": datetime.utcnow(),
    "name": "test",
    "float": 1.1,
    "int": 1
}

result = orjson.dumps(data, option=orjson.OPT_PASSTHROUGH_DATETIME,default=date_formatter)
pprint(result)
