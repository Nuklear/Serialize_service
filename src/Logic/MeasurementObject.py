from src.Logic.Calculation.formulas import *


class MeasurementObject(object):
    def __init__(self, nominal_dimmension, upper_dev_limit, lower_dev_limit, resolution, data_array: list):
        self.nominal_dimmension = nominal_dimmension
        self.upper_dev_limit = upper_dev_limit
        self.lower_dev_limit = lower_dev_limit
        self.data_array = data_array
        self.upper_sec_limit = nominal_dimmension + upper_dev_limit
        self.lower_sec_limit = nominal_dimmension + lower_dev_limit
        self.tolerance = upper_dev_limit - lower_dev_limit
        self.resolution = resolution
        self.alpha = 0.05
        self.tolerance_portion = 0.2
        self.sigma_mult = 6
        self.real_dimension = 6.002

        self.first_formula_result = formula1(self.resolution, self.sigma_mult)
        self.second_formula_result = formula2(data_array)
        self.third_formula_result = formula3_4(data_array, self.second_formula_result)

    def calculation(self):
        first = formula13(
            self.alpha,
            self.tolerance_portion,
            self.tolerance,
            self.sigma_mult,
            len(self.data_array),
            self.third_formula_result)

        second = formula16(
            self.alpha,
            self.tolerance_portion,
            self.tolerance,
            self.second_formula_result,
            self.third_formula_result,
            len(self.data_array),
            self.real_dimension,
            self.sigma_mult
        )
        return [first, second]

    def get_result_json(self):
        j = {
                "characteristicId": "0a662382-6c1e-4386-8128-ee0f4b9a1ec9",
                "iso": {
                    "qms": formula7(
                                self.first_formula_result,
                                self.second_formula_result,
                                self.third_formula_result,
                                self.real_dimension,
                                self.tolerance
                            ),
                    "outliers": 0,
                    "uncertainties": [
                        {
                            "name": "ENV",
                            "value": self.third_formula_result,
                            "manualInput": None,
                            "active": None,
                            "notes": None
                        },
                        {
                            "name": None,
                            "value": None,
                            "manualInput": None,
                            "active": None,
                            "notes": null
                        }
                    ],
                    "ssigma": self.third_formula_result
                },
                "msa": null,
                "vda": null
            }
