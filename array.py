import numpy as np
#playing whit np arrays
def line():
    print("----------------------------")

print("building table")

table = np.array([[2,3,4],
                  [5,5,5],
                  [1,2,9]])

line()

print(table)

line()

print("Power")

line()

table2 = np.power(table,3)
print(table2)

line()

table[[2]] = 4
print("Chage row 3 (value = 4)")

line()

print(table)

line()
print("Cutting table")
line()

print(table[:,1])



for i in range(0,len(table)):
    table[i,1:2] = 9

line()
print("Using for whit array")
line()

print(table)

line()
print("Fancy index")
line()

print(table[[1,2,1,1,1]])

line()
print("Transposed")
line()

print(table[[1,2,1,1,1]].T)

line()
print("Substract")
line()

print(np.subtract(table,table2))

line()
print("Square root")
line()

print(np.sqrt(table))

line()
print("Trigonometric sine")
line()

print(np.sin(table))