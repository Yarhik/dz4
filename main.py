class Student:
    def __init__(self, name, age, student_id, wtw, GPA):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.wtw = wtw
        self.GPA = GPA

    def new_name(self, new_name):
        self.name = new_name

    def new_age(self, new_age):
        self.age = new_age

    def new_student_id(self, new_id):
        self.student_id = new_id

    def new_major(self, new_wtw):
        self.wtw = new_wtw


    def new_GPA(self, new_GPA):
        self.GPA = new_GPA


    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"wtw: {self.wtw}")
        print(f"GPA: {self.GPA}")


student1 = Student("John Doe", 20, "S228228", "IT", 3.7)
student2 = Student("Jane Smith", 22, "S69693", "Engineer", 3.9)
 


student1.new_name("John Smith")
student1.new_age(21)





student1.display_student_info()
student2.display_student_info()
