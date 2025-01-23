from django.urls import path
from . import views

app_name ='games'

urlpatterns = [
    path('minislot/', views.minislot, name='minislot'),
    path('submit_minislot_result/', views.minislotresult, name='minislotresult'),

    path('head_tail/', views.flipcoin, name='flipcoin'),
    path('submit_head_or_tail_result/', views.flipcoinresult, name='minislotresult'),


    path('rock_paper_sissors/', views.rockpaper, name='rockpaper'),
    path('submit_rock_paper_sissors_result/', views.rockpaperresult, name='minislotresult'),


    path('bottle_spin', views.bottlespin, name='bottlespin'),
    path('submit_bottlespin_result/', views.bottlespinresult, name='minislotresult'),
]