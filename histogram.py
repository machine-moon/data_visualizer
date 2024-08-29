# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions
import matplotlib.pyplot as plt


# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Phillip Pietrobon"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101270421"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-100"

#==========================================#
# Place your histogram function after this line


def histogram(student_list: list, attribute: str) -> None:
    """
    Displays a histogram of an indicated attribute of a dictionary of students.
    Function returns None
    
    Preconditions: None
    
    >>>histogram([{"Health": 2}, {"Health": 3}, {"Health": 2 }, {"Health": 6 }, {"Health": 3 }, {"Health": 6 }, {"Health": 1 }, {"Health": 3 }, {"Health": 2 }], "Health")
    
    """
    #define empty values
    lst = []
    quantity = 0
    dict = {}

    for i in range(0, len(student_list)): #Take inputs from input list of dictionaries
        lst.append((student_list[i][attribute])) #convert values associated with keys to a list
        if type(lst[i]) == float: #check if list contains float values
            lst[i] = round(lst[i], 0) #round float values to nearest int to make intervals of whole numbers (ex: 2.5 -> 3.49, 3.5 -> 4.49, etc)
            
    for i in range(0, len(lst)): #count the number of identical numbers in the list
        quantity = 0
        for j in range(0, len(lst)):
            if lst[i] == lst[j]:
                quantity += 1
        dict[lst[i]] = quantity #create new dictionary of all values with repititions

    for key in dict: #graph the data from the dictionary 
        plt.bar(key, dict[key], 0.5, color = "dodgerblue")
        plt.title(attribute + " Graph (Rounded to Nearest Whole Number)")
        plt.xlabel(attribute + " value")
        plt.ylabel("Number of Students")
        
    plt.show() #show graph
        
    return None

# Do NOT include a main script in your submission
