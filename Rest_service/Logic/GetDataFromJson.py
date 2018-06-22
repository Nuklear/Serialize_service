import json


class GetDataFromJson(object):
    def __init__(self, data_json):
#        self.dict_json = json.loads(data_json)
        self.dict_json = data_json

    def get_data_array(self, id):
        values = []
        data = self.dict_json.get('experimentType1Data').get('table')
        for d in data:
            if d.get('characteristicId') == id:
                values = [i.get('value') for i in d.get('cells')]
        return values

    def get_all_ids(self):
        return [i.get('characteristicId') for i in self.dict_json.get("measurementTask").get('characteristics')]

    def get_data_for_calc(self, id):
        data_dict = {}
        data = self.dict_json.get('measurementTask').get('characteristics')
        for d in data:
            if d.get('characteristicId') == id:
                data_dict['nominal_dimmen'] = d.get('nominalValue')
                data_dict['upper_dev_limit'] = d.get('upperProcessLimit').get('value')
                data_dict['lower_dev_limit'] = d.get('lowerProcessLimit').get('value')

        data = self.dict_json.get('measurementSystem').get('characteristics')
        for d in data:
            if d.get('characteristicId') == id:
                data_dict['resolution'] = d.get('resolution')

        return data_dict

