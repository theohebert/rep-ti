import random
import argparse

def test_associativity(a,b, nombre_essais,op1,op2):
    random.seed(0)
    NombreReussites = 0
    for i in range(nombre_essais):
        x = random.uniform(a, b)
        y = random.uniform(a, b)
        z = random.uniform(a, b)

        res1 = eval(op1) #(x+y)+z
        res2 = eval(op2) #x+(y+z)  

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
    random.seed(0)
    
    parser = argparse.ArgumentParser(description="Test associativity of operations")
    parser.add_argument("--op1", type=str, default="(x + y) + z", help="First operation")
    parser.add_argument("--op2", type=str, default="x + (y + z)", help="Second operation")
    parser.add_argument("--repetitions", type=int, default=100000, help="Number of repetitions")
    parser.add_argument("--a", type=float, default=0, help="Lower bound of uniform distribution")
    parser.add_argument("--b", type=float, default=1, help="Upper bound of uniform distribution")
    args = parser.parse_args()
    
    
    NombreReussites = test_associativity(args.a, args.b, args.repetitions, args.op1, args.op2)
    ecriture_resultats("answer_associativity.txt", args.a, args.b,args.repetitions, NombreReussites)