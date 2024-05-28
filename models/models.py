import uuid
import re
from pydantic import BaseModel, Field, EmailStr, field_validator

person_regexp = r"^[a-zA-Z\xC0-\uFFFF]+([ \-']{0,1}[a-zA-Z\xC0-\uFFFF]+){0,2}[.]{0,1}$"
class User(BaseModel):
    id: uuid.UUID
    first_name: str = Field(regex=person_regexp)
    middle_name: str = Field(regex=person_regexp)
    last_name: str = Field(regex=person_regexp)
    email: EmailStr


    class Config:
        schema_extra = {
            "examples": [
                {
                    "first_name": "Ivan",
                    "last_name": "Bezned",
                    "mail": "ivan@chort.ru",
                }
            ]
        }