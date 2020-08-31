"""
# with in a row, values are changing. we requied a nested loop.
# How many row ? lenght of string.

"""
string = input("Please Enter String")
lenght=len(string)
for row in range(lenght):
    for col in range(row+1):
        print(string[col], end=' ')
    print()