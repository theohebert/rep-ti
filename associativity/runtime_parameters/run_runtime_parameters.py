import random
import pandas as pd

def test_associativity(a,b, nombre_essais,op1,op2,seed=0):
    random.seed(seed)
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
    #utilse seulement pour comparer les differentes combinaisons de parametres
    factors_comb = [
    {"op1": "(x + y) + z", "op2": "x + (y + z)"}
    #{"op1": "(x + y) + z", "op2": "x + (y + z)"},
    #{"op1": "(x + y) + z", "op2": "x + (y + z)"},
    #{"op1": "(x + y) + z", "op2": "x + (y + z)"},
    ]
    seed = [0,1,2,4,8,16]
    repetions_list = [10,20,100,500,2000,5000,10000]
    a_list = [-1,0,1,10,20,50,100]
    b_list = [1,5,10,20,50,100,10000]
    res_df = pd.DataFrame(columns=["op1", "op2", "repetition", "seed", "a", "b", "NombreReussites", "NombreEssais", "PourcentageReussites"])
    res_df.to_csv("results_associativity.csv", index=False)
    print("Starting tests...")
    for factor in factors_comb:
        for seed in seed:
            for repetition in repetions_list:
                for a in a_list:
                    for b in b_list:
                        if a >= b:
                            continue
                        print(f"Running test with parameters: op1={factor['op1']}, op2={factor['op2']}, repetition={repetition}, seed={seed}, a={a}, b={b}")
                        NombreReussites = test_associativity(a, b, repetition, factor['op1'], factor['op2'],seed)
                        res_df = pd.concat([res_df, pd.DataFrame({'op1': [factor['op1']], 'op2': [factor['op2']], 'repetition': [repetition], 'seed': [seed], 'a': [a], 'b': [b], 'NombreReussites': [NombreReussites], 'NombreEssais': [repetition], 'PourcentageReussites': [(NombreReussites/repetition)*100]})], ignore_index=True)

    res_df.to_csv("results_associativity.csv", index=False)
