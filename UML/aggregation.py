from typing import List

# Student class (can exist independently)
class Student:
    def __init__(self,name:str,roll_no:int)->None:
        self.__name=name
        self.__roll_no=roll_no
    def get_name(self)->str:
        return self.__name
    def get_roll_no(self)->int:
        return self.__roll_no

# Department class (contains students - Aggregation)
class Department:
    def __init__(self,dept_name:str)->None:
        self.__dept_name:str=dept_name
        self.__students:List[Student]=[]
    def add_students(self,student:Student)->None:
        self.__students.append(student)
    def show_students(self)->None:
        print(f"\nStudents in {self.__dept_name} Department:")
        for student in self.__students:
            print(f"Name: {student.get_name()}, Roll No: {student.get_roll_no()}")

## Craeting Student objects
student1:Student=Student("Rahul",101)
student2:Student=Student("Priya",102)
student3:Student=Student("Amit",103)

# creating department object
cs_department: Department=Department("Computer Science")

# Adding students to department (Aggregation happening here!)
cs_department.add_students(student1)
cs_department.add_students(student2)
cs_department.add_students(student3)

# Displaying students in the department
cs_department.show_students()


# Display students
cs_department.show_students()

# IMPORTANT: Even if we delete the department, students still exist!
del cs_department  # Department deleted

# Students are still alive and can be used
print(f"\nStudent still exists: {student1.get_name()}")
# Output: Student still exists: Rahul