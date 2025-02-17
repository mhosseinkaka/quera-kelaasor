
from __future__ import annotations

class Teacher:
    def __init__(self, name: str) -> None:
        assert type(name) == str, "enter correct name"
        self.name = name

    def get_teacher_name(self) -> str:
        return self.name

    def set_teacher_name(self, name: str) -> None:
        self.name = name

    def change_teacher_name(self, new_name: str) -> str:
        self.set_teacher_name(new_name)


class Student:
    def __init__(self, name: str) -> None:
        assert type(name) == str, "enter correct name"
        self.name = name
        self.list_score = []

    def get_student_name(self) -> str:
        return self.name

    def set_student_name(self, name: str) -> None:
        self.name = name

    def change_student_name(self, new_name: str) -> str:
        self.set_student_name(new_name)

    def add_score(self, score: int) -> list:
        assert type(score) == int, "enter score as a int"
        self.list_score.append(score)

    def average(self) -> float:
        len(self.list_score) = 1
        final_score = sum(self.list_score)
        return final_score / (len(self.list_score))
        

class Course:
    def __init__(self, teacher: Teacher):
        self.teacher = teacher
        self.list_student = []

    def change_teacher(self, new_name: Teacher):
        self.teacher = new_name

    def add_student(self, name: Student):
        self.list_student.append(name)

    def score_student(self):
        for student in self.list_student:
            print(f"enter score {student.get_student_name()} :")
            score = int(input())
            student.add_score(score)

    def print_student(self):
        final_list = sorted(self.list_student, key = lambda x: x.average(), reverse = True)
        for student in final_list:
            print(f"student: {student.get_student_name()} and her average is {student.average()} ")










p = Teacher("fred")
# print(p.get_teacher_name())
# p.change_teacher_name("sara")
# print(p.get_teacher_name())

s1 = Student("sara")
s1.add_score(19)
s1.add_score(17)

s2 = Student("farbod")
s2.add_score(15)
s2.add_score(17)

course = Course(p)
course.add_student(s1)
course.add_student(s2)
course.print_student()
course.score_student()
