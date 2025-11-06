# How to run simply

You should execute those two scripts :
```bash
python ./associativity/runtime_parameters/run_runtime_parameters.py
```
```bash
python ./banking_problem/banking_poblem_expe.py
```

# How to run in docker 

First, be sure you have Docker well installed (https://www.docker.com/).

Go on the root directory of the project (where this file is) and Build image with :
```bash
sudo docker build -t tp .
```

And then run with 
```bash
sudo docker run -v  .:/app tp
```

# Results

You should have somthing like the 2 CSV that are in /results

# Analysing

To analyse those result you could read those CSV and train a decision tree with the jupyter notbooks
_/associativity/runtime_parameters/analyse.ipynb_ and _banking_problem/analyse.ipynb_

