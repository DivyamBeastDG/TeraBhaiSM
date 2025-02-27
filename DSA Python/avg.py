
operations = {
   'average': lambda seq: sum(seq)/len(seq),
   'total': sum,
   'top': max
}

students = [
    {"name": "Divyam", "grades": (90, 89, 98, 100)},
    {"name": "chammo", "grades": (3, 78, 67, 10)},
    {"name": "Amandeep", "grades": (92, 69, 91, 100)}
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total' or 'top': ")

    operation_function = operations[operation]
    print(operation_function(grades))