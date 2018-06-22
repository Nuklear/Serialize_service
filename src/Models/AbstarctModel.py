import json
from aiohttp_ultrajson import jsonify


class AbstractModel(object):
    def to_json(self):
        d = json.dumps(self.__dict__)
        return d

    def from_json(self, raw_json):
        assert raw_json is not None
        assert isinstance(raw_json, str)

        for k, v in json.loads(raw_json).items():
            print("{0} - {1}".format(k, v))
            self.__setattr__(k, v)

