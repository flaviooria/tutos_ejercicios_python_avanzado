from dataclasses import dataclass

# Dataclass, nos sirve para 

@dataclass
class UserBase:
    name: str
    email: str
    password: str


user = UserBase(name='Flavio', email='flavio@dev', password='pass123')

print(user)
