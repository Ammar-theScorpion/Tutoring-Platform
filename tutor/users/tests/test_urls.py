from django.test import TestCase
from django.urls import resolve
from django.urls import reverse

from tutor.users.models import User


class UriTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testUser", email="test@example.com")

    def test_detail(self):
        assert (
            reverse("users:profile", kwargs={"username": self.user.username})
            == f"/users/{self.user.username}/"
        )
        assert resolve(f"/users/{self.user.username}/").view_name == "users:profile"

    def test_update(self):
        assert reverse("users:update") == "/users/~update/"
        assert resolve("/users/~update/").view_name == "users:update"

    def test_redirect(self):
        assert reverse("users:redirect") == "/users/~redirect/"
        assert resolve("/users/~redirect/").view_name == "users:redirect"
