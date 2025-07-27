# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_CONVERSION_FACTOR = 9 / 5
CELSIUS_CONVERSION_FACTOR = 5 / 9
FAHRENHEIT_OFFSET = 32

# Define conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_OFFSET) * CELSIUS_CONVERSION_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * FAHRENHEIT_CONVERSION_FACTOR) + FAHRENHEIT_OFFSET

def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted:.2f}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted:.2f}°F")
        else:
            print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()