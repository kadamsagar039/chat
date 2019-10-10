from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<token>/', views.activate, name='activate'),
    path('resetpassword', views.reset_password, name='resetpassword'),
    path('verify/<Token>/', views.verify, name='verify'),
    path('login/resetmail/', views.sendmail, name='resetmail'),
    path('resetpassword/<username>/', views.reset_password, name='resetmail'),
    path('login/index_page', views.index, name='index_page'),
    path('login/index/<str:room_name>/', views.room, name='room_page'),
    path('', views.home, name='home')
]