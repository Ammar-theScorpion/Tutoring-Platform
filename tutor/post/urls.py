from django.urls import path

from .views import post_create_view
from .views import post_delete_view
from .views import post_details_view
from .views import post_update_view

app_name = "post"
urlpatterns = [
    path("create/", view=post_create_view, name="create"),
    path("<pk>/", view=post_details_view, name="details"),
    path("edit/<pk>/", view=post_update_view, name="edit"),
    path("delete/<pk>/", view=post_delete_view, name="delete"),
]
