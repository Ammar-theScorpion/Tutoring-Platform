from django.test import TestCase
from django.urls import reverse

from tutor.users.models import User

from .models import Post

OK = 200
REDIRECT = 302


# Create your tests here.
class TestCreatePost(TestCase):
    def setUp(self):
        self.url = reverse("post:create")
        self.user, _ = User.objects.get_or_create(
            username="testuser",
            email="test@example.com",
        )
        self.valid_data = {
            "title": "test title",
            "body": "test body",
            "image_url": "https://th.bing.com/th/id/OIP.UYjsISFqF09_P5Dnns6e2gHaE8?rs=1&pid=ImgDetMain",
        }

        self.invalid_data = {
            "title": "",
            "body": "test body",
            "image_url": "https://th.bing.com/th/id/OIP.UYjsISFqF09_P5Dnns6e2gHaE8?rs=1&pid=ImgDetMain",
        }

    def test_template_user(self):
        self.client.force_login(self.user)

        response = self.client.get(self.url)
        assert self.url == "/post/create/"
        assert response.status_code == OK
        self.assertTemplateUsed(response, "post/create_post.html")

    def test_post_unathorized(self):
        response = self.client.post(self.url, data=self.valid_data)

        assert response.status_code == REDIRECT
        assert Post.objects.exists()
        self.assertRedirects(response, f"{reverse('account_login')}?next={self.url}")

    def test_valid_authorized_post(self):
        self.client.force_login(self.user)

        response = self.client.post(self.url, data=self.valid_data)
        assert response.status_code == OK

        assert Post.objects.count() == Post.objects.count()
        post = Post.objects.first()
        assert post.title == self.valid_data["title"]
        assert post.body == self.valid_data["body"]

    def test_invalid_authorized_post(self):
        self.client.force_login(self.user)
        response = self.client.post(self.url, data=self.invalid_data)

        assert response.status_code == OK
        assert Post.objects.count() == 0
        self.assertTemplateUsed(response, "post/create_post.html")


class TestDeletePost(TestCase):
    def setUp(self):
        valid_data = {
            "title": "test title",
            "body": "test body",
            "image_url": "https://th.bing.com/th/id/OIP.UYjsISFqF09_P5Dnns6e2gHaE8?rs=1&pid=ImgDetMain",
        }

        self.user, _ = User.objects.get_or_create(
            username="testuser",
            email="test@example.com",
        )
        self.post = Post.objects.create(**valid_data)

        self.url = reverse("post:delete", kwargs={"pk": self.post.uuid})
        self.user, _ = User.objects.get_or_create(
            username="testuser2",
            email="test@example.com",
        )

    def test_template_used(self):
        self.client.force_login(self.user)

        response = self.client.get(self.url)
        assert self.url == f"/post/delete/{self.post.uuid}/"
        assert response.status_code == OK
        self.assertTemplateUsed(response, "post/delete_post.html")

    def test_post_unathorized(self):
        response = self.client.get(self.url)

        assert response.status_code == REDIRECT
        assert Post.objects.exists()
        self.assertRedirects(response, f"{reverse('account_login')}?next={self.url}")

    def test_valid_authorized_delete(self):
        self.client.force_login(self.user)

        response = self.client.post(self.url, follow=True)
        assert response.status_code == OK

        assert Post.objects.count() == 0
