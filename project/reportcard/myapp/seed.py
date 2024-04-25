from faker import Faker
fake = Faker()
import random
from .models import *

def seed_marks():
    student_object = Student.objects.all()
    for std in student_object:
        subject_object = Subject.objects.all()
        for sub in subject_object:
            SubjectMarks.objects.create(student=std,subject=sub,marks=random.randint(0,100))

def seed_data(n=50):
    for i in range(n):
        dept_object = Department.objects.all()
        index_range = random.randint(0,len(dept_object)-1)

        dept = dept_object[index_range]
        name = fake.name()
        email = fake.email()
        age = random.randint(20,40)

        std_obj =  StudentId.objects.create(student_id = f"STD_{random.randint (100,999)}")

        Student.objects.create(department=dept,studentid=std_obj,name=name,email=email,age=age)
