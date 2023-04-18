from dataclasses import dataclass

from app.core.admin.interactor import AdminInteractor, IEmailService


@dataclass
class OlympianTutorService:
    admin_interactor : AdminInteractor
    def send_hello(self):
        self.admin_interactor.send_hello()
    @classmethod
    def create(cls, emailer: IEmailService):
        return cls(admin_interactor=AdminInteractor(emailer))
