import math
from scipy.stats import t, norm
from scipy.stats.distributions import chi2


def formula1(RE, k):
    return (1 / (math.sqrt(3))) * (RE / 2)


def formula2(x_array):
    return (1 / len(x_array)) * sum(x_array)


def formula3_4(x_array, x_d):
    s = sum(map(lambda x: math.pow(x - x_d, 2), x_array))
    return math.sqrt((1 / (len(x_array) - 1)) * s)


def formula5(formula2_result, x_m):
    return formula2_result - x_m


def formula6(formula3_result, formula5_result):
    f = math.pow(formula3_result, 2)
    s = math.pow(((1 / math.sqrt(3)) * formula5_result), 2)
    return math.sqrt(f + s)


def formula7(formula1_result, formula2_result, formula3_result, x_m):
    f = math.pow(formula1_result, 2)
    s = math.pow(formula3_result, 2)
    t = math.pow(((1 / math.sqrt(3)) * formula2_result - x_m), 2)
    return math.sqrt(f + s + t)


def formula8(formula2_result, formula3_result, array_len, value):
    f = formula2_result
    s = formula3_result / math.sqrt(array_len)
    third = t.pdf(value, array_len - 1)
    return f + s * third


def formula9(formula2_result, formula3_result, array_len, value):
    f = formula2_result
    s = formula3_result / math.sqrt(array_len)
    third = norm(value, 0.1)
    return f + s * third


def formula10(value, array_len, formula3_result):
    f = (array_len - 1) / chi2.sf(1 - value, array_len - 1)
    return math.sqrt(f) * formula3_result


def formula11(Tp, T, k, formula3_result):
    return (Tp * T) / (k * formula3_result)


def formula12(value, Tp, T, k, array_len, formula3_result):
    f = Tp * T
    s = k * (formula10(value, array_len, formula3_result))
    return f / s


def formula13(alpha, Tp, T, k, array_len, formula3_result):
    return [formula12(alpha / 2, Tp, T, k, array_len, formula3_result),
            formula11(Tp, T, k, formula3_result),
            formula12(1 - alpha / 2, Tp, T, k, array_len, formula3_result),
            ]


def formula14(Tp, T, formula2_result, x_m, k, formula3_result):
    f = (Tp / 2) * T - (math.fabs(formula2_result - x_m))
    s = (k / 2) * formula3_result
    return f / s


def formula15(Tp, T, formula2_result, formula3_result, array_len, value, x_m, k):
    f = Tp * T - (math.fabs(formula8(formula2_result, formula3_result, array_len, value) - x_m))
    s = k / 2 * formula10(1 - value, array_len, formula3_result)
    return f / s


def formula16(alpha, Tp, T, formula2_result, formula3_result, array_len, x_m, k):
    return [
        formula15(Tp, T, formula2_result, formula3_result, array_len, alpha / 2, x_m, k),
        formula14(Tp, T, formula2_result, x_m, k, formula3_result),
        formula15(Tp, T, formula2_result, formula3_result, array_len, 1 - alpha / 2, x_m, k),
    ]


def formula17(formula1_result, formula2_result, formula3_result, x_m, T):
    f = 4 * formula7(formula1_result, formula2_result, formula3_result, x_m)
    return f / T
