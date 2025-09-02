from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.project_list, name='list'),
    path('<int:pk>/', views.project_detail, name='detail'),
    path('new/', views.project_create, name='create'),
    path('<int:pk>/edit/', views.project_update, name='update'),
    path('<int:pk>/delete/', views.project_delete, name='delete'),
    path('<int:project_pk>/remove-participant/<int:participant_pk>/', views.remove_participant, name='remove_participant')
]