from random import shuffle

p = True
while p:
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
   
    dimensions = rows * columns

    if dimensions % 2 != 0:
        print("***The value rows X columns must be even. Try again.***")
    else:
        p = False

pairs = dimensions // 2

pair_numbers = list(range(1, pairs + 1)) * 2
shuffle(pair_numbers)

stars=[]
for i in range(1, dimensions+1):
    stars.append("*")

pair_numbers_iter = iter(pair_numbers)
starts_iter = iter(stars)

number_list = []
star_list = []

# Generate the number_list and star_list
for y in range(rows):
    row = [next(pair_numbers_iter) for x in range(columns)]
    number_list.append(row)

for y in range(rows):
    row = [next(starts_iter) for x in range(columns)]
    star_list.append(row)

# *** To see final answer before guess pair numbers remove """s from below (for) statement  ***
"""
for i in range(0,rows):
        for j in range(0,columns):
            print(number_list[i][j],end=' ')
        print()
"""

for i in range(rows):
    for j in range(columns):
        print("*", end = " ")
    print()

f=True

while f:

    m,n=True,True

    while m:
        x1, y1 = input("input coordinates for first card: ").split()
        x1 = int(x1)
        y1 = int(y1)
        if x1 > rows or x1 < 1 or y1 > columns or y1 < 1:
            print("***Invalid coordinates! Try again***")
        else:
            m = False

    while n:    
        x2, y2 = input("input coordinates for second card: ").split()
        x2 = int(x2)
        y2 = int(y2)
        if x2 > rows or x2 < 1 or y2 > columns or y2 < 1:
            print("***Invalid coordinates! Try again***")
        else:
            n = False

    if number_list[x1-1][y1-1] == number_list[x2-1][y2-1]:
        star_list[x1-1][y1-1] = number_list[x1-1][y1-1]
        star_list[x2-1][y2-1] = number_list[x2-1][y2-1]
    else:
        print("Not an identical pair. Found {} at ({},{}) and {} at ({},{})".format(number_list[x1-1][y1-1], x1, y1, number_list[x2-1][y2-1], x2, y2))     

    for i in range(0,rows):
        for j in range(0,columns):
            print(star_list[i][j], end = ' ')
        print()

    
    if number_list == star_list:
        print("Game Over!")
        f = False
    

