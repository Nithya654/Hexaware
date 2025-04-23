import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from entity.models import Student, Course, Teacher, Payment
from dao.service_impl import (
    StudentServiceImpl,
    CourseServiceImpl,
    TeacherServiceImpl,
    EnrollmentServiceImpl,
    PaymentServiceImpl
)
from exception.allexception import *

def main():
    student_service = StudentServiceImpl()
    course_service = CourseServiceImpl()
    teacher_service = TeacherServiceImpl()
    enrollment_service = EnrollmentServiceImpl()
    payment_service = PaymentServiceImpl()

    while True:
        print("\n=== Student Information System Menu ===")
        print("1. Register a New Student")
        print("2. Enroll Student in a Course")
        print("3. Assign Teacher to Course")
        print("4. Make Payment")
        print("5. View All Students")
        print("6. View Enrollments by Course")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        try:
            if choice == '1':
                sid = int(input("Student ID: "))
                fname = input("First Name: ")
                lname = input("Last Name: ")
                dob = input("Date of Birth (YYYY-MM-DD): ")
                email = input("Email: ")
                phone = input("Phone: ")
                student = Student(sid, fname, lname, datetime.strptime(dob, '%Y-%m-%d').date(), email, phone)
                student_service.add_student(student)
                print("✅ Student added successfully.")

            elif choice == '2':
                sid = int(input("Student ID: "))
                cid = int(input("Course ID: "))
                enrollment_service.enroll_student(sid, cid)
                print("✅ Student enrolled in the course successfully.")

            elif choice == '3':
                tid = int(input("Teacher ID: "))
                fname = input("First Name: ")
                lname = input("Last Name: ")
                email = input("Email: ")
                teacher = Teacher(tid, fname, lname, email)
                teacher_service.add_teacher(teacher)
                print("✅ Teacher added successfully.")

                cid = int(input("Course ID to assign this teacher to: "))
                course_service.assign_teacher_to_course(cid, tid)
                print("✅ Teacher assigned to the course successfully.")

            elif choice == '4':
                sid = int(input("Student ID: "))
                amt = float(input("Amount: "))
                date_str = input("Payment Date (YYYY-MM-DD): ")
                student = Student(sid, "", "", datetime.today(), "", "")
                pid = int(input("Payment ID: "))
                payment = Payment(pid, student, amt, datetime.strptime(date_str, '%Y-%m-%d').date())
                payment_service.make_payment(payment)
                print("✅ Payment recorded successfully.")

            elif choice == '5':
                students = student_service.get_all_students()
                if not students:
                    print("❌ No students found.")
                for student in students:
                    student.display_student_info()

            elif choice == '6':
                cid = int(input("Enter Course ID: "))
                enrollments = enrollment_service.get_enrollments_by_course(cid)
                if not enrollments:
                    print(f"ℹNo enrollments found for Course ID {cid}.")
                else:
                    print(f" Enrollments for Course ID {cid}:")
                    for e in enrollments:
                        print(f"- Student ID: {e.student.student_id}, Enrollment Date: {e.enrollment_date}")

            elif choice == '7':
                print(" Exiting Student Information System...bye!")
                break

            else:
                print(" ❌Invalid choice. Please select a number from 1 to 7.")

        except DuplicateEnrollmentException as e:
            print(f"❌ {str(e)}")
        except (InvalidStudentDataException, InvalidTeacherDataException, InvalidCourseDataException,
                InvalidEnrollmentDataException, PaymentValidationException) as e:
            print(f"❌ Error: {str(e)}")
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")

if __name__ == '__main__':
    main()
