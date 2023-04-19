from dataclasses import dataclass

from app.core.admin.interactor import AdminInteractor, IEmailService
from app.core.course.interactor import CourseInteractor, ICourseInteractor


@dataclass
class OlympianTutorService:
    admin_interactor: AdminInteractor
    course_interactor: CourseInteractor

    def send_hello(self):
        self.admin_interactor.send_hello()

    def send_verification(self):
        self.admin_interactor.verify_mail()

    def get_course(self):
        self.course_interactor.get_course()

    @classmethod
    def create(
        cls, emailer: IEmailService, course_interactor: ICourseInteractor
    ) -> "OlympianTutorService":
        return cls(
            admin_interactor=AdminInteractor(emailer),
            course_interactor=CourseInteractor(course_interactor),
        )
