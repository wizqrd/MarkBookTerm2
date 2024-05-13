def add_new_student(markbook):
    student_id = input('Enter Student Id: ')
    if not student_id.isdigit() or len(student_id) != 5:
        print('Invalid Student ID')
        return 
    student_firstname = input("Enter the first name: ")
    student_lastname = input('Enter the last name: ')
    markbook[student_id] = {'first_name': student_firstname, 'last_name': student_lastname, 'marks': [], 'grade': 'N/A'}
'''Add new student'''

def add_marks(markbook):
    









































'''def add_marks(markbook):
    """
    Add marks for a student.
    """
    student_id = input("Enter student ID to add marks: ")
    if student_id not in markbook:
        print("Student ID not found.")
        return

    mark = input("Enter mark (0-100): ")
    if not mark.isdigit() or not (0 <= int(mark) <= 100):
        print("Invalid mark. Please enter a number between 0 and 100.")
        return

    markbook[student_id]['marks'].append(int(mark))

def calculate_overall_grade(markbook):
    """
    Calculate and store the overall grade of a student.
    """
    for student_id, data in markbook.items():
        marks = data['marks']
        if marks:
            average_mark = sum(marks) / len(marks)
            grade = ''
            match average_mark:
                case 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100:
                    grade = 'A'
                case 74 | 75 | 76 | 77 | 78 | 79 | 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89:
                    grade = 'B'
                case 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71 | 72 | 73:
                    grade = 'C'
                case 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59:
                    grade = 'D'
                case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49:
                    grade = 'F'
                case _:
                    grade = 'N/A'

            markbook[student_id]['overall_grade'] = grade
        else:
            markbook[student_id]['overall_grade'] = 'N/A'

def display_markbook(markbook):
    """
    Display all data stored in the markbook.
    """
    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format('Student ID', 'First Name', 'Last Name', 'Marks', 'Overall Grade'))
    for student_id, data in markbook.items():
        marks = ', '.join(map(str, data['marks']))  # Convert list of marks to a string
        print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(student_id, data['first_name'], data['last_name'], marks, data['overall_grade']))

def save_markbook(markbook):
    """
    Save the markbook to a file.
    """
    file_name = input("Enter the name of the file to save the markbook: ")
    try:
        with open(file_name, 'w') as file:
            for student_id, data in markbook.items():
                file.write(f"{student_id},{data['first_name']},{data['last_name']},{data['marks']},{data['overall_grade']}\n")
        print("Markbook saved successfully.")
    except OSError:
        print("Error: Unable to save the markbook.")

def load_markbook():
    """
    Load the markbook from a file.
    """
    file_name = input("Enter the name of the file to load the markbook: ")
    markbook = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                markbook[parts[0]] = {'first_name': parts[1], 'last_name': parts[2], 'marks': eval(parts[3]), 'overall_grade': parts[4]}
        print("Markbook loaded successfully.")
        return markbook
    except FileNotFoundError:
        print("Error: File not found.")
        return None

def main():
    markbook = {}
    while True:
        print("\n1. Add a new student\n2. Add marks for a student\n3. Calculate and store overall grade\n"
              "4. Display markbook\n5. Save markbook to a file\n6. Load markbook from a file\n7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_student(markbook)
        elif choice == '2':
            add_marks(markbook)
        elif choice == '3':
            calculate_overall_grade(markbook)
        elif choice == '4':
            display_markbook(markbook)
        elif choice == '5':
            save_markbook(markbook)
        elif choice == '6':
            markbook = load_markbook() or markbook
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()'''