"""
Project 4 (Bonus): The Mechanic
Part of the 'Python Fast Track' Bootcamp by Arprax Academy.

📺 Watch the Tutorial for this Script: https://youtu.be/wKyePEkzw2E
▶️ Full Course Playlist: https://youtube.com/playlist?list=PL7kitcmP3RiO724GV3Fmb1MHEp0g9RYnJ&si=ozyOr1brpt0lUbEH

Description:
Demonstrates how to import code from another file without running the main loop.
"""
import car_dashboard

print("👨‍🔧 Mechanic is here ...")

# We can use the 'Trip Computer' tool WITHOUT starting the engine
# because the Ignition Key in car_dashboard stopped the drive_car() loop.
miles_to_test = 100
result = car_dashboard.calculate_fuel(miles_to_test)

print(f"Diagnostic Report: {miles_to_test} miles requires {result:.2f} gallons of gas.")