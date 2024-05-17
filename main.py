def add_student(markbook):
    while True:
        student_id = input("Enter student ID (5 digits): ")
        if len(student_id) == 5 and student_id.isdigit():
            if student_id not in markbook:
                break
            else:
                print("Student ID already exists. Please enter a unique ID.")
        else:
            print("Invalid student ID. Please enter a 5-digit numeric ID.")

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    markbook[student_id] = {"first_name": first_name, "last_name": last_name, "marks": []}

def add_marks(markbook):
    student_id = input("Enter student ID: ")
    if student_id in markbook:
        try:
            mark = float(input("Enter student's mark (0-100): "))
            if 0 <= mark <= 100:
                markbook[student_id]["marks"].append(mark)
            else:
                print("Invalid mark. Mark must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric mark.")
    else:
        print("Student not found.")

def calculate_grade(mark):
    if 90 <= mark <= 100:
        return "A"
    elif 74 <= mark <= 89:
        return "B"
    elif 60 <= mark <= 75:
        return "C"
    elif 50 <= mark <= 59:
        return "D"
    elif 0 <= mark <= 49:
        return "F"
    else:
        return "N/A"

def display_markbook(markbook):
    print("\nMarkbook:")
    print("{:<10} {:<15} {:<15} {:<10}".format("Student ID", "First Name", "Last Name", "Grade"))
    for student_id, student_data in markbook.items():
        first_name = student_data["first_name"]
        last_name = student_data["last_name"]
        marks = student_data["marks"]
        average_mark = sum(marks) / len(marks) if marks else 0
        grade = calculate_grade(average_mark)
        print("{:<10} {:<15} {:<15} {:<10}".format(student_id, first_name, last_name, grade))

def save_markbook(markbook):
    filename = input("Enter a filename to save the markbook: ")
    with open(filename, "w") as file:
        for student_id, student_data in markbook.items():
            first_name = student_data["first_name"]
            last_name = student_data["last_name"]
            marks = student_data["marks"]
            file.write(f"{student_id},{first_name},{last_name},{','.join(map(str, marks))}\n")

def load_markbook():
    filename = input("Enter the filename to load the markbook: ")
    markbook = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                student_id, first_name, last_name, *marks = line.strip().split(",")
                markbook[student_id] = {"first_name": first_name, "last_name": last_name, "marks": [float(mark) for mark in marks]}
        return markbook
    except FileNotFoundError:
        print("File not found. Creating a new markbook.")
        return {}

def main():
    markbook = {}
    while True:
        print("\nMenu:")
        print("1. Add a new student")
        print("2. Add marks for a student")
        print("3. Display markbook")
        print("4. Save markbook to a file")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(markbook)
        elif choice == "2":
            add_marks(markbook)
        elif choice == "3":
            display_markbook(markbook)
        elif choice == "4":
            save_markbook(markbook)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
