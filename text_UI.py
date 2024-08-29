# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Tarek Ibrahim"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101258978"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-100"

#==========================================#
# Place your script for your text_UI after this line

import matplotlib.pyplot as plt
from sort import sort
from load_data import load_data
from load_data import add_average
from curve_fit import curve_fit
from histogram import histogram

loaded = False


def main_menu():
    return input("The available commands are:\n L)oad Data\n S)ort Data\n C)urve Fit\n H)istogram\n E)xit\n\nPlease type your command: ")


def text_UI():
    """
    returns..
    """

    try:
        loaded = False
        command = main_menu()
        attributes = ("School", "Age", "StudyTime", "Failures",
                      "Health", "Absences", "G1", "G2", "G3", "All")

        while command != "E" or command != "e":

            if command == "L" or command == "l":
                filename = input("Please enter the name of the file: ")
                attribute = input(
                    "Please enter the attribute to use as a filter: ")

                while attribute not in attributes:
                    attribute = input(
                        "Invalid attribute. Please enter the attribute to use as a filter:")

                if attribute == 'All':
                    loaded_data = load_data(filename, (attribute, 0))
                    loaded_data_avg = add_average(loaded_data)
                elif attribute == 'School':
                    attribute_value = input(
                        "Please enter the value of the attribute: ")
                    loaded_data = load_data(
                        filename, attribute, attribute_value)
                    loaded_data_avg = add_average(loaded_data)
                else:
                    attribute_value = int(
                        input("Please enter the value of the attribute: "))
                    loaded_data = load_data(
                        filename, attribute, attribute_value)
                    loaded_data_avg = add_average(loaded_data)
                loaded = True
                print("\n", "Data Loaded", "\n")

            elif command == "S" or command == "s":
                while loaded == False:
                    print("\n", "File not loaded. Please, load a file first.", "\n")
                    main_menu()

                sort_method = input(
                    "Please enter the attribute you want to use for sorting: \n'Age' 'StudyTime' 'Failures' 'G_Avg\n:")
                while sort_method not in attributes:
                    sort_method = input(
                        "Attribute is invalid \nPlease enter the attributed you want to use for sorting:\n'Age' 'StudyTime' 'Failures' 'G_Avg\n:")

                order = input("Ascending (A) or Descending (D) order: ")
                display_data = input(
                    "Data Sorted. Do you want to display the data? (Y/N): ")

                if display_data == "Y" or display_data == "y":
                    print(sort(loaded_data_avg, order, sort_method))

                elif display_data == "N" or display_data == "n":
                    print("\n")
                    main_menu()
                else:
                    print("Invalid input", "\n")
                    main_menu()

            elif command == "C" or command == "c":
                while loaded == False:
                    print("File not loaded. Please, load a file first.", "\n")
                    main_menu()

                key = input(
                    "Please enter the attribute you want to use to find the best fit for G_Avg:")
                degree = int(
                    input("Please enter the order of the polynomial to be fitted:"))
                print(curve_fit(loaded_data_avg, key, degree))

            elif command == "H" or command == "h":
                while loaded == False:
                    print("File not loaded. Please, load a file first.", "\n")
                    main_menu()

                attribute = input(
                    "Please enter the attribute you want to use for plotting:")
                print(histogram(loaded_data_avg, attribute))

            else:
                print("Invalid Input. Restarting Program...")
            command = main_menu()

    except ValueError:
        print("Invalid Input. Restarting Program...")
        main_menu()


text_UI()




