# This function converts temperature in Celsius (°C) to Fahrenheit (°F)
def cel2fahr():
    temp_c = input('Temperature in Celsius: ')
    try:
        temp_f = int(temp_c) * 9 / 5 + 32
        print("{temp_c}°C = {temp_f}°F".format(temp_c=temp_c, temp_f=temp_f))
    except:
        print('Enter a valid number: ')

# This function converts temperature in Fahrenheit (°F) to Celsius (°C)
def fahr2cel():
    temp_f = input('Temperature in Fahrenheit: ')
    try:
        temp_c = (int(temp_f) - 32) * 5 / 9
        print("{temp_f}°F = {temp_c}°C".format(temp_f=temp_f, temp_c=temp_c))
    except:
        print('Enter a valid number: ')
