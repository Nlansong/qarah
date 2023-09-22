from django.urls import path

from .import views

app_name = "dashboard"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('<slug:slug>/', views.detail_post, name='detail'),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),
]