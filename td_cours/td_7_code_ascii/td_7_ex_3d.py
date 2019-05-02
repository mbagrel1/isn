def chiffrer_caractere(caractere, cle):
    ascii = ord(caractere)
    limite = 90 - cle
    if 65 <= ascii <= 90:
        if ascii <= limite:
            ascii = ascii + cle
        else:
            var = ascii + cle
            ascii = var - 26
        caractere = chr(ascii)
    return caractere

def convert_phrase(phrase, cle):
    phrase_cryptee = ""
    cle = cle % 26
    for i in range(len(phrase)):
        carac = chiffrer_caractere(phrase[i], cle)
        phrase_cryptee = phrase_cryptee + carac
    return phrase_cryptee

cle_cryptage = input("saisissez la cle de cryptage : ")
carac = raw_input("saisissez une phrase a crypter : ")
print convert_phrase(carac, cle_cryptage)

