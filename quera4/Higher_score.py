
'''
1. The Student class takes the names and grades of two students
2. It says which one has the higher rank.
3. This class has a method that performs the comparison.
'''

from __future__ import annotations
class Student:
    def __init__(self, name: str, grade: int):
        assert type(name) == str, "enetr yor currect name"
        assert type(grade) == int, "enter your grade as a number"
        self.name = name
        self.grade = grade

    '''
    1. The compare_grade method performs a comparison between grades 
    2. The compare_grade returns the output as a string.
    '''

    def compare_grade(self, other_student: Student) -> str: 
        if self.grade > other_student.grade:
            return print(f"{self.name} has a higher grade")
        elif other_student.grade > self.grade:
            return print(f"{other_student.name} has a higher grade")
        else:
            return print(f"{self.name} and {other_student.name} have the same grade")
        




# test_case_1
s1 = Student("Alice", 90)  
s2 = Student("Bob", 85)  
s1.compare_grade(s2)


# test_case_2
s1 = Student("manochehr", 90)  
s2 = Student("abid", 93)  
s1.compare_grade(s2)

# test_case_3
s1 = Student("sara", 97)  
s2 = Student("zahar", 97)  
s1.compare_grade(s2)