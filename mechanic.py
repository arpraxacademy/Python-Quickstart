import car_dashboard
print("👨‍🔧 Mechanic is here ...")
# car_dashboard.start_engine()

# We can use the 'Trip Computer' tool WITHOUT starting the engine
# because the Ignition Key (if __name__ == "__main__") stopped the drive_car() loop.

miles_to_test = 100
result = car_dashboard.calculate_fuel(miles_to_test)
print(f"Diagnostic Report: {miles_to_test} requires {result:.2f} gallon of gas.")
