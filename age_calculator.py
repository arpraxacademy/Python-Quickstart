# Age Calculator Program
'''
This app asks for your name and age,
then calculates the year you turn 100
'''

# 1. Ask for the user's name
name = input("What is your name? ")

# 2. Ask for age
age = int(input("What is your age? "))

# 3. The Logic
years_left = 100 - age
current_year = 2025
turn_100_year = current_year + years_left

# 4. The Output
print(f"Hello, {name}, you will turn 100 years old in the year {turn_100_year}.")

