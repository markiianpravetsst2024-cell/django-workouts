from django.urls import path
from . import views
urlpatterns = [
    path('', views.workout_list, name='workout_list'),
    path('create/', views.workout_create, name='workout_create'),
    path('<int:pk>/', views.workout_detail, name='workout_detail'),
    path('<int:pk>/done/', views.workout_done, name='workout_done'),
    path('<int:pk>/delete/', views.workout_delete, name='workout_delete'),
    path('<int:pk>/edit/', views.workout_edit, name='workout_edit'),
]