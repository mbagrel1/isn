def modulo(nombre, diviseur):
    return nombre % diviseur == 0

nb = input("quel nombre voulez vous tester : ")
divise = input("par quel nombre voulez vous le diviser : ")
print modulo(nb, divise)
