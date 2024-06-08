markbook = {}

def addStudent():
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
    print("Student added successfully.")

def isValidStudentID(studentID):
    return len(studentID) == 5 and studentID.isdigit()

def isValidFilename(filename):
    return all(not (not char.isalnum() and char != ' ') for char in filename)

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

def displayMarkbook():
    print("{:<10} {:<15} {:<15} {:<20} {:<5}".format('Student ID', 'First Name', 'Last Name', 'Marks', 'Grade'))
    print('-' * 65)
    for studentID, studentData in markbook.items():
        firstName = studentData['firstName']
        lastName = studentData['lastName']
        marks = ', '.join(str(mark) for mark in studentData['marks'])
        grade = studentData['grade']
        print("{:<10} {:<15} {:<15} {:<20} {:<5}".format(studentID, firstName, lastName, marks, grade))

def saveMarkbook():
    filename = input("Enter filename to save markbook: ")
    if not isValidFilename(filename):
        print("Invalid filename. Please enter a valid filename.")
        return
    try:
        with open(f"{filename}.txt", 'w') as file:
            for studentID, studentData in markbook.items():
                file.write(f"{studentID},{studentData['firstName']},{studentData['lastName']},{','.join(str(mark) for mark in studentData['marks'])},{studentData['grade']}\n")
        print(f"Markbook saved successfully to {filename}.txt")
    except Exception as e:
        print(f"Error saving markbook: {e}")

def loadMarkbook():
    filename = input("Enter filename to load markbook: ")
    if not isValidFilename(filename):
        print("Invalid filename. Please enter a valid filename.")
        return
    try:
        with open(f"{filename}.txt", 'r') as file:
            markbook.clear()
            for line in file:
                studentID, firstName, lastName, marksStr, grade = line.strip().split(',')
                marks = [int(mark) for mark in marksStr.split(',')]
                markbook[studentID] = {
                    'firstName': firstName,
                    'lastName': lastName,
                    'marks': marks,
                    'grade': grade
                }
        print(f"Markbook loaded successfully from {filename}.txt")
    except Exception as e:
        print(f"Error loading markbook: {e}")

def exitProgram():
    print("Exiting program...")

while True:
    print("\nMarkbook Menu:")
    print("1. Add a new student")
    print("2. Add marks for a student")
    print("3. Display markbook")
    print("4. Save markbook")
    print("5. Load markbook")
    print("6. Exit")
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
            print("Invalid choice. Please try again.")
