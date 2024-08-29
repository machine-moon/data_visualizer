# ECOR 1042 Lab 4 - team submission

# import check module here
import check
# import load_data module here
from load_data import load_data_set
from load_data import load_data
from load_data import add_average
from load_data import student_failures_list
from load_data import student_age_list
from load_data import student_health_list
from load_data import student_school_list

# Update "" with your the name of the active members of the team
__author__ = "Gillian O'Connell (101262146), Phillip Pietrobon (101270421), Tarek Ibrahim (101258978), Jonah Cook (101244113)"

# Update "" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-100"

#==========================================#

# Place test_return_list function here


def test_return_list() -> None:
    # Assign file name to variable
    file = "student-test.csv"
    # Complete the function with your test cases

    # test that student_school_list returns a list (3 different test cases required)
    school_input = ["GP", "MS", "Carlton"]  # List containing test cases

    for i in range(0, len(school_input)):
        # Perform check for equivalent type
        check.equal(type(student_school_list(file, school_input[i])), list)

    # test that student_age_list returns a list (3 different test cases required)
    age_input = [17, 18, 67]  # List containing test cases

    for i in range(0, len(age_input)):
        # Perform check of equivalent type
        check.equal(type(student_age_list(file, age_input[i])), list)

    # test that student_health_list returns a list (3 different test cases required)
    health_input = [3, 4, 77]  # List containing test cases

    for i in range(0, len(health_input)):
        # Perform check of equivalent type
        check.equal(type(student_health_list(file, health_input[i])), list)

    # test that student_failures_list returns a list (3 different test cases required)
    fail_input = [1, 20, 3]  # List containing test cases

    for i in range(0, len(fail_input)):
        # Perform check of equivalent type
        check.equal(type(student_failures_list(file, fail_input[i])), list)

    # test that load_data returns a list (6 different test cases required)
    # List containg test cases
    load_key_input = ["Failures", "Age",
                      "SchGSHAHool", "Health", "School", "Age"]
    load_value_input = [1, 28, "GP", 3, "uOttawa", 15]

    for i in range(0, len(load_key_input)):
        # Perform check of equivalent type
        check.equal(
            type(load_data(file, load_key_input[i], load_value_input[i])), list)

    # test that add_average returns a list (3 different test cases required)
    add_v1 = [{'Age': 16, 'StudyTime': 2.0, 'Failures': 0,
               'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}]

    add_v2 = [{'School': 'MB', 'StudyTime': 2.0, 'Failures': 0,
               'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}]

    add_v3 = [{'School': 'MB', 'StudyTime': 2.0, 'Failures': 0,
               'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}]

    add_input = [add_v1, add_v2, add_v3]  # List containing test cases

    for i in range(0, len(add_input)):
        # Perform check of equivalent type
        check.equal(type(add_average(add_input[i])), list)
    check.summary()
    return None
# Place test_return_list_correct_lenght function here


def test_return_list_correct_lenght() -> None:
    # Complete the function with your test cases

    # test that student_school_list returns a list with the correct lenght (3 different test cases required)
    check.equal(len(student_school_list("student-test.csv", "GP")), 3)
    check.equal(len(student_school_list("student-test.csv", "MB")), 2)
    check.equal(len(student_school_list("student-test.csv", "CF")), 3)

    # test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(student_age_list("student-test.csv", 18)), 4)
    check.equal(len(student_age_list("student-test.csv", 15)), 3)
    check.equal(len(student_age_list("student-test.csv", 47)), 0)

    # test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(student_health_list("student-test.csv", 3)), 8)
    check.equal(len(student_health_list("student-test.csv", 5)), 3)
    check.equal(len(student_health_list("student-test.csv", 4)), 3)

    # test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    check.equal(len(student_failures_list("student-test.csv", 0)), 11)
    check.equal(len(student_failures_list("student-test.csv", 3)), 1)
    check.equal(len(student_failures_list("student-test.csv", 2)), 2)

    # test that load_data returns a list  with the correct lenght (6 different test cases required)
    check.equal(len(load_data("student-test.csv", "School", "GP")), 3)
    check.equal(len(load_data("student-test.csv", "Age", 16)), 2)
    check.equal(len(load_data("student-test.csv", "Failures", 3)), 1)
    check.equal(len(load_data("student-test.csv", "Health", 5)), 3)
    check.equal(len(load_data("student-test.csv", "School", "PP")), 0)
    check.equal(len(load_data("student-test.csv", "All", 1)), 15)

    # test that add_average returns a list   with the correct lenght (3 different test cases required)
    check.equal(len(add_average([{"School": "GP", "Age": 18, "StudyTime": 2.0,
                "Health": 3, "Absences": 6, "G1": 5, "G2": 6, "G3": 6}])), 1)
    check.equal(len(add_average([{"School": "MB", "Age": 16, "StudyTime": 2.0,
                "Health": 3, "Absences": 12, "G1": 5, "G2": 5, "G3": 5}])), 1)
    check.equal(len(add_average([{"School": "BD", "Age": 18, "StudyTime": 2.0,
                "Health": 3, "Absences": 2, "G1": 8, "G2": 8, "G3": 8}])), 1)

    check.summary()
    return None
# Place test_return_correct_dict_inside_list function here


def test_return_correct_dict_inside_list() -> None:

    # Complete the function with your test cases

    # test that student_school_list returns a correct dictionary inside the list (3 different test cases required)

    check.equal([student_school_list("student-test.csv", "CF")[1]],  # check file, school, index
                [{'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}])
    check.equal([student_school_list("student-test.csv", 'BD')[2]],  # check file, school, index
                [{'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9}])
    check.equal(student_school_list("student-test.csv", 'AB'),
                [])  # check file, school, index

    # test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)

    check.equal([student_age_list("student-test.csv", 18)[1]],  # check file, age, index
                [{'School': 'BD', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 8}])
    check.equal([student_age_list("student-test.csv", 17)[2]],  # check file, age, index
                [{'School': 'BD', 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9}])
    check.equal(student_age_list("student-test.csv", 19),
                [])  # check file, age, index

    # test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)

    check.equal([student_health_list("student-test.csv", 3)[1]],  # check file, health, index
                [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}])
    check.equal([student_health_list("student-test.csv", 5)[2]],  # check file, health, index
                [{'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])
    check.equal(student_health_list("student-test.csv", 7),
                [])  # check file, health, index

    # test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)

    check.equal([student_failures_list("student-test.csv", 0)[1]],  # check file, failures, index
                [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}])
    check.equal([student_failures_list("student-test.csv", 3)[0]],  # check file, failures, index
                [{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}])
    check.equal(student_failures_list("student-test.csv", 6),
                [])  # check file, failures, index

    # test that load_data returns a correct dictionary inside the list (6 different test cases required)

    check.equal([load_data("student-test.csv", 'All', 0)[0]],  # check file, load data, index
                [{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}])
    check.equal([load_data("student-test.csv", 'Failures', 1)[0]],  # check file, load data, index
                [{'School': 'CF', 'Age': 16, 'StudyTime': 2, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}])
    check.equal([load_data("student-test.csv", 'Age', 16)[1]],  # check file, load data, index
                [{'School': 'CF', 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}])
    check.equal([load_data("student-test.csv", 'Health', 4)[2]],  # check file, load data, index
                [{'School': 'MS', 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}])
    check.equal([load_data("student-test.csv", 'School', 'MS')[1]],  # check file, load data, index
                [{'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 1, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}])
    check.equal(load_data("student-test.csv", 'School', 'AB'),
                [])  # check file, load data, index

    # test that add_average returns a lcorrect dictionary inside the list  (3 different test cases required)

    check.equal(add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}]),  # check avg
                [{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}])
    check.equal(add_average([{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}]),  # check avg
                [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33}])
    check.equal(add_average([{'School': 'BD', 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9}]),  # check avg
                [{'School': 'BD', 'Age': 17, 'StudyTime': 3, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9, 'G_Avg': 9.33}])

    check.summary()  # prints: Ran # tests, # failed
    return None

# Place test_add_average function here


def test_add_average() -> None:
    # Complete the function with your test cases
    add_average_tests = [add_average(student_school_list('student-test.csv', 'MB')), add_average(student_health_list('student-test.csv', 5)), add_average(
        student_age_list('student-test.csv', 18)), add_average(student_failures_list('student-test.csv', 2)), add_average(load_data('student-test.csv', 'All', None))]
    tests = [student_school_list('student-test.csv', 'MB'), student_health_list('student-test.csv', 5), student_age_list(
        'student-test.csv', 18), student_failures_list('student-test.csv', 2), load_data('student-test.csv', 'All', None)]

    # test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)
    for i in range(len(tests)):
        check.equal(len(add_average_tests[i]), len(tests[i]), '')
    # test that the function returns an empty list when it is called whith an empty list
    check.equal(add_average([]), [], '')

    # test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    Test2 = True
    for Functions in (add_average_tests):
        for dictionarys in Functions:
            if Functions != add_average_tests[4]:
                if (len(dictionarys) - 1) != 8:
                    Test2 = False
            elif Functions == add_average_tests[4]:
                if (len(dictionarys) - 1) != 9:
                    Test2 = False
        check.equal((Test2), True, '')
        Test2 = True

    # test that the G_Avg value is properly calculated  (5 different test cases required)
    Test3 = True
    for Functions in (add_average_tests):
        for dictionarys in Functions:
            if round(((dictionarys.get('G1')) + (dictionarys.get('G2')) + (dictionarys.get('G3'))) / 3, 2) != dictionarys.get('G_Avg'):
                Test3 = False
        check.equal((Test3), True, '')
        Test3 = True

    check.summary()
    return None

# Do NOT include a main script in your submission
