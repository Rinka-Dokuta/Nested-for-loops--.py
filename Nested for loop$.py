for i in range(6):
    for j in range(10):
        print("$", end = " ")
    print()
    
rows = 3
columns = 5
for i in range(rows, rows + columns):
    for j in range(columns):
        print(i, end = " ")
    print()
