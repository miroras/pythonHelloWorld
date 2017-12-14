students = ["joe", "Moe", "Boe", "Jane", "Carter", "Jerry", "Avi", "Trent"]

#break example

for name in students:
    if name == "Jerry":
        print("Found {0}".format(name))
        break
    print("Currently Scanning {0}".format(name))

#continue example

for name in students:
    if name == "Boe":
        continue
        print("Found {0}".format(name))
        break
    print("Currently Scanning {0}".format(name))
