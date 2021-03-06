from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('home/', views.homepage, name='homepage'),
    path('projects/', views.projects_list, name='projects_list'),
    path('invite_user/', views.invite_new_user, name='invite_new_user'),
    path('project_create/', views.project_create, name='project_create'),
    path('projects/<int:project_number>/chart', views.chart, name='chart'),
    path('projects/<int:project_number>/project_edit', views.project_edit, name='project_edit'),
    path('projects/<int:project_number>/project_delete', views.project_delete, name='project_delete'),
    path('projects/<int:project_number>', views.tasks_list, name='tasks_list'),
    path('projects/<int:project_number>/user_list', views.all_users, name='all_users'),
    path('projects/<int:project_number>/task_create', views.task_create, name='task_create'),
    path('projects/<int:project_number>/<int:task_number>/task_edit', views.task_edit, name='task_edit'),
    path('projects/<int:project_number>/<int:task_number>/task_delete', views.task_delete, name='task_delete'),

]