notes=[12,8,13,12,6,10,17,10]

def moyenne(notes):
    somme=0
    for x in notes:
        somme=somme+x
        moy=somme/(len(notes)-1)
    return moy

print moyenne(notes)

