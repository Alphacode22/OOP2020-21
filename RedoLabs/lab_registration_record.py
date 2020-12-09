# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 13-11-2020
# purpose: A solution to the word games lab exercise


class Student:
    """
    INSERT YOUR DOCSTRING INFORMATION HERE
    """

    #STUDY_TYPE =  ("POSTGRADUATE", "UNDERGRADUATE")
    UNDERGRADUATE, POSTGRADUATE = range(2) #?????

    def __init__(self, study_type, f_name, l_name):
        # YOUR CODE GOES HERE
        self.__study_type = study_type
        self.__f_name = f_name
        self.__l_name = l_name
        self.__courses = []

    # YOUR CODE GOES HERE
    @property
    def study_type(self):
        return self.__study_type

    @study_type.setter
    def study_type(self, value):
        self.__study_type = value

    @property
    def full_name(self):
        return self.__f_name, self.__l_name

    @full_name.setter
    def full_name(self, value):
        if type(value) != list:
            print("AHHHHHHHHHHHHHHHHH")

        self.__f_name = value[0]
        self.__l_name = value[1]

    # def name(self):
    #     return {}{}.self

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        if type(value) != str:
            print("AHHH")

        self.__courses.append(value)


    def __str__(self): #dk
        return f"{self.full_name} {self.study_type} {self.courses}"

    def get_all_student_data(self): # dk
        return self.full_name, self.study_type, self.courses




class RegistrationData:
    """
    INSERT YOUR DOCSTRING INFORMATION HERE
    """
    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        self.__address = address
        self.__registration_fee = registration_fee
        self.__s_id = s_id
        try:
            self.__student_object = Student(study_type, f_name, l_name)
        except Exception as e:
            pass


    # YOUR CODE GOES HERE
    @property
    def student_object(self):
        return self.student_object


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def registration_fee(self):
        return self.__registration_fee

    # ..............


    def display_student_data(self): # dk
        print(self.student_object)








r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500,
                     Student.POSTGRADUATE, "Bianca", "Phelan")
r.display_student_data()
r.student_id_property="C12345"
r.display_student_data()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.student_object.courses = course

r.display_student_data()

# print(RegistrationData.__doc__)

#display
# mix other datatype