# from django.contrib.auth import logout
# from django.shortcuts import redirect
# from django.views import generic
#
#
# def user_logout(request):
#     """Функция для выхода пользователя в Django 5."""
#     logout(request)
#     return redirect('/')
#
#
# class logOut(generic.View):
#     """Класс для выхода пользователя в Django 5."""
#     def get(self, request):
#         logout(request)
#         return redirect('/')
#
# для стандартной формы регистрации
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

