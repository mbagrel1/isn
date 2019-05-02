chaine=raw_input("entrer une chaine de caractere a inverser:")
dernier=len(chaine)-1
text_inv=""
for i in range(len(chaine)):
    text_inv= text_inv+ chaine[dernier-i]
print text_inv
