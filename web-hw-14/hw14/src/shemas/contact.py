from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, EmailStr

# from src.database.models import User
from src.shemas.users import UserResponse


class ContactModel(BaseModel):
    first_name: str = Field(
        default="",
        examples=["Yoda", "Anakin"],
        min_length=1,
        max_length=25,
        title="Ім'я",
    )
    last_name: str = Field(
        default="",
        examples=["Master", "Skywalker"],
        min_length=1,
        max_length=25,
        title="Прізвище",
    )
    email: EmailStr
    phone: str | None = Field(
        None,
        examples=["+380 66 123-4567", "+380 (66) 1234567", "+380661234567"],
        max_length=25,
        title="Номер телефону",
    )
    birthday: date | None = None
    comments: str | None = Field(default=None, title="Додаткові дані")
    favorite: bool = False
    # user_id: int = Field(1, gt=0)


class ContactFavoriteModel(BaseModel):
    favorite: bool = False

    # pattern=r"^+[0-9\s\(\)-]+$


class ContactResponse(BaseModel):
    id: int
    first_name: str | None
    last_name: str | None
    email: EmailStr | None
    phone: str | None
    birthday: date | None
    comments: str | None
    favorite: bool
    created_at: datetime
    updated_at: datetime
    user: UserResponse

    # class Config:
    #     from_attributes = True

    model_config = ConfigDict(from_attributes=True)

    # email: str = Field(default="email@examole.com", pattern=r'^\w+@\w+\.\w+$')


# class Contact(Base):
#     """
#     Ім'я
#     Прізвище
#     Електронна адреса
#     Номер телефону
#     День народження
#     Додаткові дані (необов'язково)
#     """
#     __tablename__ = "contacts"

#     id = Column(Integer, primary_key=True, index=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     email = Column(String)
#     phone = Column(String)
#     birthday = Column(Date)
#     comments = Column(Text)
#     favorite = Column(Boolean, default=False)
#     created_at = Column(DateTime, default=func.now())
#     updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
