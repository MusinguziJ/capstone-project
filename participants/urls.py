from django.urls import path
from . import views

app_name = 'participants'

urlpatterns = [
    path('', views.participant_list, name='list'),
    path('<int:pk>/', views.participant_detail, name='detail'),
    path('new/', views.participant_create, name='create'),
    path('<int:pk>/edit/', views.participant_update, name='update'),
    path('<int:pk>/delete/', views.participant_delete, name='delete'),
]