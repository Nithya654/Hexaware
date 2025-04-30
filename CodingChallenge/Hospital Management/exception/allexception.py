class PatientNumberNotFoundException(Exception):
    def __init__(self, message="Patient number not found in database."):
        super().__init__(message)

