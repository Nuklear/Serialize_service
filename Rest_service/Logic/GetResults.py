from Rest_service.Logic.MeasurementObject import MeasurementObject
from Rest_service.Logic.GetDataFromJson import GetDataFromJson


def get_data_from_json(raw_json):
    results = {}
    data = GetDataFromJson(raw_json)
    ids = data.get_all_ids()
    for id in ids:
        data_dict = data.get_data_for_calc(id)
        m_data = MeasurementObject(
            data_dict['nominal_dimmen'],
            data_dict['upper_dev_limit'],
            data_dict['lower_dev_limit'],
            data_dict['resolution'],
            data.get_data_array(id)
        )
        results[id] = m_data.calculation()
    print(results)
    return results