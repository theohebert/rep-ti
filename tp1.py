import random

def test_associativity(a,b, nombre_essais):
    NombreReussites = 0
    for i in range(nombre_essais):
        x = random.uniform(a, b)
        y = random.uniform(a, b)
        z = random.uniform(a, b)

        res1 = (x+y)+z
        res2 = x+(y+z)  

        if res1 == res2:
            NombreReussites += 1
        #else:
            #residu = res1 - res2
            #residus = pd.concat([residus, pd.DataFrame({'residu': [residu]})], ignore_index=True)
    return NombreReussites


def ecriture_resultats(nom_fichier, a, b, NombreEssais, NombreReussites):
    with open(nom_fichier, "w") as fichier:
        fichier.write(f"Intervalle de tirage uniforme: [{a}, {b}]\n")
        print(f"Intervalle de tirage uniforme: [{a}, {b}]")
        fichier.write(f"Nombre d'essais: {NombreEssais}\n")
        print(f"Nombre d'essais: {NombreEssais}")
        fichier.write(f"Nombre de réussites: {NombreReussites} sur {NombreEssais}\n")
        print(f"Nombre de réussites: {NombreReussites} sur {NombreEssais}")
        pourcentage = (NombreReussites / NombreEssais) * 100
        fichier.write(f"Pourcentage de réussites: {pourcentage:.2f}%\n")
        print(f"Pourcentage de réussites: {pourcentage:.2f}%")
        fichier.close()



if __name__ == "__main__":
    random.seed(12)
    NombreEssais = 100000
    a = 0
    b = 1
    
    NombreReussites = test_associativity(a, b, NombreEssais)
    ecriture_resultats("answer_associativity.txt", a, b, NombreEssais, NombreReussites)