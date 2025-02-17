
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
        self.name = new_name


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
        self.name = new_name

    def add_score(self, score: int) -> list:
        assert type(score) == int, "enter score as a int"
        self.list_score.append(score)

    def average(self) -> int:
        final_score = 0
        for score in self.list_score:
            final_score += score
        return final_score / (len(self.list_score))