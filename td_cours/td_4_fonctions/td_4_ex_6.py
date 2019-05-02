chaine=raw_input("entrer une chaine de caractere :")
i=0
dernier=len(chaine)-1
PAL=False
for i in range chaine:
    if chaine[i]==chaine[dernier-i]:
    i=i+1

    PAL=True


if PAL==True:
    print"le mot est un palindrome"
else:
    print"le mot n'est pas un palindrome"
