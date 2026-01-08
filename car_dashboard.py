# 1. THE DATA (Dictionary)
# Key = Destination Name, Value = Distance in miles
gps_favorites = {
    "Home": 5,
    "Work": 15,
    "Beach": 50,
    "Gym": 2
}

# 2. FUNCTION WITHOUT ARGUMENTS (The Start Button)
# Just flips a switch. No input needed.
def start_engine():
    print("----------------")
    print(" Inject the fuel ")
    print(" Spark the plug ")
    print(" 🚗 Engine Started ... Ready")
    print("------------------")

# 3. FUNCTION WITH RETURN (The Trip Computer)
# Input: Distance. Output: Fuel needed.
def calculate_fuel(miles):
    # This car gets 25 miles per gallon (MPG)
    fuel_needed = miles/25
    return fuel_needed

# 4. MAIN PROGRAM (The Driving Logic)
def drive_car():
    start_engine()
    print("GPS Destinations Found:")
    # Loop through the dictionary keys
    for place in gps_favorites:
        print(f"📍{place}: {gps_favorites[place]}")

    destination = input("\nWhere do you want to go? ")
    if destination in gps_favorites:
        distance = gps_favorites[destination]
        # Use the trip computer to do the math
        gallons = calculate_fuel(distance)
        print(f"Driving to {destination}")
        print(f"✅ Arrived! Trip used {gallons} gallons of gas")
        print("----------------")
    else:
        print(" ❌ Error: Destination not found")

# 5. THE IGNITION KEY
# Only start the engine if THIS file is the one being run.
if __name__ == "__main__":
    drive_car()