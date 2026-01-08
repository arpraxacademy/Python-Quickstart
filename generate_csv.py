import requests
import pandas as pd
# Setup the target
url = "https://jsonplaceholder.typicode.com/users"

# Fetch the data
print("Fetching data from the internet ...")
response = requests.get(url)
data = response.json()

# Test if it works
print(data[0]['name'])

# Create a DataFrame (The Excel Sheet in RAM)
df_nested = pd.DataFrame(data)
df = pd.json_normalize(data)

# Save to a file
print("Saving report ...")
df_nested.to_csv("user_report_nested.csv", index=False)
df.to_csv("user_report.csv", index=False)

print("File Saved.")

