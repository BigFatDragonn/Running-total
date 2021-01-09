a = [int(i) for i in input()]
# you can also place len(a) inside b and change range(lenght + 1) to (range(1, len(a) + 1))
# and remove print(list(b[1:])) to print(b), but this was my first solutions
lenght = len(a)
b = [sum(a[0:x]) for x in range(lenght + 1)]
print(list(b[1:]))