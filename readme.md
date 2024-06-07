# Task Description

You are required to create a markbook program using Python3.

## Requirements

The program should have a menu-driven interface with the following subroutines:

### Add a new student (3 marks)
- Need to enter a first name, last name, and student ID
- Student ID is a unique 5-digit numeric string e.g. ‘50043’

### Add marks for a student (1 mark)
- Mark has to be between 0-100 (inclusive)

### Calculate and store the overall grade of a student automatically (3 marks)
- Use a switch statement (in Python3 look up ‘Match Case’)
- Mark cut-offs are:
  - Between 90 to 100 (inclusive) is A
  - Between 74 to 89 (inclusive) is B
  - Between 60 to 75 (inclusive) is C
  - Between 50 to 59 (inclusive) is D
  - Between 0 to 49 (inclusive) is F
  - Otherwise store “N/A”

### Display all the data stored in the markbook in a formatted CLI output (3 marks)
- Include column names

### Save the markbook to a file (2 marks)
- Give the user a prompt to name the output file, e.g., ‘Maths Markbook’, ‘English Markbook’

### Load the markbook from a file (2 marks)
- Allow user to specify which file to load, e.g., ‘Maths Markbook’

### Exit the program (1 mark)

## Additional Requirements
- Each dot point above must be its own self-contained subroutine
- Your code must have comments to explain every subroutine
- Your code must loop until prompted to exit
- Student data must be stored using a dictionary
- Implement error handling for input validation:
  - Check valid student ID
  - Check if missing first name or last name
  - Check if marks are in the correct range
  - Check if markbook name is valid when saving
  - Check if markbook name is valid when loading
