from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
# from .views import user_logout


from users.apps import UsersConfig
from users.views import RegisterView, ProfileView

# from users.views import logOut

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # ссылка на выход пользователя через функцию
    # path('logout/', user_logout, name='logout'),
    # ссылка на выход пользователя через кастомный класс
    # path('logout/', logOut.as_view(), name='logout'),
]
