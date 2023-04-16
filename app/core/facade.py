from dataclasses import dataclass


@dataclass
class SiteService:
    @classmethod
    def create(cls):
        return cls()
