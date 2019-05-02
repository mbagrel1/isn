notes = [12, 8, 13, 12, 6, 10, 17, 10]
def mauvaise(notes):
    dernier = len(notes) - 1
    final = sorted(notes, reverse=True)
    nb = final[dernier]
    notes.remove(nb)
    return notes

print mauvaise(notes)
