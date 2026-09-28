def convert_to_fahrenheit(temperature):
    return tempc * (9/5) + 32
tempc = int(input("Enter the Temperature (in Celsius): ")) #Accepts temperature in as input.
tempf = convert_to_fahrenheit(tempc)
print(f"The temperature in fahrehneit is: {tempf:.2f}") #Displays temperature in fahrenheit (rounded up to two decimal places).
