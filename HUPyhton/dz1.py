n1 = int(input("First number\n>>> "))
n2 = int(input("Second number\n>>> "))
n3 = int(input("Third number\n>>> "))

out = "Correct order:\n%d %d %d"

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(out % (n1, n2, n3))
    else:
        print(out % (n1, n3, n2))
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(out % (n2, n1, n3))
    else:
        print(out % (n2, n3, n1))
else:
    if n1 > n2:
        print(out % (n3, n1, n2))
    else:
        print(out % (n3, n2, n1))


