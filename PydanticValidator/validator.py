from pydantic import BaseModel, ValidationError, validator

class CreateUser(BaseModel):
    email: str
    password: str 
    confirm_password: str
    
    @validator("email")
    def validate_email(cls, value):
        if "admin" in value:
            raise ValueError("Admin emails are not allowed")
        return value
    
    @validator("confirm_password")
    def passwords_match(cls, v, values):
        if "password" in values and v != values["password"]:
            raise ValueError("Passwords do not match")
        return v

try:
    CreateUser(email="user@fastapigamil.com", password="123", confirm_password="123")
    print("Validation successful")
except ValidationError as e:
    print(e)




