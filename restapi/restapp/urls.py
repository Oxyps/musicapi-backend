from django.urls import path

from . import views

urlpatterns = [
    path('musics/', views.MusicList.as_view()),
    path('music/<int:pk>/', views.MusicDetail.as_view()),
]