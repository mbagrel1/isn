notes=[12,8,13,12,6,10,17,10]
bon=[]
def bonus(liste):
    for x in liste:
        bon.append(x+1)
    return bon

print bonus(notes)
