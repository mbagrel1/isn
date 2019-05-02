#fonctions
def imc(poids, taille):
    indice=poids/(taille*taille)
    return indice


def interpretation(i_m_c):
    if i_m_c<16.5:
        return"famine"
    elif 16.5<i_m_c<18.5:
        return"maigreur"
    elif 18.5<i_m_c<25:
        print"corpulence normale"
    elif 25<i_m_c<30 :
        return "surpoids"
    else:
        return"obesite moderee"

#programme principal

poids=input("saisissez votre poids en kg :")
taille=input("saisissez votre taille en m :")
IMC=imc(poids, taille)
print "l'interpretation est", interpretation(IMC)
