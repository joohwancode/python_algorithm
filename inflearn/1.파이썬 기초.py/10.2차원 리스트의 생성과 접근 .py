# a = [0] * 3
# print(a)

a = [[0] * 3 for _ in range(3)]
print(a)
a[0][1] = 2
a[1][2] = 1
print(a)

for x in a:
    print(x)

for x in a:
    for y in x:
        print(y, end=" ")
    print()
