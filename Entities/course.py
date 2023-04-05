from dataclasses import dataclass
from db_conn import DB_CONN

@dataclass
class Course:
    name: str
    teacher_id: int

class CourseManager:
    def add_course(self, course: Course) -> None:
        cursor = DB_CONN.cursor()
        sql_statement = "INSERT INTO courses (name, teacher_id) VALUES (?, ?)"
        cursor.execute(sql_statement, (course.name, course.teacher_id))
        DB_CONN.commit()
        cursor.close()

    def ask_course_details(self) -> Course:
        print("Insert course's info")
        name = input("Name: ")
        teacher_id = int(input("Teacher Id: "))
        course = Course(name=name, teacher_id=teacher_id)
        return course
    
    def view_records(self) -> None:
        courses = self.get_courses()
        print("Courses: ")
        for course in courses:
            print(f"Course Id: {course[0]} - Name: {course[1]}, Teacher Id: {course[2]}")
        return None
    
    def get_courses(self):
        cursor = DB_CONN.cursor()
        sql_statement = "SELECT * FROM courses"
        cursor.execute(sql_statement)
        records = cursor.fetchall()
        DB_CONN.commit()
        cursor.close()
        return records