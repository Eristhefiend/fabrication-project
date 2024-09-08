# Variables for fabrication calculation
def get_float_input(prompt: str, default: float = None) -> float:
    while True:
        try:
            user_input = input(prompt)
            if user_input == "" and default is not None:
                return default
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")

while True:
    # Material properties dictionary
    material_properties = {
        "steel": {"density": 7850, "tensile_strength": 400, "yield_strength": 250},  # density in kg/m^3, strengths in MPa
        "aluminum": {"density": 2700, "tensile_strength": 300, "yield_strength": 150},
        "titanium": {"density": 4500, "tensile_strength": 900, "yield_strength": 800},
        "copper": {"density": 8900, "tensile_strength": 220, "yield_strength": 200}
    }

    # Get material type from user
    material_type = input("Enter the material type (steel, aluminum, titanium, copper): ").lower()
    if material_type not in material_properties:
        print("Invalid material type. Defaulting to steel.")
        material_type = "steel"

    # Get material properties
    density_of_material = material_properties[material_type]["density"]
    tensile_strength = material_properties[material_type]["tensile_strength"]
    yield_strength = material_properties[material_type]["yield_strength"]

    # Get other inputs from user
    length = get_float_input("Enter the length of the sheet (in meters): ")
    width = get_float_input("Enter the width of the sheet (in meters): ")
    thickness = get_float_input("Enter the thickness of the sheet (in meters): ")
    material_cost_per_kg = get_float_input("Enter the material cost per kg: ")
    waste_factor = get_float_input("Enter the waste factor (as a percentage): ")
    leveling_cost_per_sqm = get_float_input("Enter the cost to level per square meter: ")
    deburring_cost_per_sqm = get_float_input("Enter the cost to debur per square meter: ")
    labor_cost_per_hour = get_float_input("Enter the labor cost per hour: ")
    applied_load = get_float_input("Enter the applied load on the sheet (in Newtons): ")

    # Calculating volume of the sheet
    volume = length * width * thickness  # in cubic meters

    # Calculating mass of the sheet
    mass = volume * density_of_material  # in kg

    # Adjusting for waste
    total_mass = mass * (1 + waste_factor / 100)

    # Calculating total material cost
    material_cost = total_mass * material_cost_per_kg

    # Calculating area of the sheet (for leveling and deburring costs)
    area = length * width  # in square meters

    # Calculating leveling and deburring costs
    leveling_cost = area * leveling_cost_per_sqm
    deburring_cost = area * deburring_cost_per_sqm

    # Calculating total cost
    total_cost = material_cost + leveling_cost + deburring_cost

    # Calculating stress on the material
    stress = applied_load / area  # in Pascals (Pa), which is equivalent to N/m^2
    stress_mpa = stress / 1e6  # converting to MPa

    # Check for yield strength failure
    if stress_mpa > yield_strength:
        yield_failure = "Yes"
    else:
        yield_failure = "No"

    # Print the results
    print(f"The total fabrication cost, including leveling and deburring, is: ${total_cost:.2f}")
    print(f"Material: {material_type.capitalize()}")
    print(f"Tensile Strength: {tensile_strength} MPa")
    print(f"Yield Strength: {yield_strength} MPa")
    print(f"Applied Load: {applied_load} N")
    print(f"Calculated Stress: {stress_mpa:.2f} MPa")
    print(f"Yield Strength Failure: {yield_failure}")

    # Ask the user if they want to calculate again
    calculate_again = input("Do you want to calculate again? (yes/no): ").lower()
    if calculate_again != "yes":
        break