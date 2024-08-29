# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Jonah Cook"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101244113"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-100"

#==========================================#
# Place your script for your batch_UI after this line


from Load_data import *
from sort import *
from histogram import *
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
#The curve_fit function is altered code from my group member used to display the equation of the polynomial
def curve_fit_A(data: list, key: str, degree: int):
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
    return equation





L_Data = []
Data = []
print('Please enter the name of the file where your commands are stored')
#This code interpretes the .txt file and creates a List with all commands
filename = input()
infile = open(filename, 'r')  # open filename
for lines in(infile):
    The_Values = lines.split(';')
    The_Values[-1] = The_Values[-1].strip('\n')
    Data.append(The_Values)
#This code will iterate throught the list to each 'full commmand' line
for Lists in(Data):
    #This code user the load data and add_average function from lab 3 to load your csv file
    if Lists[0] == 'L' or Lists[0] == 'l':
        if Lists[2] == 'School':
            L_Data = []
            L_Data = load_data(Lists[1],Lists[2],Lists[3])
            L_Data = add_average(L_Data)
            print('Data loaded') 
        else:
            L_Data = []
            L_Data = load_data(Lists[1],Lists[2],int(Lists[3]))
            L_Data = add_average(L_Data)
            print('Data loaded')     
    #This code uses the sort function from lab 5 to sort throught the Loaded Data
    elif Lists[0] == 'S' or Lists[0] == 's':
        if L_Data == []:
            print('File not loaded. Please, load a file first.')
        else:
            L_Data = sort(L_Data,Lists[2],Lists[1])
            if Lists[3] == 'Y':
                print('Data sorted')
                print(L_Data)
            elif Lists[3] == 'N':
                print('Data sorted. <<<You selected not to display>>>')
    #This code uses the Histogram function from lab 6 to create a histogram with the desired data
    elif Lists[0] == 'H' or Lists[0] == 'h':
        if L_Data == []:
            print('File not loaded. Please, load a file first.')
        else:
            histogram(L_Data,Lists[1])
    #This code uses the curve_fit function in lab 6 to display the equation for the polynomial
    elif Lists[0] == 'C' or Lists[0] == 'c':
        if L_Data == []:
            print('File not loaded. Please, load a file first.')
        else:
            Filler = curve_fit_A(L_Data,Lists[1],int(Lists[2]))
            print(Filler)
            

