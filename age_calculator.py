"""
Project 1: Age Calculator
Part of the 'Python Fast Track' Bootcamp by Arprax Academy.

📺 Watch the Tutorial for this Script: https://youtu.be/770xemnXhDU
▶️ Full Course Playlist: https://youtube.com/playlist?list=PL7kitcmP3RiO724GV3Fmb1MHEp0g9RYnJ&si=itvpA_3vroiblfjV

Description:
A simple script to calculate when you will turn 100 years old.
This introduces the 3 pillars of basic Python:
1. Variables (Buckets for data)
2. Casting (Turning Text into Numbers)
3. F-Strings (Injecting data into text)
"""

# 1. Ask for the user's name
# The input() function always returns a string (text).
name = input("What is your name? ")

# 2. Ask for age
# We wrap input() inside int() to convert the text "25" into the number 25.
# If we don't do this, we cannot do math on it later.
age = int(input("What is your age? "))

# 3. The Logic
# Calculate the years remaining and the target year.
years_left = 100 - age
current_year = 2025
turn_100_year = current_year + years_left

# 4. The Output
# We use an f-string (note the 'f' before the quotes).
# This lets us inject variables directly using {curly_brackets}.
print(f"Hello, {name}, you will turn 100 years old in the year {turn_100_year}.")