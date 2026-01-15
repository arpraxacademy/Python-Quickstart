"""
Project 6: Data Pipeline
Part of the 'Python Fast Track' Bootcamp by Arprax Academy.

📺 Watch the Tutorial for this Script: https://youtu.be/7RbLMQ8T2fk
▶️ Full Course Playlist: https://youtube.com/playlist?list=PL7kitcmP3RiO724GV3Fmb1MHEp0g9RYnJ&si=ozyOr1brpt0lUbEH

Description:
Fetches real user data from the internet, cleans it, and saves a report.
Teaches:
- External Libraries (requests, pandas)
- APIs (Fetching JSON data)
- JSON Normalization (Flattening nested data)
- Exporting to CSV
"""

import requests
import pandas as pd

# 1. Setup the target URL (A fake API for testing)
url = "https://jsonplaceholder.typicode.com/users"

# 2. Fetch the data (Extract)
print("Fetching data from the internet ...")
response = requests.get(url)
data = response.json() # Convert raw text to Python Dictionary/List

# Test if it works
print(f"First User Fetched: {data[0]['name']}")

# 3. Process the Data (Transform)
# Create a DataFrame (Think of this as an Excel Sheet in RAM)
# 'df_nested' will have raw dictionaries inside columns (messy)
df_nested = pd.DataFrame(data)

# 'df' uses json_normalize to flatten nested data (e.g., address.city)
df = pd.json_normalize(data)

# 4. Save to a file (Load)
print("Saving report ...")
df_nested.to_csv("user_report_nested.csv", index=False)
df.to_csv("user_report.csv", index=False)

print("File Saved: user_report.csv")