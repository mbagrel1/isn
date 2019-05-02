def creation_bin(n):
    i = 7
    A = []
    while i >= 0:
        if n - 2 ** i >= 0:
            A.append(1)
            n = n - 2 ** i
        else:
            A.append(0)
        i = i - 1
    return A


nombre = input("rentrer un nombre entier entre 0 et 255 :")
if 0 <= nombre <= 255:
    n = nombre

print creation_bin(n)