# Checks if the value is an integer or not, removing the decimal point and the trailing zeroes if the value is an integer.
def check_integer(value):
    if value.is_integer(): 
        return int(value)
    else:
        return value

def celsius_to_fahrenheit(celsius):
    return celsius * (9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_rankine(celsius):
    return (celsius + 273.15) * (9/5)

def celsius_to_reaumur(celsius):
    return celsius * (4/5)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def fahrenheit_to_rankine(fahrenheit):
    return fahrenheit + 459.67

def fahrenheit_to_reaumur(fahrenheit):
    return (fahrenheit - 32) * (4/9)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def kelvin_to_rankine(kelvin):
    return kelvin * (9/5)

def kelvin_to_reaumur(kelvin):
    return kelvin_to_celsius(kelvin) * (4/5)

def rankine_to_celsius(rankine):
    return (rankine - 491.67) * (5/9)

def rankine_to_fahrenheit(rankine):
    return rankine - 459.67

def rankine_to_kelvin(rankine):
    return rankine * (5/9)

def rankine_to_reaumur(rankine):
    return (rankine - 491.67) * (4/9)

def reaumur_to_celsius(reaumur):
    return reaumur * (5/4)

def reaumur_to_fahrenheit(reaumur):
    return reaumur * (9/4) + 32

def reaumur_to_kelvin(reaumur):
    return  reaumur_to_celsius(reaumur) + 273.15

def reaumur_to_rankine(reaumur):
    return reaumur * (9/4) +  491.67

scales = {
    1: ("celsius", "c", "degrees celsius"),
    2: ("fahrenheit", "f", "degrees fahrenheit"),
    3: ("kelvin", "k"),
    4: ("rankine", "r", "degrees rankine"),
    5: ("reaumur", "re", "degrees reaumur")
}

print("Python temperature converter")
scale = input("Select a scale (Celsius, Fahrenheit, Kelvin, Rankine, or Reaumur), or type 'list': ").strip().lower()

if scale == "list":
    print("Available scales include: ")
    for key, value in scales.items():
        # Fixed SyntaxError: Changed internal double quotes to single quotes
        print(f"{key}: {', '.join(value)}") 

# 4. Search for the user input inside the scales dictionary
else:
    found = False
    primary_scale = None
    
    for key, value in scales.items():
        if scale == str(key) or scale in value:
            primary_scale = key
            found = True
            break # Exit the loop once found

    if found and primary_scale == 1:
        temp = float(input("Enter the Temperature (in Celsius): "))
        print(f"{check_integer(temp)} degrees Celsius is {check_integer(celsius_to_fahrenheit(temp))} Degrees Fahrenheit.")
        print(f"{check_integer(temp)} degrees Celsius is {check_integer(celsius_to_kelvin(temp))} Kelvin.")
        print(f"{check_integer(temp)} degrees Celsius is {check_integer(celsius_to_rankine(temp))} Degrees Rankine.")
        print(f"{check_integer(temp)} degrees Celsius is {check_integer(celsius_to_reaumur(temp))} Degrees Reaumur.")
    elif found and primary_scale == 2:
            temp = float(input("Enter the Temperature (in Fahrenheit): "))
            print(f"{check_integer(temp)} degrees Fahrenheit is {check_integer(fahrenheit_to_celsius(temp))} Degrees Celsius.")
            print(f"{check_integer(temp)} degrees Fahrenheit is {check_integer(fahrenheit_to_kelvin(temp))} Kelvin.")
            print(f"{check_integer(temp)} degrees Fahrenheit is {check_integer(fahrenheit_to_rankine(temp))} Degrees Rankine.")
            print(f"{check_integer(temp)} degrees Fahrenheit is {check_integer(fahrenheit_to_reaumur(temp))} Degrees Reaumur.")
    elif found and primary_scale == 3:
                temp = float(input("Enter the Temperature (in Kelvin): "))
                print(f"{check_integer(temp)} Kelvin is {check_integer(kelvin_to_celsius(temp))} Degrees Celsius.")
                print(f"{check_integer(temp)} Kelvin is {check_integer(kelvin_to_fahrenheit(temp))} Degrees Fahrenheit.")
                print(f"{check_integer(temp)} Kelvin is {check_integer(kelvin_to_rankine(temp))} Degrees Rankine.")
                print(f"{check_integer(temp)} Kelvin is {check_integer(kelvin_to_reaumur(temp))} Degrees Reaumur.")
    elif found and primary_scale == 4:
                temp = float(input("Enter the Temperature (in Rankine): "))
                print(f"{check_integer(temp)} degrees Rankine is {check_integer(rankine_to_celsius(temp))} Degrees Celsius.")
                print(f"{check_integer(temp)} degrees Rankine is {check_integer(rankine_to_fahrenheit(temp))} Degrees Fahrenheit.")
                print(f"{check_integer(temp)} degrees Rankine is {check_integer(rankine_to_kelvin(temp))} Kelvin.")
                print(f"{check_integer(temp)} degrees Rankine is {check_integer(rankine_to_reaumur(temp))} Degrees Reaumur.")
    elif found and primary_scale == 5:
                temp = float(input("Enter the Temperature (in Reaumur): "))
                print(f"{check_integer(temp)} degrees Reaumur is {check_integer(reaumur_to_celsius(temp))} Degrees Celsius.")
                print(f"{check_integer(temp)} degrees Reaumur is {check_integer(reaumur_to_fahrenheit(temp))} Degrees Fahrenheit.")
                print(f"{check_integer(temp)} degrees Reaumur is {check_integer(reaumur_to_kelvin(temp))} Kelvin.")
                print(f"{check_integer(temp)} degrees Reaumur is {check_integer(reaumur_to_rankine(temp))} Degrees Rankine.")
    else:
        print("Invalid scale (Please select Celsius, Fahrenheit, Kelvin, Rankine, or Reaumur, or enter 1-5.).")
