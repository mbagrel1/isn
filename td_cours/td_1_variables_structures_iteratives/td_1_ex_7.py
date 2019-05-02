a=input("Donner le premier nombre:")
b=input("Donner le second nombre:")
c=input("Donner le troisieme nombre:")

moyenne=(a+b+c)/3.0
print " La moyenne est",moyenne
print"La note minimale est",min(a,b,c)
print"La note maximale est", max(a,b,c)

if moyenne<=10.0:
    print"INSUFFISANT"
elif moyenne<=12.0:
    print"ASSEZ BIEN"
else:
    print"TRES BIEN"
