from django.urls import path
from .views import RegisterView
from .views import LoginView
from . import views
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    
    path("register-page/", views.register_page, name="register_page"),
    path("login-page/", views.login_page, name="login_page"),
]
