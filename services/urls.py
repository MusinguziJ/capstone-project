from django.urls import path
from . import views

app_name = 'services'  # This helps avoid name clashes between apps

urlpatterns = [
    path('', views.service_list, name='list'), # List all services
    path('<int:pk>/', views.service_detail, name='detail'), # View a single service
    path('new/', views.service_create, name='create'), # Form to create a new service
    path('<int:pk>/edit/', views.service_update, name='update'), # Form to edit a service
    path('<int:pk>/delete/', views.service_delete, name='delete'), # Form to delete a service
]