#object oriented programm that creates a menu for a school system
# what am i missing here? i am getting an error that says: AttributeError: type object 'StudentManager' has no attribute '_Menu__add_student'
from db_conn import DB_CONN
from Entities.student import StudentManager
from Entities.course import CourseManager
from Entities.teacher import TeacherManager
from Entities.enrollment import EnrollmentManager


class Menu:
    def __init__(self) -> None:
        return None
    
    def askChoice(self) -> str:
        print("1. Add new student")
        print("2. View student records")
        print("3. Update student records")
        print("4. Add new course")
        print("5. View course list")
        print("6. Enroll student in a course")
        print("7. View student's enrolled courses")
        print("8. add new teacher")
        print("9. view teacher's records")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        return choice
    
    def start(self) -> None:
        exitCondition = None
        while exitCondition != '0':
            choice = self.askChoice()
            if choice == '1':
                StudentManager().add_student(StudentManager().ask_student_details())
            elif choice == '2':
                StudentManager().view_records()
            elif choice == '3':
                StudentManager().input_update()
            elif choice == '4':
                CourseManager().add_course(CourseManager().ask_course_details())
            elif choice == '5':
                CourseManager().view_records()
            elif choice == '6':
                EnrollmentManager().enroll_student(EnrollmentManager().ask_enrollment_details())
            elif choice == '7':
                EnrollmentManager().view_records()
            elif choice == '8':
                TeacherManager().add_teacher(TeacherManager().ask_teacher_details())
            elif choice == '9':
                TeacherManager().view_records()
            elif choice == '0':
                break
            else:
                print("Unkown option")
            print("")
        return None







