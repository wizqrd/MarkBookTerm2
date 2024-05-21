markbook = {}

def add_student():
    firstName = input("Enter the student's first name: ")
    lastName = input("Enter the student's last name: ")
    studentID = input("Enter the student's ID: ")
    if not is_valid_student_id(studentID):
        print("Invalid student ID. Enter 5 digit Num.")
        return
    if studentID in markbook:
        print("Student ID already exists.")
        return
    markbook[studentID] = {"firstName": firstName, "lastName": lastName, "marks": []}
    print("Student added successfully.")

def is_valid_student_id(studentID): 
    return len(studentID) == 5 and studentID.isdigit()

def is_valid_filename(filename):
    for char in filename:
        if not char.isalnum() and char != ' ':
            return False
    return True

def add_marks():
    student_id = input("Enter student ID: ")
    if student_id not in markbook:
        print("Student ID not found.")
        return
    mark = input("Enter mark (0-100): ")
    if not mark.isdigit() or int(mark) < 0 or int(mark) > 100:
        print("Invalid mark. Please enter a value between 0 and 100.")
        return
    markbook[student_id]['marks'].append(int(mark))
    print("Mark added successfully.")
    calculate_grade(student_id)

def calculate_grade(student_id):
    marks = markbook[student_id]['marks']
    average_mark = sum(marks) / len(marks) if marks else 0

    match average_mark:
        case mark if 90 <= mark <= 100:
            grade = "A+"
        case mark if 80 <= mark < 90:
            grade = "A"
        case mark if 70 <= mark < 80:
            grade = "B"
        case mark if 60 <= mark < 70:
            grade = "C"
        case mark if 50 <= mark < 60:
            grade = "D"
        case mark if 0 <= mark < 50:
            grade = "F"
        case _:
            grade = "N/A"

    markbook[student_id]['grade'] = grade

def display_markbook():
    """Display all data stored in the markbook."""
    print("{:<10} {:<15} {:<15} {:<20} {:<5}".format('Student ID', 'First Name', 'Last Name', 'Marks', 'Grade'))
    print('-' * 65)

    for student_id, student_data in markbook.items():
        first_name = student_data['firstName']
        last_name = student_data['lastName']
        marks = ', '.join(str(mark) for mark in student_data['marks'])
        grade = student_data['grade']
        print("{:<10} {:<15} {:<15} {:<20} {:<5}".format(student_id, first_name, last_name, marks, grade))

def save_markbook():
    """Save the markbook to a file."""
    filename = input("Enter filename to save markbook: ")

    # Validate filename
    if not is_valid_filename(filename):
        print("Invalid filename. Please enter a valid filename.")
        return

    try:
        with open(f"{filename}.txt", 'w') as file:
            for student_id, student_data in markbook.items():
                file.write(f"{student_id},{student_data['firstName']},{student_data['lastName']},{','.join(str(mark) for mark in student_data['marks'])},{student_data['grade']}\n")
        print(f"Markbook saved successfully to {filename}.txt")
    except Exception as e:
        print(f"Error saving markbook: {e}")

def load_markbook():
    """Load the markbook from a file."""
    filename = input("Enter filename to load markbook: ")

    # Validate filename
    if not is_valid_filename(filename):
        print("Invalid filename. Please enter a valid filename.")
        return

    try:
        with open(f"{filename}.txt", 'r') as file:
            markbook.clear()
            for line in file:
                student_id, first_name, last_name, marks_str, grade = line.strip().split(',')
                marks = [int(mark) for mark in marks_str.split(',')]
                markbook[student_id] = {
                    'firstName': first_name,
                    'lastName': last_name,
                    'marks': marks,
                    'grade': grade
                }
        print(f"Markbook loaded successfully from {filename}.txt")
    except Exception as e:
        print(f"Error loading markbook: {e}")

def exit_program():
    """Exit the program."""
    print("Exiting program...")

def main():
    while True:
        print("\nMarkbook Menu:")
        print("1. Add a new student")
        print("2. Add marks for a student")
        print("3. Display markbook")
        print("4. Save markbook")
        print("5. Load markbook")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_marks()
        elif choice == '3':
            display_markbook()
        elif choice == '4':
            save_markbook()
        elif choice == '5':
            load_markbook()
        elif choice == '6':
            exit_program()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()