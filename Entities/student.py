from dataclasses import dataclass
from db_conn import DB_CONN


@dataclass
class Student:
    name: str
    email: str
    age: int


class StudentManager:
    def add_student(self, student: Student) -> None:
        cursor = DB_CONN.cursor()
        sql_statement = "INSERT INTO students (name, age, email) VALUES (?, ?, ?)"
        cursor.execute(sql_statement, (student.name, student.age, student.email))
        DB_CONN.commit()
        cursor.close()

    def ask_student_details(self) -> Student:
        print("Insert student's info")
        name = input("Name: ")
        age = int(input("Age: "))
        email = input("Email: ")
        student = Student(name=name, age=age, email=email)
        return student

    def view_records(self) -> None:
        students = self.get_students()
        print("Students: ")
        for student in students:
            print(f"Student Id: {student[0]} - Name: {student[1]}, age: {student[2]}, Email:{student[3]}")
        return None

    def get_students(self):
        cursor = DB_CONN.cursor()
        sql_statement = "SELECT * FROM students"
        cursor.execute(sql_statement)
        records = cursor.fetchall()
        DB_CONN.commit()
        cursor.close()
        return records

    def get_student_record(self, student_id):
        cursor = DB_CONN.cursor()
        sql_statement = "SELECT * FROM students WHERE id = ?"
        cursor.execute(sql_statement, (student_id,))
        student_data = cursor.fetchone()
        cursor.close()
        return student_data

    def update_record(self, student_data, new_name, new_email, new_age):
        if len(new_name.strip()) > 0:
            student_data = student_data[:1] + (new_name,) + student_data[2:]
        if len(new_email.strip()) > 0:
            student_data = student_data[:3] + (new_email,) + student_data[4:]
        if new_age is not None:
            student_data = student_data[:2] + (new_age,) + student_data[3:]

        cursor = DB_CONN.cursor()
        sql_statement = "UPDATE students SET name = ?, age = ?, email = ? WHERE id = ?"
        cursor.execute(sql_statement, (*student_data[1:], student_data[0]))
        DB_CONN.commit()
        cursor.close()

    def input_update(self):
        student_id = input("Enter the ID of the student to update: ")
        student_data = self.get_student_record(student_id)

        if student_data is not None:
            print(f"Current record: {student_data}")
            new_name = input("Enter new name (or leave blank to keep the current name): ")
            new_email = input("Enter new email (or leave blank to keep the current email): ")
            new_age_str = input("Enter new age (or leave blank to keep the current age): ")
            new_age = int(new_age_str) if new_age_str.strip() else None

            self.update_record(student_data, new_name, new_email, new_age)
            print(f"Record updated: {student_data}")
        else:
            print(f"No record found with ID {student_id}")

    
        