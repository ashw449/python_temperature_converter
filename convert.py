def celsius_to_fahrenheit(temperature):
    return temperature * (9/5) + 32 #Celsius to Fahrenheit
def celsius_to_kelvin(temperature):
    return temperature + 273 #Celsius to Kelvin
tempc = int(input("Enter the Temperature (in Celsius): ")) #Accepts temperature in as input.
tempf = celsius_to_fahrenheit(tempc) 
tempk = celsius_to_kelvin(tempc) 
print(f"The temperature in fahrehneit is: {tempf:.2f}") #Displays temperature in fahrenheit (rounded up to two decimal places).
print(f"The temperature in kevlin is: {tempf:.2f}") #Displays temperature in kelvin (rounded up to two decimal places).
