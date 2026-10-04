#!/usr/bin/env python3

import math
import os

def distance(v1, v2): # Calculates distance between two nodes
    return math.sqrt((v1.x - v2.x)**2+(v1.y - v2.y)**2)

def getvalue(filename): # Get shortest route from .sol file
    base = os.path.splitext(os.path.basename(filename))[0]
    sol_filename = f"/home/patryksiutkowski/GitHub/VRPAlgorithmComparison/Database/{base}.sol"

    with open(sol_filename) as f:
        for line in f:
            if line.strip().startswith("Cost"):
                return int(line.split()[1])