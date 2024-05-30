from pydantic import BaseModel,field_validator
import typing

def fake_validator(value:typing.Any):
    return value


class A(BaseModel):
    a:int
    
    _validate_a=field_validator("a")(fake_validator)
    
    
class B(BaseModel):
    b:int
    
    _validate_a=field_validator("b")(fake_validator)
    
    
print(A(a=1))
print(B(b=1))