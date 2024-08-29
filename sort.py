# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" with your the name of the active members of the team
__author__ = "Gillian O'Connell (101262146), Phillip Pietrobon (101270421), Tarek Ibrahim (101258978), Jonah Cook (101244113)"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-100"
#==========================================#
# Place your sort_students_age_bubble function after this line


def sort_students_age_bubble(data: list, order: str) -> list:
    """Returns a given list of dictionaries sorted by age based on a given order (acending or
    decending). If "Age" is not present in the dictionarie, an message will be
    printed saying so.

    Preconditions: N/A

    Examples:
    >>>sort_students_age_bubble([{"School": "GP", "Age": 18}, {"School": "MS",
    "Age": 16}, {"School": "GP", "Age": 17}], "A")

    [{"School": "MS", "Age": 16}, {"School": "GP",
        "Age": 17}, {"School": "GP", "Age": 18}]

     >>>sort_students_age_bubble([{"School": "GP", "Age": 18}, {"School": "MS",
    "Age": 16}, {"School": "GP", "Age": 17}], "D")

    [{"School": "GP", "Age": 18}, {"School": "GP",
        "Age": 17}, {"School": "MS", "Age": 16}]

    >>>sort_students_age_bubble([{"School": "GP", "Health": 6}, {"School": "MS",
    "Failures": 2}, {"School": "GP", "Absencens": 17}], "A")

    'Age' is not a present key in list of dictionaries.
    """

    if order == "A":  # Perform acending bubble sort
        swap = True
        while swap:
            swap = False
            if data[0].get("Age") == None:  # Check if age is a key in the dictionaries
                print("'Age' is not a present key in list of dictionaries.")
                break
            else:
                for i in range(len(data) - 1):  # Loop through list to sort by age
                    if data[i].get("Age") > data[i + 1].get("Age"):  # Compare values
                        # Switch if necessary
                        data[i], data[i + 1] = data[i + 1], data[i]
                        swap = True

            return data

    elif order == "D":  # Perform decending bubble sort
        swap = True
        while swap:
            swap = False
            if data[0].get("Age") == None:  # Check if age is a key in the dictionaries
                print("'Age' is not a present key in list of dictionaries.")
                break
            else:
                for i in range(len(data) - 1):  # Loop through list to sort by age
                    if data[i].get("Age") < data[i + 1].get("Age"):  # Compare values
                        # Switch if necessary
                        data[i], data[i + 1] = data[i + 1], data[i]
                        swap = True

        return data

    else:  # User enters invalid order parameter (does not enter "A" or "D")
        return data


#==========================================#
# Place your sort_students_time_selection function after this line
def sort_students_time_selection(stud_list: list, order: str) -> list:
    """
    Return a list of dictionaries ordered by study time in either a descending
    or ascending order depending on user input

    Preconsitions: None

    >>> sort_students_time_selection ([{"StudyTime":10.2,"School":"GP"}, {"StudyTime":19.1,"School":"MS"}], "D")

    [{"StudyTime": 19.1, "School":"MS"}, {"StudyTime":10.2, "School":"GP"}]

    >>> sort_students_time_selection([{"StudyTime": 27.4, "School": "GP"}, {"StudyTime": 13.76, "School": "MS"},
    {"StudyTime": 18.97, "School": "MS"}, {"StudyTime": 11.26, "School": "PC"}, {"StudyTime": 14.2, "School": "PC"}], "A")

    [{'StudyTime': 11.26, 'School': 'PC'}, {'StudyTime': 13.76, 'School': 'MS'}, {'StudyTime': 14.2, 'School': 'PC'},
    {'StudyTime': 18.97, 'School': 'MS'}, {'StudyTime': 27.4, 'School': 'GP'}]

    >>> sort_students_time_selection([{"School": "GP"}, {"School": "MS"}], "D")

    'StudyTime' key is not present
    [{'School': 'GP'}, {'School': 'MS'}]
    """

    # Check if StudyTime is contained in the dictionary
    if "StudyTime" in stud_list[0]:

        if order == "A":  # Check if order value is Ascending

            for i in range(len(stud_list)):  # create for loop for selection sort

                min = i

                for j in range(i + 1, len(stud_list)):
                    # Check if Studytime value minimum is greater than the next studytime value
                    if stud_list[min]["StudyTime"] > stud_list[j]["StudyTime"]:
                        min = j
                stud_list[i], stud_list[min] = stud_list[min], stud_list[i]
            return stud_list  # return final list

        elif order == "D":  # Check if order value is Descending

            for i in range(len(stud_list)):

                min = i

                for j in range(i + 1, len(stud_list)):
                    # Check if Studytime value minimum is less than the next studytime value
                    if stud_list[min]["StudyTime"] < stud_list[j]["StudyTime"]:
                        min = j

                stud_list[i], stud_list[min] = stud_list[min], stud_list[i]
            return stud_list  # return final list

    else:

        print("'StudyTime' key is not present")  # print error message
        return stud_list  # return list without studytime values

#==========================================#
# Place your sort_students_g_avg_insertion function after this line


def sort_students_g_avg_insertion(data: list, order: str) -> list:
    """
    Returns a sorted list when “G_Avg” is a key in the dictionary, if “G_Avg” is not a key
    in the dictionary, the function prints a message stating "G_Avg" key is not present.


    Preconditions: order == 'A' or 'D'

    Examples:

    >>> sort_students_g_avg_insertion([{"G_Avg":10.2,"School":"GP"}, {"G_Avg":19.1,"School":"MS"}, {"G_Avg":13.4,"School":"MS"}], "D")
    [{'G_Avg': 10.2, 'School': 'GP'}, {'G_Avg': 19.1,
        'School': 'MS'}, {'G_Avg': 13.4, 'School': 'MS'}]

    >>> sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}], "D")
    [{"G_Avg": 9.1, "School":"MS"}, {"G_Avg":7.2, "School":"GP"}]

    >>> sort_students_g_avg_insertion([{"School":"GP"},{"School":"MS"}], "D")
    "G_Avg" key is not present
    [{'School': 'GP'}, {'School': 'MS'}]
    """

    for i in range(len(data)):  # loop for how long data is
        if data[i].get('G_Avg') == None:  # check if key is in dictionary
            print('"G_Avg" key is not present')  # print key is not present
        return data  # return given data

    if order == 'A' or order == 'D':  # check asending or decending
        for i in range(1, len(data)):  # loop from 1 - data length
            key = data[i]['G_Avg']  # get g_avg value
            key1 = data[i]  # get index
            j = i - 1
            while j >= 0 and key < data[j]['G_Avg']:  # sorting
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key1

        if order == 'A':  # if its acending, reverse data
            data.reverse()
        return data  # print data

    else:  # if user inputs other than key (A or D) then
        return 'invalid order key'  # print a invalid key

#==========================================#
# Place your sort_students_failures_bubble function after this line


def sort_students_failures_bubble(List: list, key: str):
    """This code is designed to take a list and orginize that list based on the amount of failures that student has. This new organized list can be in ascending or descending order depending on the key value inputed into the argument.

    Preconditions:
    key == 'A' or 'D'

    Example:
    >>>sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
    [{"Failures": 19, "School":"MS"}, {"Failures":10, "School":"GP"}]

    >>> sort_students_ failures _bubble([{"School":"GP"}, {"School":"MS"}], "D")
    "Failures" key is not present.
    [{"School":"GP"}, {"School":"MS"}]

    """
    # This for loop is used to insure that every dictionary in the list has a 'Failure' value.
    for dictionarys in range(len(List)):
        Local = List[dictionarys]
        if Local.get('Failures') == None:
            print('"Failures" key is not present')
            return List
    # This for loop is to orginize this list with ascending values of failures (Smallest to Largest)
    if key == 'A':
        for i in range(len(List)):
            for j in range(0, len(List) - 1 - i):
                if List[j]['Failures'] > List[j + 1]['Failures']:
                    List[j]['Failures'], List[j + 1]['Failures'] = List[j
                                                                        + 1]['Failures'], List[j]['Failures']
    # This for loop is to orginize this list with descending values of failures (Largest to Smallest)
    elif key == 'D':
        for i in range(len(List)):
            for j in range(0, len(List) - 1 - i):
                if List[j]['Failures'] < List[j + 1]['Failures']:
                    List[j + 1]['Failures'], List[j]['Failures'] = List[j]['Failures'], List[j + 1]['Failures']

    return List

#==========================================#
# Place your sort function after this line


def sort(data: list, order: str, sort: str):
    """
    This function lets the user choose how the data will be sorted. It takes three input parameters:
    (1) a list of dictionaries, (2) a string (“A” or “D”) to determine if the students will be sorted in ascending or descending order,
    and (3) a string (“Age”, “StudyTime”, “G_Avg”, “Failures”) to determine the attribute used for sorting.

    Preconditions: order == 'A' or 'D'

    Examples:
    >>>sort([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D", "Failures)
    [{"Failures": 19, "School":"MS"}, {"Failures":10, "School":"GP"}]


    >>>sort([{"G_Avg":10.2,"School":"GP"}, {"G_Avg":19.1,"School":"MS"}, {"G_Avg":13.4,"School":"MS"}], "D", "G_Avg")
    [{'G_Avg': 10.2, 'School': 'GP'}, {'G_Avg': 19.1,'School': 'MS'}, {'G_Avg': 13.4, 'School': 'MS'}]


    >>>sort([{"School": "GP", "Age": 18}, {"School": "MS", "Age": 16}, {"School": "GP", "Age": 17}], "A", "Age")
    [{"School": "MS", "Age": 16}, {"School": "GP", "Age": 17}, {"School": "GP", "Age": 18}]
    """
    if sort == 'Age':  # if chosen sorting is age
        return sort_students_age_bubble(data, order)  # return sorted data

    if sort == 'StudyTime':  # if chosen sorting is studytime
        # return sorted data
        return sort_students_time_selection(data, order)

    if sort == 'G_Avg':  # if chosen sorting is G_avg
        # return sorted data
        return sort_students_g_avg_insertion(data, order)

    if sort == 'Failures':  # if chosen sorting is failures
        # return sorted data
        return sort_students_failures_bubble(data, order)

    # if chosen sorting is neither age/studytime/failures/g_avg
    if sort != ("Failures" or "StudyTime" or "G_Avg" or "Age"):
        print("Cannot be sorted by", sort)  # print a msg for user
        return data  # return data

# Do NOT include a main script in your submission
