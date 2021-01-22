from game import views
from django.urls import path, include

# app_name='game'

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('game_list/', views.game_list, name='game_list'),
    path('game/', views.game, name='game'),
    path('accept/<int:pk>/', views.accept, name="accept"),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('ranking/', views.ranking, name='ranking'),
]