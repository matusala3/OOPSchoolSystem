from dataclasses import dataclass
from db_conn import DB_CONN

@dataclass
class Teacher:
    name: str
    email: str

class TeacherManager:
    def add_teacher(self, teacher: Teacher) -> None:
        cursor = DB_CONN.cursor()
        sql_statement = "INSERT INTO teachers (name, email) VALUES (?, ?)"
        cursor.execute(sql_statement, (teacher.name, teacher.email))
        DB_CONN.commit()
        cursor.close()
    
    def ask_teacher_details(self) -> Teacher:
        print("Insert teacher's info")
        name = input("Name: ")
        email = input("Email: ")
        teacher = Teacher(name=name, email=email)
        return teacher
    
    def view_records(self) -> None:
        teachers = self.get_teachers()
        print("Teachers: ")
        for teacher in teachers:
            print(f"Teacher Id: {teacher[0]} - Name: {teacher[1]}, Email: {teacher[2]}")
        return None
    
    def get_teachers(self):
        cursor = DB_CONN.cursor()
        sql_statement = "SELECT * FROM teachers"
        cursor.execute(sql_statement)
        records = cursor.fetchall()
        DB_CONN.commit()
        cursor.close()
        return records