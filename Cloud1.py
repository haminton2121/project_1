from random import choices
hours = list(range(1,25))
status = ["Alert", "No Alert"]
for i in hours:
    print(f"Hour: {i} -- {choices(status)}")