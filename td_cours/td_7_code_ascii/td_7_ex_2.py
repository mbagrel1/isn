def convertMaj(phrase):
    phrase_maj = ""
    for i in range(len(phrase)):
        carac = ord(phrase[i])
        if 97 <= carac <= 123:
            carac = carac - 32
            phrase_maj = phrase_maj + (chr(carac))
        else:
            phrase_maj = phrase_maj + phrase[i]
    return phrase_maj


phrase_saisie = raw_input("saisissez une phrase : ")
print convertMaj(phrase_saisie)

