from typing import Any

from django import forms
from django import shortcuts
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView

from .models import Post, Profile, Tag


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "main/create_post.html"
    success_url = reverse_lazy("app_vladislav_yurenya:all_post")
    fields = [
        "car_brand",
        "car_model",
        "cost",
        "year",
        "content",
        "photo",
        "city",
        "name_user",
        "number_user",
    ]

    def form_valid(self, form):
        new = form.save(commit=False)
        new.key = self.request.user
        name_tag = form.cleaned_data["car_brand"]
        tag_for_use = Tag.objects.create(name=name_tag)
        tag_for_use.save()
        new.tag = tag_for_use
        return super().form_valid(form)


class ListPost(ListView):
    model = Post
    template_name = "main/all_post.html"

    def get_queryset(self):
        unique = Post.objects.values("car_brand").distinct()

        if (
            self.request.GET.get("search") is None
            or self.request.GET.get("search") == ""
        ):
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(
                car_brand__contains=self.request.GET.get("search")
            )

        return {"posts": posts, "unique": unique}


class DetailPost(DetailView):
    model = Post
    template_name = "main/detail.html"


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "main/update.html"
    success_url = reverse_lazy("app_vladislav_yurenya:all_post")
    fields = [
        "car_brand",
        "car_model",
        "cost",
        "year",
        "content",
        "photo",
        "city",
        "name_user",
        "number_user",
    ]


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "main/delete.html"
    success_url = reverse_lazy("app_vladislav_yurenya:all_post")


class DetailProfile(DetailView):
    model = Profile
    template_name = "main/profile.html"

    def get_object(self, queryset: Any = None) -> Any:
        object_1 = self.model.objects.get(user_id=self.request.user.id)
        return object_1


class FormUser(forms.Form):
    name = forms.CharField(label="Имя")
    tel = forms.IntegerField(label="Контактный телефон")
    email = forms.CharField(label="Почта")
    password = forms.CharField(
        label="Password:",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class RegisterUser(FormView):
    template_name = "main/register.html"
    form_class = FormUser
    success_url = reverse_lazy("app_vladislav_yurenya:all_post")

    def form_valid(self, form: forms.Form) -> HttpResponse:
        (username, email, tel, password) = (
            form.cleaned_data["name"],
            form.cleaned_data["email"],
            form.cleaned_data["tel"],
            form.cleaned_data["password"],
        )
        user = User.objects.create_user(username, email, password)
        user.save()
        user_to_profile = User.objects.get(username=user.username)
        user_to_profile.email, user_to_profile.tel = (email, tel)
        create_profile(user_to_profile)
        login(request=self.request, user=user)
        return shortcuts.redirect(self.success_url)


def create_profile(user: Any) -> None:
    profile = Profile.objects.create(
        name=user.username,
        tel=user.tel,
        email=user.email,
        user=user,
    )
    profile.save()


class LogoutUser(LogoutView):
    template_name = "main/user_or_guest.html"
    success_url = reverse_lazy("app_vladislav_yurenya:enter")


class EnterUser(LoginView):
    success_url = reverse_lazy("app_vladislav_yurenya:all_post")
    template_name = "main/enter.html"


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "main/update_profile.html"
    success_url = reverse_lazy("app_vladislav_yurenya:all_post")
    fields = ["name", "tel", "email"]


class MyPostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = "main/my_post_list.html"

    def get_queryset(self):
        my_post = Post.objects.filter(key_id=self.request.user)
        return {"my_post": my_post}


class MyPostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "main/my_post.html"
    success_url = reverse_lazy("app_vladislav_yurenya:my_post_list")
    fields = [
        "car_brand",
        "car_model",
        "cost",
        "year",
        "content",
        "photo",
        "city",
        "name_user",
        "number_user",
    ]


class MyPostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "main/my_post_delete.html"
    success_url = reverse_lazy("app_vladislav_yurenya:my_post_list")


class FilterTag(ListView):
    template_name = "main/all_post.html"
    model = Post

    def get_queryset(self):
        unique = Post.objects.values("car_brand").distinct()
        posts = Post.objects.filter(car_brand=self.request.GET.get("hz"))
        return {"posts": posts, "unique": unique}
