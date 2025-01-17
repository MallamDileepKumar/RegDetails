from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('regdetails/', views.RegisterDetails.as_view(), name='regdetails'),
]