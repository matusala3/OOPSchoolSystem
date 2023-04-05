from dataclasses import dataclass
from db_conn import DB_CONN

@dataclass
class Enrollment:
    student_id: int
    course_id: int

class EnrollmentManager:
    def enroll_student(self, enrollment: Enrollment) -> None:
        cursor = DB_CONN.cursor()
        sql_statement = "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)"
        cursor.execute(sql_statement, (enrollment.student_id, enrollment.course_id))
        DB_CONN.commit()
        cursor.close()

    def ask_enrollment_details(self) -> Enrollment:
        print("Insert enrollment's info")
        student_id = int(input("Student Id: "))
        course_id = int(input("Course Id: "))
        enrollment = Enrollment(student_id=student_id, course_id=course_id)
        return enrollment
    
    def view_records(self) -> None:
        enrollments = self.get_enrollments()
        print("Enrollments: ")
        for enrollment in enrollments:
            print(f"Student Id: {enrollment[0]} - Course Id: {enrollment[1]}")
        return None
    
    def get_enrollments(self):
        cursor = DB_CONN.cursor()
        sql_statement = "SELECT * FROM enrollments"
        cursor.execute(sql_statement)
        records = cursor.fetchall()
        DB_CONN.commit()
        cursor.close()
        return records