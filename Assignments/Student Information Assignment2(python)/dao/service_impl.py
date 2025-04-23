import pyodbc
from datetime import date
from typing import List
from entity.models import Student, Course, Teacher, Enrollment, Payment
from exception.allexception import *
from util.db_conn_util import DBConnUtil


class StudentServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def add_student(self, student: Student):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
    "INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)",
    student.student_id,
    student.first_name,
    student.last_name,
    student.date_of_birth.strftime('%Y-%m-%d'),  
    student.email,
    student.phone
)

            self.conn.commit()
        except Exception as e:
            raise InvalidStudentDataException(str(e))

    def get_all_students(self) -> List[Student]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        return [Student(*row) for row in rows]


class CourseServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def add_course(self, course: Course):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO courses VALUES (?, ?, ?, ?)",
                course.course_id, course.course_name, course.course_code, None
            )
            self.conn.commit()
        except Exception as e:
            raise InvalidCourseDataException(str(e))

    def assign_teacher_to_course(self, course_id: int, teacher_id: int):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE courses SET teacher_id = ? WHERE course_id = ?", teacher_id, course_id)
        if cursor.rowcount == 0:
            raise CourseNotFoundException()
        self.conn.commit()

    def get_all_courses(self) -> List[Course]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT course_id, course_name, course_code, teacher_id FROM courses")
        rows = cursor.fetchall()
        return [Course(row[0], row[1], row[2], str(row[3]) if row[3] else None) for row in rows]


class TeacherServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def add_teacher(self, teacher: Teacher):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO teacher VALUES (?, ?, ?, ?)",
                teacher.teacher_id, teacher.first_name, teacher.last_name, teacher.email
            )
            self.conn.commit()
        except Exception as e:
            raise InvalidTeacherDataException(str(e))

    def get_all_teachers(self) -> List[Teacher]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM teacher")
        rows = cursor.fetchall()
        return [Teacher(*row) for row in rows]


class EnrollmentServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def enroll_student(self, student_id: int, course_id: int):
        cursor = self.conn.cursor()
        # Check for duplicate
        cursor.execute("SELECT * FROM enrollments WHERE student_id = ? AND course_id = ?", student_id, course_id)
        if cursor.fetchone():
            raise DuplicateEnrollmentException()

        # Get next enrollment_id
        cursor.execute("SELECT ISNULL(MAX(enrollment_id), 0) + 1 FROM enrollments")
        next_id = cursor.fetchone()[0]

        cursor.execute(
    "INSERT INTO enrollments VALUES (?, ?, ?, ?)",
    next_id, student_id, course_id, date.today().strftime('%Y-%m-%d')  # ✅ Convert date to string
)

        self.conn.commit()

    def get_enrollments_by_course(self, course_id: int) -> List[Enrollment]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM enrollments WHERE course_id = ?", course_id)
        rows = cursor.fetchall()
        enrollments = []
        for row in rows:
            student = Student(row[1], "", "", date.today(), "", "")  # minimal for now
            course = Course(row[2], "", "", "")  # minimal
            enrollments.append(Enrollment(row[0], student, course, row[3]))
        return enrollments


class PaymentServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def make_payment(self, payment: Payment):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO payments VALUES (?, ?, ?, ?)",
                payment.payment_id, 
                payment.student.student_id,
                payment.amount, 
                payment.payment_date.strftime('%Y-%m-%d') 
            )
            self.conn.commit()
        except Exception as e:
            raise PaymentValidationException(str(e))

    def get_payments_by_student(self, student_id: int) -> List[Payment]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM payments WHERE student_id = ?", student_id)
        rows = cursor.fetchall()
        payments = []
        for row in rows:
            student = Student(row[1], "", "", date.today(), "", "")
            payments.append(Payment(row[0], student, row[2], row[3]))
        return payments
