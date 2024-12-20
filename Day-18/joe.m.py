"""
AUTHOR : JOE MARTIN RINCE
"""
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
    for element in row:
        print(element, end=" ")
    print()

print()
print()

n = 7

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
print()
print()

n = 5

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2}", end=" ")
    print()
