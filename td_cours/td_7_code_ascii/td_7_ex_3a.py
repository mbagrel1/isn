def chiffreRot13(caractere):
    ascii = ord(caractere)
    if 65 <= ascii <= 90:
        if ascii <= 77:
            ascii = ascii + 13
        else:
            ascii = ascii - 13
        caractere = chr(ascii)
    return caractere

def convertphrase13(phrase):
    phrase_cryptee = ""
    for i in range(len(phrase)):
        carac = chiffreRot13(phrase[i])
        phrase_cryptee = phrase_cryptee + carac
    return phrase_cryptee


carac = raw_input("saisissez une phrase a crypter : ")
print convertphrase13(carac)