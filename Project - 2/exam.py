print("Welcome to the Student Data Organizer!")

students = [
    {"ID":1 , "Name":"Alice", "Age":20, "Grade":"B+", "Date of Birth":2002-5-14, "Subjects":"Maths, Science, English"},
    {"ID":2 , "Name":"Dexter", "Age":20, "Grade":"B", "Date of Birth":2002-9-30, "Subjects":"Maths, History, English"}
]

print("Select an option:")

while True:
    print("1. Add Student")
    print("2. Display all students")
    print("3. Update Student information")
    print("4. Delete student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice from the above options :"))

    if choice == 1:
            student_id= int(input("Enter student id to add :"))
            name=input("Enter student name :")
            age=int(input("Enter student age :"))
            grade=input("Enter Grade :")
            dob=input("Enter student's DOB (YYYY-MM-DD) :")
            sub=input("Enter subjects :")

            new_student = {
                "ID":student_id,
                "Name":name,
                "Age":age,
                "Grade":grade,
                "Date of Birth":dob,
                "Subjects":sub
            }

            students.append(new_student)
            print("Student added successfully!")
            print("Students List after Adding :", students)

    elif choice == 2:
        for student in students:
            print("ID :",student["ID"] ,"Name :",student["Name"],"Age :",student["Age"],"Grade :",student["Grade"],"Date of Birth :",student["Date of Birth"],"Subjects :",student["Subjects"],sep=" | ")

    elif choice == 3:
        student_id= int(input("Enter student ID :"))
        found = False

        for student in students:
            if student["ID"]== student_id:
                student["Age"]==int(input("Enter new age :"))
                student["Subjects"]==input("Enter new subjects :")
                found = True
                print("List Updated successfully!")
                break

        print("Updated Student List :",students)
        
        if found == False:
            print("Student with this id not exists.")

    
    elif choice ==  4:
        student_id=int(input("Enter student id to remove :"))
        found=False

        for student in students:
            if student["ID"]==student_id:
                students.remove(student)
                found=True
                print("Student removed successfully!")
                break

        print("Student List after Removing :",students)

        if found==False:
            print("Student with this id not exists.")

    elif choice == 5:
        new_subjects={"Maths", "Science", "English", "Maths", "History", "English", "Economics", "Management", "Computer"}
        print("These are the subjects you can select :",new_subjects)

    elif choice == 6:
        print("Thank you for using the programme!")
        break

    else:
        print("Invalid choice ! Please enter a number from 1 to 8.")
        


