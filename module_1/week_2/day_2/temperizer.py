"""An example library for converting temperatures."""


def convert_f_to_c(temp_f):
    """Convert Fahrenheit to Celsius."""
    temp_c = (temp_f - 32) * (5/9)
    return temp_c


def convert_c_to_f(temp_c):
    """Convert Celsius to Fahrenheit."""
    temp_f = (temp_c * 9/5) + 32
    return temp_f


def convert_c_to_k(temp_c):
    """Convert Celsius to Kelvin"""
    temp_k = (temp_c + 273.15)
    return temp_k


def convert_f_to_k(temp_f):
    """Convert Farenheit to Kelvin"""
    temp_k = (temp_f + 459.67) * 5/9
    return temp_k


def convert_k_to_c(temp_k):
    """Convert Kelvin to Celsius"""
    temp_c = (temp_k - 273.15)
    return temp_c


def convert_k_to_f(temp_k):
    """Convery Kelvin to Farenheit"""
    temp_f = ((temp_k - 273.15) * 9/5) + 32
    return temp_f

#make a function in your temperizer that will take a temp in F, and print out:

def write_f_in_c_and_k(temp_f):
    temp_c = convert_f_to_c(temp_f)
    temp_k = convert_f_to_k(temp_f)  
    print(f"""The temperature {temp_f}F is:
             - {temp_c} in C
             - {temp_k} in k""")
