from. import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home.html'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('form',views.form,name='form'),
    path('newpage',views.new_page,name='newpage'),
    path('logout',views.logout,name='logout'),

]