import json

# Load existing data
with open("user_data.json", "r") as file:
    data = json.load(file)

# Update skills
data["skills"].append("PowerShell")

# Save updated data
with open("user_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Skills updated successfully!")