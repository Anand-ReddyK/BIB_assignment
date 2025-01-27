from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home_view, name='home'),
    path('chat/<str:room_name>/', views.chat_room, name="chat_room")
]