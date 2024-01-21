from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
# from .views import user_logout


from users.apps import UsersConfig
# from users.views import logOut

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('logout/', user_logout, name='logout'),
    # path('logout/', logOut.as_view(), name='logout'),
]
