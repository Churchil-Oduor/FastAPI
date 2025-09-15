from pydantic import BaseModel
from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4


class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "User"
    student = "student"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    #middle_name: Optional[str]
    gender: Gender
    roles: List[Role]


