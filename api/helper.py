import numpy as np
import math

import locale

def rupiah_format(angka, with_prefix=False, desimal=0):
    locale.setlocale(locale.LC_NUMERIC, 'id_ID.utf8')
    rupiah = locale.format_string("%.*f", (desimal, angka), True)
    if with_prefix:
        return "Rp. {}".format(rupiah)
    return rupiah


# assume value is a decimal
def transform_to_rupiah_format(value):

    if math.isnan(value):
        return np.nan
    value = float(int(value))
    str_value = str(value)

    unit = ''
    show_result = ''


    separate_decimal = str_value.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    if len(str_value) >= 15:
        unit = 'M'
        show_result = temp_result.split('.')[0] + temp_result.split('.')[1] + "," + temp_result.split('.')[1][0]
    elif len(str_value) >= 12:
        unit = 'M'
        show_result = temp_result.split('.')[0] + "," + temp_result.split('.')[1][0]
    elif len(str_value) >= 8:
        unit = 'JT'
        show_result = temp_result.split('.')[0]
    elif len(str_value) >= 5:
        unit = 'RB'
        show_result = temp_result.split('.')[0]
    else:
        unit = ''
        show_result = temp_result.split('.')[0]


    return "Rp " + show_result + unit



# assume value is a decimal
def transform_to_rupiah(value):
    if math.isnan(value):
        return np.nan
    value = float(int(value))
    str_value = str(value)
    unit = ''
    show_result = ''


    separate_decimal = str_value.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    if len(str_value) >= 15:
        unit = 'M'
        show_result = temp_result.split('.')[0] + temp_result.split('.')[1] + "," + temp_result.split('.')[1][0]
    elif len(str_value) >= 12:
        unit = 'M'
        show_result = temp_result.split('.')[0] + "," + temp_result.split('.')[1][0]
    elif len(str_value) >= 8:
        unit = 'JT'
        show_result = temp_result.split('.')[0]
    elif len(str_value) >= 5:
        unit = 'RB'
        show_result = temp_result.split('.')[0]
    else:
        unit = ''
        show_result = temp_result.split('.')[0]


    return "Rp " + show_result + unit

def transform_format(value):
    
    if math.isnan(value):
        return np.nan
    value = float(int(value))
    str_value = str(value)
    separate_decimal = str_value.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    #return "Rp " + temp_result + "," + before_decimal
    return temp_result

def transform_to_format(value):
    
    if math.isnan(value):
        return np.nan
    value = float(int(value))
    str_value = str(value)
    unit = ''

    separate_decimal = str_value.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    if len(str_value) >= 12:
        unit = 'jt'
        show_result = temp_result.split('.')[0] + "." + temp_result.split('.')[1] 
    elif len(str_value) >= 9:
        unit = 'jt'
        show_result = temp_result.split('.')[0] + "," + temp_result.split('.')[1][0]
    elif len(str_value) >= 6:
        unit = 'rb'
        show_result = temp_result.split('.')[0] + "," + temp_result.split('.')[1][0]
    else:
        unit = ''
        show_result = temp_result.split('.')[0]
        
    return show_result + unit
