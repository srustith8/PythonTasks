from django.contrib import admin
from django.urls import path,include
from drf_api import views

urlpatterns = [
    path('', views.apioverview,name="api-overview"),
    path('task-list/', views.tasklist,name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail,name="task-detail"),
    path('task-create/', views.taskCreate,name="task-create"),
    path('task-update/<str:pk>/', views.taskUpdate,name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete,name="task-delete"),
]
