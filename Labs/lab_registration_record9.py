# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 13-11-2020
# purpose: A solution to the word games lab exercise


class Student:
    """
    INSERT YOUR DOCSTRING INFORMATION HERE
    """

    def __init__(self, study_type, f_name, l_name):
        # YOUR CODE GOES HERE
        self.study_type = study_type
        self.f_name = f_name
        self.l_name = l_name


    # YOUR CODE GOES HERE



class RegistrationData:
    """
    INSERT YOUR DOCSTRING INFORMATION HERE
    """
    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        # YOUR CODE GOES HERE
        self.address = address,
        self.registration_fee = registration_fee,
        self.study_type = study_type,
        self.f_name = f_name,
        self.l_name = l_name,
        self.s_id = s_id

    # YOUR CODE GOES HERE
    def get_address(new_address):
        address = new_address

    def set_address(self):
        self.address = value

    def get_registration_fee(registration_fee):
        self.registration_fee = registration_fee

    def set_registration_fee(self):
        self.registration_fee = values

    def get_study_type(self):
        self.study_type





r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500,
                     Student.POSTGRADUATE, "Bianca", "Phelan")
r.display_student_data()
r.student_id_property="C12345"
r.display_student_data()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.student_object.courses = course

r.display_student_data()

# print(RegistrationData.__doc__)
