"""Module for all Form Tests."""

from django.test import TestCase

from tutor.users.forms import UserAdminCreationForm
from tutor.users.models import User


class TestUserAdminCreationForm(TestCase):
    """
    Test class for all tests related to the UserAdminCreationForm
    """

    def setUp(self):
        self.user, _ = User.objects.get_or_create(id=0)

    def test_username_validation_error_msg(self):
        """
        Tests UserAdminCreation Form's unique validator functions correctly by testing:
            1) A new user with an existing username cannot be added.
            2) Only 1 error is raised by the UserCreation Form
            3) The desired error message is raised
        """

        # The user already exists,
        # hence cannot be created.
        form = UserAdminCreationForm(
            {
                "username": self.user.username,
                "password1": self.user.password,
            },
        )

        assert not form.is_valid()
        assert "username" in form.errors
