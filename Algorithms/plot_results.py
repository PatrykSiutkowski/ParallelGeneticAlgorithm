#!/usr/bin/env python3

import os
import matplotlib.pyplot as plt
import numpy as np

def plot_results(vertices, solution, distance_over_time, distance_found, filename, shortest, algo, exval):
    base = os.path.basename(filename) 
    name = os.path.splitext(base)[0] 
    shortest_distance_possible = shortest

    colors = ['blue', 'green', 'red', 'purple', 'cyan', 'grey', 'pink']
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    if algo == "ant":
        fig.suptitle(f"Vehicle Routing Solution using Ant Colony Optimisation for: {name}", fontsize=12)
    elif algo == "ga":
        fig.suptitle(f"Vehicle Routing Solution using Genetic Algorithm for: {name}", fontsize=12)
    else:
        fig.suptitle(f"Vehicle Routing Solution using Artifical for: {name}", fontsize=12)

    for idx, route in enumerate(solution):
        color = colors[idx % len(colors)]
        x = [vertices[i].x for i in route] + [vertices[route[0]].x]
        y = [vertices[i].y for i in route] + [vertices[route[0]].y]
        axs[0].plot(x, y, marker='o', color=color, label=f"Vehicle {idx+1}")
    
    axs[0].scatter(vertices[0].x, vertices[0].y, color='black', s=100, label='Depot')
    axs[0].set_title("Vehicle Routes", fontsize=10)
    axs[0].legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4, fontsize=6)
    
    # Plot Convergence
    axs[1].plot(distance_over_time)
    axs[1].set_title(f"Convergence", fontsize=10)
    axs[1].set_xlabel("Generation")
    axs[1].set_ylabel("Distance")
    axs[1].text(0.5, -0.25, f"Shortest Distance possible: {shortest_distance_possible}", transform=axs[1].transAxes, ha='center')
    axs[1].text(0.5, -0.30, f"Shortest Distance found: {distance_found:.0f}", transform=axs[1].transAxes, ha='center')

    plt.tight_layout()
    #plt.savefig(f"/home/patryksiutkowski/GitHub/VRPAlgorithmComparison/Results/{algo}/{algo}_{name}_on_{datetime.datetime.now().strftime('%Y.%m.%d')}_at_{datetime.datetime.now().strftime('%H:%M')}.png")
    plt.savefig(f"/home/patryksiutkowski/GitHub/VRPAlgorithmComparison/Results/{algo.upper()}/{name}/{algo}_{name}_test_no_{exval}.png")
    plt.show()

def plot_all_results(): # This plot is a last minute addition to the dissertaion, hence the hard coding.
    abc_data = {
        "ABC F-n45-k4":  [834, 829, 750, 771, 790, 769, 785, 749, 815, 776],
        "ABC F-n72-k4":  [294, 262, 312, 300, 272, 350, 299, 358, 354, 271],
        "ABC F-n135-k7": [1631, 1670, 1649, 1636, 1697, 1598, 1643, 1623, 1710, 1725]
    }
    
    aco_data = {
        "ACO F-n45-k4":  [919, 972, 941, 880, 933, 951, 928, 868, 926, 870],
        "ACO F-n72-k4":  [336, 334, 331, 327, 332, 340, 330, 326, 337, 335],
        "ACO F-n135-k7": [1617, 1589, 1624, 1621, 1664, 1645, 1659, 1587, 1611, 1607]
    }
    
    ga_data = {
        "GA F-n45-k4":  [857, 907, 934, 1071, 922, 865, 1021, 907, 925, 1005],
        "GA F-n72-k4":  [432, 374, 403, 396, 366, 387, 366, 379, 438, 436],
        "GA F-n135-k7": [2191, 2235, 2111, 2374, 2264, 2182, 2272, 2284, 2011, 2503]
    }

    
    all_rows = []# Combine data and calculate
    for dataset in [abc_data, aco_data, ga_data]:
        for label, values in dataset.items():
            avg = round(np.mean(values), 2)
            best = np.min(values) # Minimum distance is the "Best" for CVRP
            all_rows.append([label] + values + [avg, best])

    
    columns = ["Algo &\nDataset", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "Average", "Best"] # Table Setup
    
    fig, ax = plt.subplots(figsize=(18, 6)) # Width increased to fit columns
    ax.axis('tight')
    ax.axis('off')

    table = ax.table(cellText=all_rows, colLabels=columns, loc='center', cellLoc='center')# Create Table

    # Styling
    table.auto_set_font_size(False)
    table.set_fontsize(13)
    table.scale(1.2, 4.0)

    # Highlighting and Formatting
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor('#2c3e50') # Navy background for header
            cell.set_text_props(color='white', weight='bold')
        elif row % 2 == 0:
            cell.set_facecolor('#95aed8') # Light grey for labels
        if col == 0:
            cell.set_text_props(weight='bold')   
        


    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_all_results()