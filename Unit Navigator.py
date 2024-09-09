# Supported units and their conversion rates to meters (for length)
conversion_factors = {
    'kilometers': 1000,
    'meters': 1,
    'centimeters': 0.01,
    'millimeters': 0.001,
    'miles': 1609.34,
    'yards': 0.9144,
    'feet': 0.3048,
    'inches': 0.0254
}

def show_supported_units():
    print("Supported units for conversion:")
    for unit in conversion_factors.keys():
        print(f"- {unit}")

def convert_units(amount, from_unit, to_unit):
    # Convert the amount from the original unit to meters
    if from_unit in conversion_factors and to_unit in conversion_factors:
        meters = amount * conversion_factors[from_unit]
        converted_amount = meters / conversion_factors[to_unit]
        return converted_amount
    else:
        return None

def unit_converter():
    while True:
        show_supported_units()
        from_unit = input("Enter the unit you have (e.g., kilometers, meters): ").lower()
        to_unit = input("Enter the unit you want to convert to: ").lower()

        if from_unit not in conversion_factors or to_unit not in conversion_factors:
            print("Sorry, unsupported unit. Exiting the program.")
            break
        
        try:
            amount = float(input(f"Enter the amount in {from_unit}: "))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
            continue

        result = convert_units(amount, from_unit, to_unit)
        if result is None:
            print("Invalid conversion. Exiting the program.")
            break
        else:
            print(f"{amount} {from_unit} is equal to {result:.4f} {to_unit}")

        continue_conversion = input("Do you want to convert to another unit? (yes/no): ").lower()
        if continue_conversion != 'yes':
            print("Thank you for using Unit Navigator. Goodbye!")
            break

# Start the program
unit_converter()
