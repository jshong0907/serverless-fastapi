from app.models.domains.base_class import Base


class User(Base):
    email: str
    password: str
