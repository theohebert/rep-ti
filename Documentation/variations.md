## Variations de notre code

Lors de nos différents essais de variations des paramètres de notre experience (x+y)+z==x+(y+z) nous avous pu remarquer que les **parametres a et b** (servant à créer l'intervalle [a,b] utilisé pour piocher les nombres aléatoires) avaient un impact non négligeable sur les résultats de l'experience. 

Un autre facteur de variabilité du résultat est le **nombre de repetitions de l'experience** (Nombre d'essais). 

De la même manière, la **seed de l'aléatoire a un leger impact sur les resultas** (impact moins important mais expliquant de potentiels écarts).

A noter que les scripts ont été lancé dans un même environnement de python (3.12.3) et sur une machine locale (ubuntu 24.04.1). Docker étant hors service, nous n'avons pas pu faire varier la version de l'os et de python qui auraient pu impacter les résultats.




## rep-INSA (sallooh,Aziz-xas)
Avec leur experience de base:
réglages: 
- pas de seed
- a = -1e16
- b = 1e16
- NombreEssais = 10000
Résutat obtenu: entre 91,9 et 92,5% d'égalité.

**L'ajout de seed impacte** bien leurs résultats. (92.5% de base sans seed et 92.36% avec une seed à 12).
On choisit de **fixer la seed à 0** pour la suite de nos test afin de pouvoir isoler les autres facteurs de variabilité.  Avec la seed à 0, on obtient **92,28%**. On utilisera cette valeur comme référence.


Les **champs a et b ont aussi un impact significatif** sur leur résultats. En passant les valeurs de a et b à a=0 et b=1, on obtient un resultat de **82,89%**. Avec une variation de presque 10%, ce facteur présente un impact non négligeable.

**Le nombre de répétitions impacte aussi leurs résultats.** En passant le nombre de répétitions à 100000 (en gardant les autres réglages par defaut), on obtient un résultat de **92.4%**.


Lorsque l'on met les même réglages que dans notre experience:
réglages: 
- seed = 0
- a = 0
- b = 1
- NombreEssais = 100000

On obtient un résultat de **82,77%**. On retrouve alors le même résultat que lors de notre experience ! 