class Patient:
    def __init__(self, patient_id=None, first_name="", last_name="", dob="", gender="", contact="", address=""):
        self.__patient_id = patient_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__gender = gender
        self.__contact = contact
        self.__address = address

    def __str__(self):
        return f"{self.__patient_id}, {self.__first_name} {self.__last_name}, DOB: {self.__dob}, Gender: {self.__gender}, Contact: {self.__contact}, Address: {self.__address}"

    
class Doctor:
    def __init__(self, doctor_id=None, first_name="", last_name="", specialization="", contact=""):
        self.__doctor_id = doctor_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__specialization = specialization
        self.__contact = contact

    def __str__(self):
        return f"{self.__doctor_id}, {self.__first_name} {self.__last_name}, Specialization: {self.__specialization}, Contact: {self.__contact}"

class Appointment:
    def __init__(self, appointment_id=None, patient_id=None, doctor_id=None, appointment_date="", description=""):
        self.__appointment_id = appointment_id
        self.__patient_id = patient_id
        self.__doctor_id = doctor_id
        self.__appointment_date = appointment_date
        self.__description = description

    def __str__(self):
        return f"Appointment {self.__appointment_id}: Patient {self.__patient_id}, Doctor {self.__doctor_id}, Date: {self.__appointment_date}, Description: {self.__description}"



