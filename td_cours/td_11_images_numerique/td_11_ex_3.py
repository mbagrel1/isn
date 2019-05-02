fichier = open("drone-in-flight.ppm", "r")
fichier1 = open("rouge.ppm", "w")
fichier2 = open("vert.ppm", "w")
fichier3 = open("bleu.ppm", "w")

lignes = [l for l in fichier.readlines() if l.strip() != ""]
entete = lignes[:4]
lignes_pixels = lignes[4:]

pixels = [
    int(ligne[:-1])
    for ligne in lignes_pixels
]

r = []
v = []
b = []

for i in range(len(pixels)):
    if i % 3 == 0:
        r.append(pixels[i])
        v.append(0)
        b.append(0)
    elif i % 3 == 1:
        r.append(0)
        v.append(pixels[i])
        b.append(0)
    else:
        r.append(0)
        v.append(0)
        b.append(pixels[i])

def refaire_fichier(pixels):
    return "".join(entete) + "\n".join([str(pixel) for pixel in pixels]) + "\n"

fichier1.write(refaire_fichier(r))
fichier2.write(refaire_fichier(v))
fichier3.write(refaire_fichier(b))

fichier.close()
fichier1.close()
fichier2.close()
fichier3.close()

