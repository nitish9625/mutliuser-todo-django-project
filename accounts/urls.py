from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="home"),
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout, name="logout"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('change-status/<int:id>/<str:status>', views.change_status, name="change-status"),
    path('edit/<int:id>',views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
]
