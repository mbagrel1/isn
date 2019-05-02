a=input("Donner le premier nombre:")
b=input("Donner le second nombre:")
c=input("Donner le troisieme nombre")
if a>b:
    if b>c:
        print"La note moyenne est",b
    elif a>c:
        print"La note moyenne est" ,c
    else:
        print"La note moyenne est",a
else:
    print"Le premier nombre est le plus grand"
