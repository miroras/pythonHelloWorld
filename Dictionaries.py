employee = {
    "name":"Jesse James",
    "Age": 34,
    "Tech Level": 12,
    "EmpID": 23487}

print(employee["name"])

employee["name"] = "Yokatoro San"
employee["Tech Level"] = 34
del employee["Age"]

print(employee.values())
print(employee.keys())
