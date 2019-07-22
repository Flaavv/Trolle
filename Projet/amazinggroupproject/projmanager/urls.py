'''
Created on 16 juil. 2019

@author: All

'''
from django.urls import path
from . import views

app_name = 'projmanager'

urlpatterns = [
    path('', views.Auth_User, name='loginuser'),
    path('projects/', views.List_project, name='projects'),
    path('<int:project_id>/', views.List_task_for_project, name='tasks'),
    path('task/<int:task_id>/', views.Task_Show, name='taskdetail'),
    path('new_task/', views.New_Task, name='new_task'),
    path('taskupdate/<int:task_id>', views.Task_Update, name='taskupdate'),
    path('newproject/', views.New_Project, name='newproject'),
    path('logout/', views.Deconnect, name='logout'),
    path('task/informations/<int:task_id>', views.Informations, name='informations'),
    path('task/newinformation/', views.New_Information, name='newinformation'),
]
