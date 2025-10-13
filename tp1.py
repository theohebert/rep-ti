import random

random.seed(0)

NombreEssais = 100000
NombreReussites = 0
a = 0
b = 1

print("Test de l'associativité de l'addition en virgule flottante")
print(f"Intervalle de tirage uniforme: [{a}, {b}]")
print(f"Nombre d'essais: {NombreEssais}")
print("On compte le nombre de fois où (x+y)+z == x+(y+z)")

fichier = open("answer_associativity.txt", "w")
fichier.write(f"Intervalle de tirage uniforme: [{a}, {b}]\n")
fichier.write(f"Nombre d'essais: {NombreEssais}\n")

for i in range(NombreEssais):
    x = random.uniform(a, b)
    y = random.uniform(a, b)
    z = random.uniform(a, b)

    res1 = (x+y)+z
    res2 = x+(y+z)  

    if res1 == res2:
        NombreReussites += 1
    else:
        residu = res1 - res2
        #residus = pd.concat([residus, pd.DataFrame({'residu': [residu]})], ignore_index=True)
    

print(f"Nombre de réussites: {NombreReussites} sur {NombreEssais}")
fichier.write(f"Nombre de réussites: {NombreReussites} sur {NombreEssais}\n")
pourcentage = (NombreReussites / NombreEssais) * 100

fichier.close()

#plot = residus.plot(kind='hist', bins=100, title='Histogramme des résidus (x+y)+z - x+(y+z)')
NombreReussites = 0
#residus = pd.DataFrame(columns=['residu'])