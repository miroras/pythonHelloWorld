employee = {
    "name":"Jesse James",
    "Age": 34,
    "EmpID": 23487}

try:
    some_number = 3 + employee["name"]
    print(employee["Tech Level"])
except KeyError:
    print("This is a KeyError i cought.")
except TypeError:
    print("This is a TypeError i cought")
except Exception as error:
    print("General Exception")
    print(error)

print("i reached the end")
