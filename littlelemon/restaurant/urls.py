from django.urls import path
from . import views 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('', views.defualt_home, name = "home"),
    path('menu', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('view-user', views.UserDetailView.as_view()),
    path('create-user', views.CreateUser.as_view()),
    path('update-user/<int:pk>', views.UserUpdateView.as_view()),
    path('api-token-auth', obtain_auth_token),
]