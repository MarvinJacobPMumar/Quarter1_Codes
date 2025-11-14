# Define Variables
students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))
classTotal = 0
studentTotal = 0

#Main loop
for i in range(1, students + 1):
    print("Student", i)
    studentTotal = 0
    for j in range(1, subjects + 1):
        # Input scores for each subject
        x = int(input(f"Enter score {j}: "))
        studentTotal += x
        
    # Averaging
    average = studentTotal / subjects
    classTotal += average
    studentTotal = 0
    print("Average for Student", i, ":", average)

# Process class average
classAverage = classTotal / students
print("Class Average:", classAverage)

    
