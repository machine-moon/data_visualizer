# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Gillian O’Connell (101262146), Tarek Ibrahim (101258978), Phillip Pietrobon 101270421. Jonah Cook(101244113)"

# Update "" with your team (e.g. T102)
__team__ = "T100"

#==========================================#
# Place your student_school_list function after this line


def student_school_list(filename: str, school: str) -> list:
    """Return a list of dictionaries that each the information (school, age, 
    study time, absenses, G1, G2, and G3) for each student that belongs to a 
    given school. If the given school does not exist, return an empty list.

    Preconditions: N/A

    >>>student_school_list("student-mat.txt", "MB")
    [{'Age': 16, 'Study Time': 2, 'Failures': 0, 'Health': 3,
      'Absenses': 12, 'G1': 5, 'G2': 5,'G3': 5}, {another student...}, ...]
    """
    # Create list for students
    student_list = []
    # Create and declare boolean to collect header
    first_line = True

    # Open file
    file = open(filename, "r")

    # Loop through CSV file to create list of students who belong to a given school school
    for line in file:
        # Obtain data titles from file header
        if first_line == True:
            header = line.split(",")
            header[8] = header[8].strip("\n")
            first_line = False
    # Analyse and collect applicable student data
        else:
            # Split line of data and save in a list for current student being checked
            info_line = line.split(",")
            # Check if student belongs to given school
            if info_line[0] == school:
                # If student blongs to school, add student's data to list in dictionary
                student_list.append({header[1]: int(info_line[1]),
                                     header[2]: float(info_line[2]),
                                     header[3]: int(info_line[3]),
                                     header[4]: int(info_line[4]),
                                     header[5]: int(info_line[5]),
                                     header[6]: int(info_line[6]),
                                     header[7]: int(info_line[7]),
                                     header[8]: int(info_line[8])})

    file.close()
    return student_list

#==========================================#
# Place your student_health_list function after this line


def student_health_list(filename: str, Health: str) -> list:
    """This code is designed to take a csv file and a health value stored as an
    integer and return a list of student dictionarys of students with the same
    health value.

    Preconditions: 0 < Health <= 5

    >>>student_health_list('student-mat.csv', 2)
    [{'School': 'GP',
    'Age': 15,
    'StudyTime': 2,
    'Failures': 0,
    'Absences': 0,
    'G1': 10,
    'G2': 8,
    'G3': 9},
    {another element},
    ...
    ]
    """
    Students = []
    # Runs load_data_set and its returned list is stored as Student_List
    Student_List = load_data_set(filename)
    # Iterates throught based on length of student dictionarys
    for i in range(len(Student_List)):
        # Creates a temporary varible for the student dictionary
        Local = Student_List[i]
        # Determins if the student has the desired health value
        if Local.get('Health') == Health:
            # Removes 'Health' key and value from the dictionary
            del Local['Health']
            # Appends the dictionary to a list for storage
            Students.append(Local)
    # Returns the List of student dictionarys with the desired health value
    return Students


def load_data_set(filename):
    """This is an addition code written by Jonah Cook used to simplify his code
    and also used in the add_average and the load_data
    Example:
    >>>load_data_set('student-mat.csv')
    [{'School': 'GP',
    'Age': 18,
    'StudyTime': 2,
    'Failures': 0,
    'Health': 3,
    'Absences': 6,
    'G1': 5,
    'G2': 6,
    'G3': 6},
    {another element}
    ...
    ]
    """
    # Creates two empty lists of students
    Students = []
    Student_List = []
    # Opens the desired file
    infile = open(filename, 'r')
    # Creates a list of Key Values based on the headers of the csv file
    header_list = infile.readline().strip('\n').strip(' ').split(',')
    # Iterates through the lines of the csv file one at a time
    for lines in (infile):
        # Creates a temporary list of each line for each iteration
        The_Values = lines.split(',')
        # Creates an empty dicitonary
        Local = {}
        # Iterates through The_Values and assignes Key_values based on position in the list
        for i in range(len(header_list)):
            # These booleans change The_Values into integers with the exception of School
            if header_list[i] == 'School':
                # Creates a Key_Value pair and stores it to Local
                Local[header_list[i]] = The_Values[i].strip()
            else:
                # Creates a Key_Value pair then changes it to and integer and stores it to Local
                Local[header_list[i]] = int(The_Values[i].strip())
        # Appends the dictionary to a List to store
        Student_List.append(Local)
    return Student_List


#==========================================#
# Place your student_age_list function after this line
def student_age_list(file_name: str, Age: str) -> list:
    """
    Return a list of students stored as a dictionary with the same age inputed.
    The keys of the dictionary should be the same labels for all attributes in the given spreadsheet
    aside from "Age". Return an empty list if the age inputed is not on the file

    Preconditions: Age >= 0

    Examples:

    >>>student_age_list('student-mat.csv', 15)
    [{'School': 'GP', 'StudyTime': 4.2, 'Failures': 3, 'Health': 3, 'Absences': 6,
    'G1': 7, 'G2': 8, 'G3': 10}
    {another element},
    ...
    ]
    """
    first_line = True  # set first_line = True
    student_list = []  # define student_list list

    # open the file
    file = open(file_name, "r")

    # itterate each line through the file
    for line in file:
        if first_line == True:  # Check if the line is the first line
            header = line.split(",")  # create list of title values
            # strip the entire first row of titles
            header[8] = header[8].strip("\n")
            first_line = False  # set first_line = false
        else:
            # create list of each file line composed of strings
            info_line = line.split(",")
            # check if the age section of list info_line is = to the age inputed
            if int(info_line[1]) == Age:

                # Add the following dictionaries to the final list student_list not including Age
                student_list.append({header[0]: (info_line[0]),
                                     header[2]: float(info_line[2]),
                                     header[3]: int(info_line[3]),
                                     header[4]: int(info_line[4]),
                                     header[5]: int(info_line[5]),
                                     header[6]: int(info_line[6]),
                                     header[7]: int(info_line[7]),
                                     header[8]: int(info_line[8])})
    # close the file and return student_list
    file.close()
    return student_list


#==========================================#
# Place your student_failures_list function after this line
def student_failures_list(filename: str, Failures: str) -> list:
    """
    Return a list of students with the same number of failures inputed.

    Preconditions: Failures >= 0

    Example:

    >>> student_failures_list('student-mat.csv', 3)
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Health': 3, 'Absences': 10,
    'G1': 7, 'G2': 8, 'G3': 10},
    {another element},
    ...
    ]
    """
    Students = []  # Create list for students

    infile = open(filename)  # open filename
    header_list = infile.readline().strip('\n').split(',')
    Key_values = []  # Create list for Key_values
    Student_List = []  # Create list for Student_List
    for string in (header_list):  # create for loop to organize values
        string = string.strip()
        Key_values.append(string)

    for lines in (infile):
        The_Values = lines.split(',')  # use , to seperate elements
        Local = {}  # define dictionary Local
        for i in range(len(Key_values)):  # loop for however long Key_values in length
            if Key_values[i] == 'School':
                # school name is string ' '
                Local[Key_values[i]] = The_Values[i].strip()
            else:
                # $result is int (age,health,etc)
                Local[Key_values[i]] = int(The_Values[i].strip())
        Student_List.append(Local)  # add to list

    for i in range(len(Student_List)):  # loop for however long Student_List in length
        # store student list in local per i itteration
        Local = Student_List[i]
        if Local.get('Failures') == Failures:
            del Local['Failures']
            Students.append(Local)  # add to list
    return Students  # Return

#==========================================#
# Place your load_data function after this line


def load_data(Filename: str, key: str, Desired_Key_Value: str or int or None) -> list or None:
    """This code is designed to take a csv file and return a list of students 
    based on the key inputed and the desired key value

    Example:
    >>>load_data('student-mat.csv','Failures',1)
    [{'School': 'GP',
    'Age': 16,
    'StudyTime': 2,
    'Health': 3,
    'Absences': 25,
    'G1': 7,
    'G2': 10,
    'G3': 11},
    {another element}
    ...
    ]
    """
    # Boolean statement to determine if key is "School"
    if key == "School":
        # Runs student_school_list function wiht filename and Desired_Key_Value
        return student_school_list(Filename, Desired_Key_Value)
    # Boolean statement to determine if key is "Age"
    elif key == "Age":
        # Runs student_age_list function wiht filename and Desired_Key_Value
        return student_age_list(Filename, Desired_Key_Value)
    # Boolean statement to determine if key is "Health"
    elif key == "Health":
        # Runs student_health_list function wiht filename and Desired_Key_Value
        return student_health_list(Filename, Desired_Key_Value)
    # Boolean statement to determine if key is "Failures"
    elif key == "Failures":
        # Runs student_failures_list function wiht filename and Desired_Key_Value
        return student_failures_list(Filename, Desired_Key_Value)
    # Boolean statement to determine if key is "All"
    elif key == 'All':
        # Runs load_data_set function wiht filenmae
        return load_data_set(Filename)
    else:
        return []

#==========================================#
# Place your add_average function after this line


def add_average(Student_List: list):
    """This code is designed to take a csv file and return an appended list with
     a new key called G_Avg based on 3 key_values in the list.

    Example:
    >>>add_average('student-mat.csv')
    [{'School': 'GP',
    'Age': 18,
    'StudyTime': 2,
    'Failures': 0,
    'Health': 3,
    'Absences': 6,
    'G1': 5,
    'G2': 6,
    'G3': 6,
    'G_Avg': '5.67'},
    {another element}
    ...
    ]
    """
    # Iterates Student_list based on length of Student_list
    for i in range(len(Student_List)):
        # creates a temporary varible based on the iteration
        Line = Student_List[i]
        # creates a temporary variable based on the average of G1,G2,G3 and rounds that figure to 2 decimal points
        Local = round(
            ((Line.get('G1')) + (Line.get('G2')) + (Line.get('G3'))) / 3, 2)
        # Updates List to add a new key and key_value
        Student_List[i].update({'G_Avg': float(Local)})
    return Student_List
