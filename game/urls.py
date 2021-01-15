from game import views
from django.urls import path, include

# 왜 앱네임을 넣으면 오류가 뜰까?
# 왜 post_new 오류가 뜰까?

urlpatterns = [
    path('', views.main, name='main'),
    path('login', views.login, name='login'),
    path('game_list', views.game_list, name='game_list'),
    path('game_option', views.game_option, name='game_option'),
    path('game_alone', views.game_alone, name='game_alone'),
    path('game', views.game, name='game'),
    path('ranking', views.ranking, name='ranking'),
    # path('post/<int:pk>', views.post_detail, name='post_detail' ),
    # path('post/new', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # 형식
    # path(루트,view함수명,kwargs=None,name=None)
]