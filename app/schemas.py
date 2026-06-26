from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    city: str
    gender: str


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    city: str
    gender: str

    class Config:
        from_attributes = True