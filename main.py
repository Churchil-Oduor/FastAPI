from fastapi import FastAPI
from typing import List
from models import User, Role, Gender
from uuid import UUID, uuid4

app = FastAPI()
db: List[User] = [
        User(
            id=uuid4(), 
            first_name = "churchil",
            last_name = "okech",
            gender = Gender.male,
            roles = [Role.admin, Role.user]
         ),
            User(
                id = uuid4(),
                first_name = "hope",
                last_name = "brandy",
                gender = Gender.female,
                roles = [Role.student]
                )
    ]

@app.get("/")
def root():
    response =  {"msg": "hello world"}
    return response

@app.get("/api/v1/users")
def fetch_users():
    return db


@app.post("/api/v1/users")
def post_user(user: User):
    db.append(user)
    return {"id": user.id}
