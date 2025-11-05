# <span style="color:red"> /!\ Pas a jour </span>

# How to run simply

You should execute the script *tp1.py* and you then will have the file *answer_associativity.txt* in wich you should have the result.

# Associativity

## How to run in docker 

First, be sure you have Docker well installed (https://www.docker.com/).

Go on the root directory of the project (where this file is) and Build image with :
```bash
sudo docker build -t associativity .
```

And then run with 
```bash
sudo docker run -v  $(pwd):/app associativity
```

### The result you should have

Test de l'associativité de l'addition en virgule flottante
Intervalle de tirage uniforme: [0, 1]
Nombre d'essais: 100000
On compte le nombre de fois où (x+y)+z == x+(y+z)
Nombre de réussites: 82766 sur 100000

# Banking problem

## How to run in docker 

First, be sure you have Docker well installed (https://www.docker.com/).

Build image with :
```bash
sudo docker build -t banking_problem ./banking_problem
```

And then run with :
```bash
sudo docker run -v  .:/app banking_problem
```