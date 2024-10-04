from factory import Faker
from factory.django import DjangoModelFactory

from tutor.users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker("user_name")
    email = Faker("email")
