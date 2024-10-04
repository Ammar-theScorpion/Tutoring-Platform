from http import HTTPStatus

import pytest
from django.http import HttpResponseRedirect
from django.test import RequestFactory
from django.test import TestCase
from django.urls import reverse

from tutor.users.models import User
from tutor.users.tests.factories import UserFactory
from tutor.users.views import UserRedirectView
from tutor.users.views import UserUpdateView

pytestmark = pytest.mark.django_db


class TestUserUpdateView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
        )
        self.client.force_login(self.user)

        self.factory = RequestFactory()
        self.url = reverse("users:update")

    def test_get_success_url(self):
        request = self.factory.get(self.url)
        request.user = self.user

        view = UserUpdateView()
        view.request = request
        success_url = view.get_success_url()

        assert success_url == f"/users/{self.user.username}/"

    def test_get_object(self):
        request = self.factory.get(self.url)
        request.user = self.user

        view = UserUpdateView()
        view.request = request
        obj = view.get_object()

        assert obj == self.user


class TestUserRedirectView:
    def test_get_redirect_url(self, user: User, rf: RequestFactory):
        view = UserRedirectView()
        request = rf.get("/fake-url")
        request.user = user

        view.request = request
        assert view.get_redirect_url() == f"/users/{user.username}/"


class TestUserDetailView(TestCase):
    def setUp(self):
        pass

    def test_authenticated(self):
        user = User.objects.create_user(username="testuser", email="test@example.com")
        response = self.client.force_login(user)
        url = reverse("users:profile", kwargs={"username": user.username})
        response = self.client.get(url)

        assert response.status_code == HTTPStatus.OK
        assert url == f"/users/{user.username}/"

    def test_not_authenticated(self):
        user = UserFactory()  # Create a user (but don't log in)
        url = reverse("users:profile", kwargs={"username": user.username})
        response = self.client.get(url)

        # Assert the user is redirected to the login page
        assert isinstance(response, HttpResponseRedirect)
        assert response.status_code == HTTPStatus.FOUND
        assert response.url == f"/accounts/login/?next=/users/{user.username}/"
