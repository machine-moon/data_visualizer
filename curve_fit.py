# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Gillian O'Connell"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101262146"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-100"

#==========================================#
# Place your curve_fit function after this line
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc


def curve_fit(data: list, key: str, degree: int):
    """Return an equation of best fit and display a graph for a data set given 
    a list of dictionaries containing 'G_Avg' and a given key. 

    Preconditions: 'G_Avg' and selected key are in all list indecies. 

    Examples:
    >>>curve_fit([{"G_Avg": 1, "Health": 1}, {"G_Avg": 2, "Health": 2}, {"G_Avg": 3, "Health": 3}, {"G_Avg": 4, "Health": 2}], "Health", 2)
    'y=-1x^2+5x^1-3'
    >>>curve_fit([{"G_Avg": 2, "Health": 1}, {"G_Avg": 4, "Health": 2}, {"G_Avg": 6, "Health": 3}], "Health", 1)
    'y=2.0x^1'
    """
    # Define variables and storages
    current_key_value = 0
    key_values = set()
    key_list = []
    average = 0
    key_count = 0
    y_vals = []
    equation = "y="

    # Create list of key values
    for i in range(0, len(data)):
        key_values.add(data[i].get(key))
    key_list = list(key_values)

    # Loop through list to find average g_avg for each key value
    for i in range(0, len(key_list)):
        current_key_value = key_list[i]
        key_count = 0
        average = 0
        for j in range(0, len(data)):
            if data[j].get(key) == current_key_value:
                average += data[j].get("G_Avg")
                key_count += 1
        average = average / key_count
        y_vals.append(average)
    coef = np.polyfit(key_list, y_vals, degree)

    # Round coefficients to one decimal place
    for i in range(0, len(coef)):
        coef[i] = "{:.1f}".format(coef[i])

    # Create equation
    expo = degree
    for i in range(0, len(coef)):
        if int(coef[i]) != 0:
            if i == 0:
                equation += str(coef[i]) + "x^" + str(expo)
                expo -= 1
            elif expo == 0:
                equation += str(coef[i])
            elif coef[i] < 0:
                equation += str(coef[i]) + "x^" + str(expo)
                expo -= 1
            else:
                equation += "+" + \
                    str(coef[i]) + "x^" + str(expo)
                expo -= 1

    # Create plot with interpolation (connnect the dots)
    if degree < (len(key_list) - 1):
        fig = plt.figure()
        plt.plot(key_list, y_vals, 'go--')
        plt.title(key + "and G_Avg Graph")
        plt.xlabel(key + " values")
        plt.ylabel("G_Avg")
        plt.show()
    # Create plot with regression (line of best fit)
    else:
        x = np.linspace(min(key_list), max(key_list), len(key_list))
        x_e = np.linspace(min(key_list), max(key_list), 100)
        y_e = np.polyval(coef, x_e)
        plt.plot(x, y_vals, 'o', x_e, y_e, '-')
        plt.title(key + "and G_Avg Graph")
        plt.xlabel(key + " values")
        plt.ylabel("G_Avg values")
        plt.show()

    return equation

# Do NOT include a main script in your submission
