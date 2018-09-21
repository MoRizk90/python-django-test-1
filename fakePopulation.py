import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','user_data_proj.settings')

import django
django.setup()

#from here we can have fake script
import random
from user_info_app.models import USER
from faker import Faker

fake_gen = Faker()

def populate(N = 5):
    for entry in range(N):
        fake_first_name = fake_gen.first_name()
        fake_last_name = fake_gen.last_name()
        fake_email = fake_gen.email()

        USER.objects.get_or_create(first_name = fake_first_name, seconed_name = fake_last_name, email = fake_email)[0]

if __name__ == '__main__':
    print("populating script")
    populate(5)
    print("done")
