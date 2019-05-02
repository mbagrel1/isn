TABLE=7

for i in range(0,21,1):
    resultat=TABLE*i
    if resultat % 3 != 0:
        print i,"x", TABLE, "=", resultat
    else:
        print i,"x", TABLE, "=", resultat, "*"

