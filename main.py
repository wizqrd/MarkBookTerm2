markbook_DB = {}

def add_marks():
    student_id = input("Enter a unique 5 digit student ID: ")
    while not verify_student_id(student_id):
        student_id = input("Please enter a valid ID: ")
    while True:
        score = input("PLease enter score(or press enter to finish): ")
        if score == "":
            break
        try:
            score = int(score)
            if 0 <= score <= 100:
                grade = calculate_score(score)
                modify_data_in_file("student.txt", student_id, grade)
                print(f'mark added as {grade}')
            else:
                print("Please enter a valid score between 0 and 100")
        except ValueError:
            print("Invalid input, please enter an integer")


def verify_student_id(student_id):
    try:
        with open("student.txt", "r") as file:
            for line in file:
                stored_id,_ = line.strip().split(',' , 1)
                if stored_id == student_id:
                    return True
        return False
    except FileNotFoundError:
        print("The student_id does not exist.")
    return False
        
def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score <= 59:
        return 'F'
    else:
        return 'Invalid score'

def display_markbook():
    if not markbook_DB:
        print("Markbook is empty, PLease try again.")    
        return

    for student_id, marks in markbook_DB.items():
        print(f"Student ID: {student_id}")
        for mark in marks:
            print(f" Mark: {mark}")
        print(" | " * 20) 
    
    
"""f = open('marbook.txt', 'r')
read("markbook.txt")
file_contents = f.read("markbook.txt")
print (file_contents)
f.close()"""
  

    
                
            
    


def load_file(markbook_DB, file_path):
        try:
            with open(file_path, 'r') as f:
                pass
        except Exception as e:
            print(f'Open File Error: {e}')
            return markbook_DB

        with open(file_path, 'r') as input_file:
            data = {}
            for i in input_file.read().split():
                if i == 'WOMP':
                    break
                data[i.split("|")[0]] = [i.split("|")[1], i.split("|")[2], i.split("|")[3]]
            return data



def add_student():
    add_id_done = False
    print("Add a student")
    print("Must be 5 numbers long and only contain integers")    
    id = input("Enter Student ID: ")
    while not verify_new_id(id):
        id = input("Invalid ID. Enter Student ID: ")
    if verify_new_id(id):  
        add_id_done = True
        print(f'ID {id} is a success!')
    if add_id_done:
        student_name_done = False
        while not student_name_done:
            first_name = input("Enter the First Name of student: ")
            last_name = input("Enter the Last Name of student: ")
            if first_name.isalpha() and last_name.isalpha():  
                student_information = f"{id}|{first_name}|{last_name}|N/A"
                with open('students.txt', 'r') as f:
                    lines = f.readlines()

                with open('students.txt', 'w') as f:
                    for line in lines:
                        if "WOMP" in line:
                            line = line.replace("WOMP", f"{student_information}\nWOMP")
                        f.write(line)

                print(f'Student {first_name} {last_name} has been added, with the ID: {id}')
                student_name_done = True
            else:
                print("Names must contain only alphabetic characters. Please try again.")

def verify_new_id(student_id):
    try:
        with open("students.txt", "r") as file:
            for line in file:
                stored_id, _ = line.strip().split(',', 1)
                if stored_id == student_id:
                    return False
        return True
    except FileNotFoundError:
        return True

def modify_data_in_file(file_path, student_id, new_data):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            for line in lines:
                if line.startswith(student_id + ','):
                    parts = line.strip().split('|')
                    if len(parts) == 4:  # Ensure the line has the correct format
                        parts[3] = new_data  # Replace the grade data
                        line = '|'.join(parts) + '\n'
                file.write(line)
        print(f'Data for student ID {student_id} has been updated.')
    except FileNotFoundError:
        print(f'The file {file_path} does not exist.')
    except Exception as e:
        print(f'An error occurred: {e}')

def save_markbook(markbook_DB):
    
    

    
def markbook_menu():
    print("""1. Add a student. 2. Add marks for student. 3. Display markbook. 
    4. Save markbook to file. 5. Load markbook from file. 6. Exit""")
    person_choice = input('Enter your choice: ')
match person_choice:
    case "1":
        add_student()
    case "2":
        add_marks()
    case "3":
        display_markbook()
    case "4":
        save_markbook()
    case "5":
        load_markbook()
    case "6":
        print("Exiting...")
        
    
    