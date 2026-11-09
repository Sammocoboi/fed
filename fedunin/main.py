from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel,Field,EmailStr

router = FastAPI()


class User(BaseModel):
    name :str = Field(...,max_length=50)
    age:int = Field(...,le=18)
    email:EmailStr


@router.get("/")
def hello_world():
    return "hello world"

@router.get("/hello/")
def hello_name(name:str|None = None):
    if name is None:
        return f"hello anonym"
    return f"hello {name}"
if __name__ == "__main__":
    uvicorn.run("main:router",reload=True)

@router.get("/calculate")
def calculate(a:int,b:int):
    return {"умножение":a*b,"деление":a/b,"сумма":a+b,"разность":a-b}

@router.post("/users/")
def get_user(name:str,age:int,email:str):
    try:
        user = User(name,age,email)

        return {"status":"success","user":user}
    except:
        return {"status":"error"}