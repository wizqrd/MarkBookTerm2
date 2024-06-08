markbook = {}

def addStudent(): # Adds a students firstname, lastname and unique 5 digit student ID
    firstName = input("Enter first name please: ")
    lastName = input("Enter last name please: ")
    studentID = input("Enter student ID (5 digit numeric string): ") 
    if not isValidStudentID(studentID):
        print("Invalid student ID. Please enter a 5 digit numeric string.")
        return
    if studentID in markbook:
        print("Student ID already exists.")
        return
    markbook[studentID] = {
        'firstName': firstName,
        'lastName': lastName,   
        'marks': [],
        'grade': 'N/A'
    }
    print("Student added successfully.") # yay
# Adds a students firstname, lastname and unique 5 digit student ID
def isValidStudentID(studentID):
    return len(studentID) == 5 and studentID.isdigit() 
# Checks if length is five, id is digit
def isValidFilename(filename):
    return all(not (not char.isalnum() and char != ' ') for char in filename) 
# Checks if alphanumeric and if there is a space
def addMarks():
    studentID = input("Enter student ID: ")
    if studentID not in markbook:
        print("Student ID not found.")
        return
    mark = input("Enter mark (0-100): ")
    if not mark.isdigit() or int(mark) < 0 or int(mark) > 100:
        print("Invalid mark. Please enter a value between 0 and 100.")
        return
    markbook[studentID]['marks'].append(int(mark))
    print("Mark added successfully.")
    calculateGrade(studentID)

'''Takes user input (ID) then runs through a loop to check if its a digit, and is 
between 0 and 100, ending the loop when its correct. Adds marks to Dictionary when
finished...'''
def calculateGrade(studentID):
    marks = markbook[studentID]['marks']
    averageMark = sum(marks) / len(marks) if marks else 0
    match averageMark:
        case mark if 90 <= mark <= 100:
            grade = 'A'
        case mark if 74 <= mark <= 89:
            grade = 'B'
        case mark if 60 <= mark <= 75:
            grade = 'C'
        case mark if 50 <= mark <= 59:
            grade = 'D'
        case mark if 0 <= mark <= 49:
            grade = 'F'
        case _:
            grade = 'N/A'
    markbook[studentID]['grade'] = grade
# Uses a math statement to math mark to grade, and stores it in markbook dictionary
def displayMarkbook():
    print("{:<10} {:<15} {:<15} {:<20} {:<5}".format('Student ID', 'First Name', 
                                                     'Last Name', 'Marks', 'Grade'))
    print('-' * 65)
    for studentID, studentData in markbook.items():
        firstName = studentData['firstName']
        lastName = studentData['lastName']
        marks = ' , '.join(str(mark) for mark in studentData['marks'])
        grade = studentData['grade']
        print("{:<10} {:<15} {:<15} {:<20} {:<5}".format(studentID, firstName, lastName,
                                                         marks, grade))
# This shows the markbook dictionary to the console
def saveMarkbook():
    filename = input("Enter filename to save markbook: ")
    if not isValidFilename(filename):
        print("Invalid filename. Please enter a valid filename.")
        return
    try:
        with open(f"{filename}.txt", 'w') as file:
            for studentID, studentData in markbook.items():
                file.write(f"{studentID},{studentData['firstName']},{studentData['lastName']},{','.join(str(mark) for mark in studentData['marks'])},{studentData['grade']}\n")
        print(f"markbook saved successfully to {filename}.txt")
    except Exception as e:
        print(f"Uh-oh, Error saving markbook: {e}")

def loadMarkbook():
    filename = input("Enter filename to load markbook: ")
    if not isValidFilename(filename):
        print("Non-valid filename. Please enter a valid filename.")
        return
    try:
        with open(f"{filename}.txt", 'r') as file:
            markbook.clear()
            for line in file:
                studentID, firstName, lastName, marksStr, grade = line.strip().split(' | ')
                marks = [int(mark) for mark in marksStr.split(' | ')]
                markbook[studentID] = {
                    'firstName': firstName,
                    'lastName': lastName,
                    'marks': marks,
                    'grade': grade
                }
        print(f"Markbook loaded successfully from {filename}.txt")
    except Exception as e:
        print(f"Oh dear, Error loading markbook: {e}")
"""This reads the inputted file name, validates the name, clears any of the data and 
then stores in the markbook dictionary"""
def exitProgram():
    print("Exiting program, see you soon.")
# Nice bye bye message.
while True:
    print("\nMarkbook Hub:")
    print("1. Add a new student")
    print("2. Give marks to a student")
    print("3. Display the markbook")
    print("4. Save the markbook")
    print("5. Load the markbook")
    print("6. Exit :(")
    choice = input("Enter your choice (1-6): ")
    match choice:
        case '1':
            addStudent()
        case '2':
            addMarks()
        case '3':
            displayMarkbook()
        case '4':
            saveMarkbook()
        case '5':
            loadMarkbook()
        case '6':
            exitProgram()
            break
        case _:
            print("Womp, Invalid choice. Please try again.")
# This is the main hub, the user will input the number for their choice.



# Dev Note-
# | Not quite completed as i'm still stuck on file manipulation
# | Missing some organisation, and used outside help for the load and save (Not AI)
# | Shoutout to Chase for the minimising of functions.