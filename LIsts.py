students = ["joe", "Moe", "Boe"]

print(students[2])

students.append("Mark")

print(students[3])

print("Mark" in students) #should be True

print(len(students))

del students[1]

print(len(students))

print(students)

print(students[1:-1])
