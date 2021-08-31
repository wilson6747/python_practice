#Gets user input
print()
temp_input = float(input('What is the temperature? : '))
temp_type = input('Farenheit or Celcius (F/C)? : ')

#celcius convert function
def cel_convert(temp_input):
      temp_input = (temp_input * (9 / 5) + 32)
      return temp_input

#If temp type is celcius, convert to farenheit
if temp_type.upper() == 'C':
    temp_input = cel_convert(temp_input)

#Wind chill function
#Computes wind chill at each variable of wind speed
#EQUATION: 35.74 + 0.6215T - 35.75(V^0.16) + 0.4275T(V^0.16)
wind_speed = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

def wind_chill_function(temp_input, wind_speed):
    wind_chill = (35.74 + (0.6215 * temp_input) - 35.75 * (speed**0.16) + ((0.4275 * temp_input) * (speed**0.16)))
    print(f'At temperature {temp_input:.1f}F, and wind speed {speed} mph, the windchill is: {wind_chill:.2f}F')

for speed in wind_speed:
    wind_chill_function(temp_input, wind_speed)






