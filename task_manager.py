"""
Project 3: Professional Task Manager
Part of the 'Python Fast Track' Bootcamp by Arprax Academy.

📺 Watch the Tutorial for this Script: https://youtu.be/xCYtdI1woSY
▶️ Full Course Playlist: https://youtube.com/playlist?list=PL7kitcmP3RiO724GV3Fmb1MHEp0g9RYnJ&si=ozyOr1brpt0lUbEH

Description:
A To-Do List that saves data to a file so you don't lose it.
Teaches:
- File I/O (Reading/Writing txt files)
- Context Managers ('with open')
- Lists vs Sets (Handling duplicates)
- Error Handling (try/except)
"""

# --- Configuration ---
# We use a tuple for settings we don't want to change accidentally
app_settings = ("Simple task manager", "V 1.0")
print(f" --- {app_settings[0], app_settings[1]} ---")

# --- Load Data (File I/O) ---
# using 'with' automatically closes the file, even if errors happen.
print("Loading Tasks ...")
try:
    with open("todo.txt", "r") as file:
        raw_data = file.readlines()
    # List Comprehension: A shortcut to clean up the '\n' from every line
    tasks = [line.strip() for line in raw_data]
except FileNotFoundError:
    # If the file doesn't exist yet (first run), start with an empty list
    tasks = [] 

# --- User Interaction ---
# Show current list
print(f"Current tasks loaded: {len(tasks)}")

# Lists (Add new data)
new_task = input ("Enter a new tasks to add: ")
tasks.append(new_task)

# --- Remove Duplicates ---
# Sets cannot have duplicates. Converting List -> Set -> List cleans the data.
unique_tasks = set(tasks)
tasks = list(unique_tasks)

# --- Save Data (File I/O) ---
# 'w' mode overwrites the file with the new, clean list
with open("todo.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")

# --- View Tasks (For Loop) ---
print("\n--- Your To-Do list ---")
for t in tasks:
    print(f"- {t}")