"""
Project 4: Car Dashboard (The Logic Module)
Part of the 'Python Fast Track' Bootcamp by Arprax Academy.

📺 Watch the Tutorial for this Script: https://youtu.be/wKyePEkzw2E
▶️ Full Course Playlist: https://youtube.com/playlist?list=PL7kitcmP3RiO724GV3Fmb1MHEp0g9RYnJ&si=ozyOr1brpt0lUbEH

Description:
This file acts as a 'Library' or 'Module'. It holds tools (functions)
that other scripts (like mechanic.py) can import and use.
Teaches:
- Defining Functions (def)
- Return Values
- Dictionaries (Key-Value pairs)
- The 'Ignition Key' (if __name__ == "__main__")
"""

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
    fuel_needed = miles / 25
    return fuel_needed


# 4. MAIN PROGRAM (The Driving Logic)
def drive_car():
    start_engine()
    print("GPS Destinations Found:")
    # Loop through the dictionary keys
    for place in gps_favorites:
        print(f"📍{place}: {gps_favorites[place]}")

    destination = input("\nWhere do you want to go? ")

    # Check if the key exists in the dictionary
    if destination in gps_favorites:
        distance = gps_favorites[destination]
        # Use the trip computer function to do the math
        gallons = calculate_fuel(distance)
        print(f"Driving to {destination}")
        print(f"✅ Arrived! Trip used {gallons} gallons of gas")
        print("----------------")
    else:
        print(" ❌ Error: Destination not found")


# 5. THE IGNITION KEY
# This block ONLY runs if you run THIS file directly.
# If you import this file into 'mechanic.py', this block is skipped.
if __name__ == "__main__":
    drive_car()