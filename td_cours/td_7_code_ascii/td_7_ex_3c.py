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
    phrase_decryptee = ""
    for i in range(len(phrase)):
        carac = chiffreRot13(phrase[i])
        phrase_decryptee = phrase_decryptee + carac
    return phrase_decryptee


carac = raw_input("saisissez une phrase a decrypter : ")
print convertphrase13(carac)