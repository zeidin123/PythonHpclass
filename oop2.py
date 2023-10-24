class Students:
    def __init__(self,name,course,gender,age):
        self.name=name
        self.course=course
        self.gender=gender
        self.age=age
    def display(self):
        print("Name: %s \nCourse: %s\nGender: %s\nAge: %d"
              %(self.name, self.course, self.gender, self.age))
myobj=Students("Zeinab Muhidin","BBIT","Female",21)
myobj.display()

stud1 = Students("Zeinab", "CS","FEMLE",21)
stud2 = Students("Aisha", "Software engineering","FEMALE",24)

stud1.display()
stud2.display()
