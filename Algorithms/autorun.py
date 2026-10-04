#!/usr/bin/env python3

import os
from pathlib import Path

basepath = Path(__file__).resolve().parent
file_dir = "~/GitHub/VRPAlgorithmComparison/Algorithms/"

# Counter for how many times an algorithm should run
ant_counter        = 0
genetic_counter    = 0
bee_counter        = 0
max_runs           = 10
global experiment_counter
experiment_counter = 0

# Arguements values
generations = 1000
population = 100

# For ACO
alpha   = 1
beta    = 1
rho     = 0.5
h       = 0.5
Q       = 2
ants = 10

#For GA
crossover           = 0.5
mutation            = 0.5
tournament_size     = 5
dynamic_strategy    = "ILM_DHC"

#For GA
onlookers = 50
mt        = 1.5

datasets = ["F-n45-k4.vrp", "F-n72-k4.vrp", "F-n135-k7.vrp"]

if __name__ == "__main__":

    while genetic_counter < max_runs:
        for _ in range(max_runs):
            for dataset in datasets:
                cmd = f"python {file_dir}ga.py --dataset {dataset} --population {population} --generations {generations} --crossover {crossover} --mutation {mutation} --tournament_size {tournament_size} --dynamic_strategy {dynamic_strategy} --exval {experiment_counter}"
                os.system(cmd)
                experiment_counter += 1
                print(f"Completed Experiment No: {experiment_counter}")

            genetic_counter += 1

    while bee_counter < max_runs:
        for _ in range(max_runs):
            for dataset in datasets:
                cmd = f"python {file_dir}abc.py --dataset {dataset} --generations {generations} --onlookers {onlookers} --mt {mt} --exval {experiment_counter}"
                os.system(cmd)
                experiment_counter += 1
                print(f"Completed Experiment No: {experiment_counter}")

            bee_counter += 1

    while ant_counter < max_runs:
        for _ in range(max_runs):
            for dataset in datasets:
                cmd = f"python {file_dir}aco.py --dataset {dataset} --generations {generations} --ants {ants} --alpha {alpha} --beta {beta} --rho {rho} --h {h} --Q {Q} --exval {experiment_counter}"
                os.system(cmd)
                experiment_counter += 1
                print(f"Completed Experiment No: {experiment_counter}")

            ant_counter += 1
