animal=input("Enter an animal: ")

facts = {
    "cheetah": "Cheetahs run very very fast",
    "vulture": "Vultures fly very very high.",
    "dog": "Dogs have a great sense of smell."
}
fact = facts.get(animal)

if fact != None:
    print(facts[animal])
else:
    print(f"Animal {animal} is not recognize")

students = {
    373335: {"Name": "Diya",
             "Age": 12,
             "School": "Kennedy Middle School"},
    383226: {"Name": "Aditi",
             "Age": 10,
             "School": "Faria Elementary School"}
}

print(students[373335]["Age"])

ms = ["Aditi", "Surya", "Ethan", "Alex", "Alex", "Doris", "Mark"]

for m in ms:
    print(m)

# Problem: store name and gender for FLL team members
# Print in the format: "Aditi is a girl"

members = [
    {"Name": "Aditi", 
     "Gender":"Girl"},
    {"Name": "Surya",
     "Gender":"Boy"},
    {"Name": "Ethan",
     "Gender":"Boy"},
    {"Name": "Doris",
     "Gender":"Boy"},
    {"Name": "Alex",
     "Gender":"Girl"},
    {"Name": "Alex",
     "Gender":"Boy"},
    {"Name": "Mark",
     "Gender":"Girl"}
]

for member in members:
    print(member["Name"], "is a", member["Gender"])