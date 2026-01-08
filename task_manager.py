# --- Configuration ---
# We use a tuple for settings we don't want to change accidentally
app_settings = ("Simple task manager", "V 1.0")
print(f" --- {app_settings[0], app_settings[1]} ---")

# --- Load Data (File I/O) ---
# using 'with' automatically closes the file, even if errors happen
print("Loading Tasks ...")
try:
    with open("todo.txt", "r") as file:
        raw_data = file.readlines()
    # List Comprehension (Clean up \n)
    tasks = [line.strip() for line in raw_data]
except FileNotFoundError:
    tasks = [] # If file doesn't exist, start empty

# --- User Interaction ---
# Show current list
print(f"Current tasks loaded: {len(tasks)}")

# Lists (Add new data)
new_task = input ("Enter a new tasks to add: ")
tasks.append(new_task)

# --- Remove Duplicates ---
# Sets (Remove Duplicates)
unique_tasks = set(tasks)

# Convert back to list so we can sort or order them later
tasks = list(unique_tasks)

# --- Save Data (File I/O) ---
# 'with' ensures the file is saved and closed properly
with open("todo.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")

# --- View Tasks (For Loop) ---
print("\n--- Your To-Do list ---")
for t in tasks:
    print(f"- {t}")






