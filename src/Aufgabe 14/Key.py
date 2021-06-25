student = {'name' : 'Alex', 'old' : 13}
print(student)
print(student['name'])

# Update
student.update({'street': 'feuerbach Strasse 12'})
print(student)

student.update({'name': 'Alex2'})
print(student)

# delete an item
del student['street']
print(student)

# Lister von Dictionaries
students = [
   {
      "name" : "Alex",
      "age": 12
   },
   {
      "name" : "Andi",
      "age": 43
   }
]

print(students)