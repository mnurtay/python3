from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name="logout")
]
