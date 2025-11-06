#!/bin/bash

# List of combinations
combinations=(
    '--op1=(x+y)+z --op2=x+(y+z) --repetitions=1000 --a=0 --b=10'
    '--op1=x+y --op2=y+x --repetitions=500 --a=0 --b=10'
    "--op1=(x-y)-z --op2=x-(y-z) --repetitions=1000 --a=1 --b=5"
    "--op1=x*(y/z) --op2=(x*y)/z --repetitions=700 --a=10 --b=100"
)

# Loop through each combination and run the CLI program
for combination in "${combinations[@]}"
do
    echo "Running: python CLI_implementation/run_CLI.py $combination"
    python CLI_implementation/run_CLI.py $combination
done