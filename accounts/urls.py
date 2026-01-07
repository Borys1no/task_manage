from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
from .views import login_view, logout_view, register_html_view, RegisterView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_html_view, name='register'),
    path('api/register/', 
    csrf_exempt(RegisterView.as_view()),
    name='api-register'
    ),

]


