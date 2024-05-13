This is a Marking/Grading software
Task Description:
--You are required to create a markbook program using Python3.
---Requirements:
----The program should have a menu-driven interface with the following 
     subroutines:
      • Add a new student (3 marks)
        o Need to enter a first name, last name and student ID
      o Student ID is a unique 5 digit numeric string e.g. ‘50043’
    • Add marks for a student (1 mark)
    o Mark has to be between 0-100 (inclusive)
      • Calculate and stores the overall grade of a student automatically (3           marks)
        o Use a switch statement (in Python3 look up ‘Match Case’)
          o Mark cut-offs are:
        ▪ Between 90 to 100 (inclusive) is A
      ▪ Between 74 to 89 (inclusive) is B
    ▪ Between 60 to 75 (inclusive) is C
    ▪ Between 50 to 59 (inclusive) is D
  ▪ Between 0 to 49 (inclusive) is F
▪ Otherwise store “N/A”
  • Display all the data stored in the markbook in a formatted CLI output (3         marks)
    o Include column names
      • Save the markbook to a file (2 marks)
        o Give the user a prompt to name the output file i.e. ‘Maths Markbook’,
      ‘English Markbook’
    • Load the markbook from a file (2 marks)
  o Allow user to specify which file to load i.e. ‘Maths Markbook’
• Exit the program (1 mark)


➢ Each dot point above must be its own self-contained subroutine
➢ Your code must have code comments to explain every subroutine
➢ Your code must loop until prompted to exit
➢ Student data must be stored using a dictionary
➢ Implement error handling for input validation
o Check valid studentID
o Check if missing first name or last name
o Check if marks are in the correct range
o Check if markbook name is valid when saving
o Check if markbook name is valid when loading