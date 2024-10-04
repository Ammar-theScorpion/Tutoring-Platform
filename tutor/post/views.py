from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import UpdateView

from .forms import PostCreateForm
from .forms import PostUpdateForm
from .models import Post

# Create your views here.


def home_posts_view(request):
    posts = Post.objects.all()
    return render(request, "pages/home.html", {"posts": posts})


class PostDetailsView(DetailView):
    template_name = "post/page_post.html"
    model = Post


post_details_view = PostDetailsView.as_view()


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "post/create_post.html"
    form_class = PostCreateForm
    login_url = reverse_lazy("account_login")

    def form_valid(self, form):
        post = form.save()
        return render(self.request, "post/post.html", {"post": post})


post_create_view = PostCreateView.as_view()


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "post/delete_post.html"
    success_url = reverse_lazy("home")
    model = Post

    def form_valid(self, form):
        messages.success(self.request, "post deleted successfuly!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Post did not delete successfully!")
        return super().form_invalid(form)


post_delete_view = PostDeleteView.as_view()


class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "post/update_post.html"
    form_class = PostUpdateForm
    model = Post

    success_url = reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "post updated successfuly!")
        return super().form_valid(form)


post_update_view = PostUpdateView.as_view()
