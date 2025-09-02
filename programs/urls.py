from django.urls import path
from . import views

app_name = 'programs'

urlpatterns = [
    path('', views.program_list, name='list'),
    path('<int:pk>/', views.program_detail, name='detail'),
    path('new/', views.program_create, name='create'),
    path('<int:pk>/edit/', views.program_update, name='update'),
    path('<int:pk>/delete/', views.program_delete, name='delete'),
]