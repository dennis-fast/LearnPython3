temp_c = input('Temperature in Celsius: ')
try:
    temp_f = int(temp_c) * 9 / 5 + 32
    print("{temp_c}°C = {temp_f}°F".format(temp_c=temp_c, temp_f=temp_f))
except:
    print('Enter a valid number: ')
