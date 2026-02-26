from django.urls import path
from .views import RegisterView
from .views import LoginView
from . import views
# accounts/urls.py
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from .views import dashboard_page

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    
    path("register-page/", views.register_page, name="register_page"),
    path("login-page/", views.login_page, name="login_page"),
    
    path("login_success/", views.login_success, name="login_success"),
    path("register_success/", views.register_success, name="register_success"),
    
     # ... your other paths ...
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    path("dashboard/", dashboard_page, name="dashboard"),
]
