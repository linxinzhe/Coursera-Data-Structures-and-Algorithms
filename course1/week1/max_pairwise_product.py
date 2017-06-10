# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert (len(a) == n)

result = 0

max1 = (0, 0)
for i in range(0, n):
    if a[i] > max1[1]:
        max1 = i, a[i]

max2 = (0, 0)
for i in range(0, n):
    if i != max1[0] and a[i] > max2[1]:
        max2 = i, a[i]

print(max1[1] * max2[1])
