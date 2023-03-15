db = {}
for _ in range(int(input())):
    string = input()
    if string in db.keys():
        print(string + str(db[string]))
        db[string] += 1
    else:
        db[string] = 1
        print("OK")