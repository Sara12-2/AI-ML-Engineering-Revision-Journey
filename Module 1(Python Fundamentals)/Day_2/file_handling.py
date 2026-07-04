# Write

with open("data.txt", "w") as file:
    file.write("Hello Python")

# Read

with open("data.txt", "r") as file:
    print(file.read())

# Append

with open("data.txt", "a") as file:
    file.write("\nAI Engineering")