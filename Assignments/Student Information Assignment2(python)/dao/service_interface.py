from abc import ABC, abstractmethod
from typing import List
from entity.models import Student, Course, Enrollment, Teacher, Payment


class StudentService(ABC):
    @abstractmethod
    def add_student(self, student: Student):
        pass

    @abstractmethod
    def get_all_students(self) -> List[Student]:
        pass


class CourseService(ABC):
    @abstractmethod
    def add_course(self, course: Course):
        pass

    @abstractmethod
    def assign_teacher_to_course(self, course_id: int, teacher_id: int):
        pass

    @abstractmethod
    def get_all_courses(self) -> List[Course]:
        pass


class TeacherService(ABC):
    @abstractmethod
    def add_teacher(self, teacher: Teacher):
        pass

    @abstractmethod
    def get_all_teachers(self) -> List[Teacher]:
        pass


class EnrollmentService(ABC):
    @abstractmethod
    def enroll_student(self, student_id: int, course_id: int):
        pass

    @abstractmethod
    def get_enrollments_by_course(self, course_id: int) -> List[Enrollment]:
        pass


class PaymentService(ABC):
    @abstractmethod
    def make_payment(self, payment: Payment):
        pass

    @abstractmethod
    def get_payments_by_student(self, student_id: int) -> List[Payment]:
        pass
