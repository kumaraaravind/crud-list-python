# pyramid pattern:

n = int(input("enter the number to loop "))# for ex: 5,6,7,
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end=" ")
    print()

#numeric pattern:

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# star pattern
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print()

#inverted half pattern

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


