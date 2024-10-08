from django.urls import path
from . import views

app_name="account"
urlpatterns = [
    path('', views.index, name='index' ),
    path('login/', views.login_user, name='login' ),
    path('register/', views.register_user, name='register' ),
    path('me', views.me, name='me' ),
    path('logout/', views.logout_user, name='logout' ),
]