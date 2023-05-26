from faker import Faker
from dataclasses import dataclass

fake = Faker('es_MX')
 
@dataclass
class User:
    first_name: str
    last_name: str
    nickname: str
    email: str
    phone: str
    password: str


first_name = fake.first_name()
last_name = fake.last_name()
nickname = fake.user_name()
email = fake.email()
phone = fake.phone_number()
password = fake.password()


new_user = User(first_name, last_name, nickname, email, phone, password)
print(new_user)


"""
Common Faker methods:
fake.profile()
fake.name()
fake.address()
fake.email()
faker.date_of_birth()
fake.text()
fake.country()
fake.url()
fake.sentence()
faker.job()
faker.simple_profile()
"""