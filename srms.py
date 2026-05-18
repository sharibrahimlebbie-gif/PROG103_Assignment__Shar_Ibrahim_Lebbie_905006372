# STUDENT RECORD MANAGEMENT SYSTEM (SRMS)
# PROG103 STRUCTURED PROGRAMMING ASSIGNMENT

students = []


def add_student():

    print("\n========== ADD STUDENT RECORD ==========")

    name = input("Enter Student Name: ").strip()
    student_id = input("Enter Student ID: ").strip()
    department = input("Enter Department: ").strip()

    scores = []

    for i in range(3):

        while True:

            try:
                score = float(input(f"Enter Score for Subject {i+1}: "))

                if 0 <= score <= 100:
                    scores.append(score)
                    break

                else:
                    print("Score must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter numbers only.")

    total = sum(scores)
    average = total / len(scores)

    if average >= 70:
        grade = "A"
        status = "Excellent"

    elif average >= 60:
        grade = "B"
        status = "Very Good"

    elif average >= 50:
        grade = "C"
        status = "Good"

    elif average >= 40:
        grade = "D"
        status = "Pass"

    else:
        grade = "F"
        status = "Fail"

    student = {
        "name": name,
        "student_id": student_id,
        "department": department,
        "scores": scores,
        "total": total,
        "average": average,
        "grade": grade,
        "status": status
    }

    students.append(student)

    print("\nStudent Record Added Successfully!")


def view_students():

    print("\n========== STUDENT RECORDS ==========")

    if len(students) == 0:
        print("No student records found.")
        return

    for index, student in enumerate(students, start=1):

        print("\n--------------------------------------")
        print(f"Record Number : {index}")
        print(f"Name          : {student['name']}")
        print(f"Student ID    : {student['student_id']}")
        print(f"Department    : {student['department']}")
        print(f"Scores        : {student['scores']}")
        print(f"Total Score   : {student['total']}")
        print(f"Average       : {student['average']:.2f}")
        print(f"Grade         : {student['grade']}")
        print(f"Status        : {student['status']}")
        print("--------------------------------------")


def search_student():

    print("\n========== SEARCH STUDENT ==========")

    keyword = input("Enter Student ID: ").strip()

    found = False

    for student in students:

        if student['student_id'] == keyword:

            print("\nStudent Found")
            print("--------------------------------------")
            print(f"Name        : {student['name']}")
            print(f"Department  : {student['department']}")
            print(f"Scores      : {student['scores']}")
            print(f"Average     : {student['average']:.2f}")
            print(f"Grade       : {student['grade']}")
            print(f"Status      : {student['status']}")
            print("--------------------------------------")

            found = True

    if not found:
        print("Student record not found.")


def update_student():

    print("\n========== UPDATE STUDENT ==========")

    student_id = input("Enter Student ID to Update: ").strip()

    for student in students:

        if student['student_id'] == student_id:

            print("\nStudent Record Found")

            new_department = input("Enter New Department: ").strip()

            new_scores = []

            for i in range(3):

                while True:

                    try:
                        score = float(input(f"Enter New Score {i+1}: "))

                        if 0 <= score <= 100:
                            new_scores.append(score)
                            break

                        else:
                            print("Score must be between 0 and 100.")

                    except ValueError:
                        print("Invalid input.")

            total = sum(new_scores)
            average = total / len(new_scores)

            if average >= 70:
                grade = "A"
                status = "Excellent"

            elif average >= 60:
                grade = "B"
                status = "Very Good"

            elif average >= 50:
                grade = "C"
                status = "Good"

            elif average >= 40:
                grade = "D"
                status = "Pass"

            else:
                grade = "F"
                status = "Fail"

            student['department'] = new_department
            student['scores'] = new_scores
            student['total'] = total
            student['average'] = average
            student['grade'] = grade
            student['status'] = status

            print("\nStudent Record Updated Successfully!")
            return

    print("Student record not found.")


def delete_student():

    print("\n========== DELETE STUDENT ==========")

    student_id = input("Enter Student ID to Delete: ").strip()

    for student in students:

        if student['student_id'] == student_id:

            students.remove(student)

            print("\nStudent Record Deleted Successfully!")
            return

    print("Student record not found.")


def performance_summary():

    print("\n========== PERFORMANCE SUMMARY ==========")

    if len(students) == 0:
        print("No records available.")
        return

    total_students = len(students)

    passed = 0
    failed = 0

    for student in students:

        if student['status'] == "Fail":
            failed += 1

        else:
            passed += 1

    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")


def main():

    while True:

        print("\n================================================")
        print("    STUDENT RECORD MANAGEMENT SYSTEM (SRMS)")
        print("================================================")
        print("1. Add Student Record")
        print("2. View Student Records")
        print("3. Search Student")
        print("4. Update Student Record")
        print("5. Delete Student Record")
        print("6. Performance Summary")
        print("7. Exit System")
        print("================================================")

        choice = input("Enter Your Choice: ")

        if choice == '1':
            add_student()

        elif choice == '2':
            view_students()

        elif choice == '3':
            search_student()

        elif choice == '4':
            update_student()

        elif choice == '5':
            delete_student()

        elif choice == '6':
            performance_summary()

        elif choice == '7':

            print("\n========== FINAL SUMMARY ==========")

            total_students = len(students)

            passed = 0
            failed = 0

            for student in students:

                if student['status'] == "Fail":
                    failed += 1

                else:
                    passed += 1

            print(f"Total Students : {total_students}")
            print(f"Passed         : {passed}")
            print(f"Failed         : {failed}")

            print("\nSystem Closed Successfully.")
            print("Thank you for using SRMS.")
            break

        else:
            print("Invalid choice. Please try again.")


main()