chaine=raw_input("entrer une chaine de caractere :")
dernier=len(chaine)-1
text_inv=""
for i in range(len(chaine)):
    text_inv= text_inv+ chaine[dernier-i]

if text_inv==chaine:
    print"le mot est un palindrome"
else:
    print"le mot n'est pas un palindrome"
