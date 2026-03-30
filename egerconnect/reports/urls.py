from django.urls import path
from . import views
from .views import user_analysis_report

urlpatterns = [
    path('support-requests-report/', views.support_requests_report, name='support-requests-report'),
    
     path('user-analysis/', user_analysis_report, name='user-analysis-report'),
     
     path('posts-report/', views.posts_report, name='posts-report'),
]