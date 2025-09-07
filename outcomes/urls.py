from django.urls import path
from . import views

app_name = 'outcomes'

urlpatterns = [
    path('', views.project_selection, name='project_selection'),
    path('project/<int:project_id>/', views.outcome_list, name='list'),
    path('<int:pk>/', views.outcome_detail, name='detail'),
    path('project/<int:project_id>/new/', views.outcome_create, name='create'),
    path('<int:pk>/edit/', views.outcome_update, name='update'),
    path('<int:pk>/delete/', views.outcome_delete, name='delete'),
    path('<int:pk>/download/', views.download_artifact, name='download'),
]