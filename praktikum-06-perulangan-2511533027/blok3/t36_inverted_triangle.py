height = int(input("Enter height: "))
for row in range(height, 0, -1):
    for col in range(row):
        if col < row - 1:
            print("*", end=" ")
        else:
            print("*", end="")
    print()