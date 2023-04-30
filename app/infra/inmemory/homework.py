from dataclasses import dataclass, field
from typing import List

from app.core.homework.entity import Homework


@dataclass
class InMemoryHomeworkRepository:
    data: List[Homework] = field(default_factory=list)

    def create_homework(
            self, homework_text: str, tutor_mail: str, student_mail: str
    ) -> Homework:
        homework = Homework(homework_text, tutor_mail, student_mail)
        self.data.append(homework)
        return homework

    def change_homework(
            self, new_homework_text: str, old_homework_text: str, tutor_mail: str, student_mail: str
    ) -> Homework:
        for homework in self.data:
            if homework.homework_text == old_homework_text and \
                    homework.tutor_mail == tutor_mail and \
                    homework.student_mail == student_mail:
                homework.homework_text = new_homework_text

    def get_student_homework(self, student_mail: str) -> List[Homework]:
        homeworks: List[Homework] = []
        for homework in self.data:
            if homework.student_mail == student_mail:
                homeworks.append(homework)
        return homeworks

    def delete_homework(
            self, homework_text: str, tutor_mail: str, student_mail: str
    ) -> None:
        for homework in self.data:
            if homework.homework_text == homework_text and \
                    homework.tutor_mail == tutor_mail and \
                    homework.student_mail == student_mail:
                self.data.remove(homework)

