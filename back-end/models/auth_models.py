from pydantic import BaseModel, Field, validator, EmailStr
class LoginCredentials(BaseModel):
    username: str = Field(examples=['user1'])
    password: str = Field(examples=['Password@1'])

class SignUpCredentials(BaseModel):
    username: str = Field(examples=['user1'], min_length=2)
    password: str = Field(examples=['Password@1'], min_length=8)
    email: EmailStr

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

    @validator('password')
    def password_complexity(cls, v):
        special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}','[', ']', ':', ';', '"', "'", '<', '>', '?', '/', '\\', '|']
        assert any(char.isdigit() for char in v), 'must contain at least one digit'
        assert any((char>='A' and char<='Z') for char in v), 'must contain at least one upper case letter'
        assert any((char>='a' and char<='z') for char in v), 'must contain at least one lower case letter'
        assert any((char in special_characters) for char in v), 'must contain at least one special character'
        return v


class Token(BaseModel):
    token:str;