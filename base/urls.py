from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('details/<int:pk>/',views.detail, name="detail"),
    path('post/', views.new_post, name="new_post"),
    path('update/<int:pk>/', views.updatepost, name="update_post"),
    path('delete/<int:pk>/', views.deletepost, name="delete"),
    path('user/', views.loginPage, name="userlogin"),
    path('logout/', views.logoutuser, name="logout"),
    path('signup/', views.signup, name="signup"),
]
