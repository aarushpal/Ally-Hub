from core.models import *
from django.contrib.auth.models import User, auth
from faker import Faker

fake = Faker()

def db_seeder(records = 10)->None:
    for i in range(records):
        fake_email = fake.email()
        fake_username = fake.user_name()
        new_user = User(username=fake_username, email=fake_email, password='admin')
        new_user.save()