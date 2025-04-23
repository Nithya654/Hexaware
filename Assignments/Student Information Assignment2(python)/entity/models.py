from datetime import date
from typing import List, Optional


class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str, dob: date, email: str, phone: str):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = dob
        self.email = email
        self.phone = phone
        self.enrollments: List[Enrollment] = []
        self.payments: List[Payment] = []

    def enroll_in_course(self, course):
        for enrollment in self.enrollments:
            if enrollment.course.course_id == course.course_id:
                raise Exception("DuplicateEnrollmentException: Already enrolled in this course.")
        enrollment = Enrollment(len(self.enrollments) + 1, self, course, date.today())
        self.enrollments.append(enrollment)
        course.enrollments.append(enrollment)

    def update_student_info(self, first_name, last_name, dob, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = dob
        self.email = email
        self.phone = phone

    def make_payment(self, amount, payment_date):
        payment = Payment(len(self.payments) + 1, self, amount, payment_date)
        self.payments.append(payment)

    def display_student_info(self):
        print(f"Student ID: {self.student_id}, Name: {self.first_name} {self.last_name}, DOB: {self.date_of_birth}, Email: {self.email}, Phone: {self.phone}")

    def get_enrolled_courses(self):
        return [enrollment.course for enrollment in self.enrollments]

    def get_payment_history(self):
        return self.payments


class Course:
    def __init__(self, course_id: int, course_name: str, course_code: str, instructor_name: Optional[str] = None):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.teacher = None
        self.enrollments = []

    def assign_teacher(self, teacher):
        self.teacher = teacher
        self.instructor_name = f"{teacher.first_name} {teacher.last_name}"
        teacher.assigned_courses.append(self)

    def update_course_info(self, course_code, course_name, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor_name = instructor

    def display_course_info(self):
        print(f"Course ID: {self.course_id}, Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor_name}")

    def get_enrollments(self):
        return self.enrollments

    def get_teacher(self):
        return self.teacher


class Enrollment:
    def __init__(self, enrollment_id: int, student: Student, course: Course, enrollment_date: date):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date

    def get_student(self):
        return self.student

    def get_course(self):
        return self.course


class Teacher:
    def __init__(self, teacher_id: int, first_name: str, last_name: str, email: str):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.assigned_courses: List[Course] = []

    def update_teacher_info(self, name: str, email: str, expertise: str):
        parts = name.split(" ", 1)
        self.first_name = parts[0]
        self.last_name = parts[1] if len(parts) > 1 else ""
        self.email = email
        self.expertise = expertise

    def display_teacher_info(self):
        print(f"Teacher ID: {self.teacher_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}")

    def get_assigned_courses(self):
        return self.assigned_courses


class Payment:
    def __init__(self, payment_id: int, student: Student, amount: float, payment_date: date):
        self.payment_id = payment_id
        self.student = student
        self.amount = amount
        self.payment_date = payment_date

    def get_student(self):
        return self.student

    def get_payment_amount(self):
        return self.amount

    def get_payment_date(self):
        return self.payment_date
