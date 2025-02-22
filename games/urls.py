from django.urls import path
from . import views

app_name = 'games'


urlpatterns = [
    # urls for mines
    path("minesweeper/", views.minesweeper, name="minesweeper"),
    path('flappybet.mines/reveal/', views.reveal_card, name='flappybet.reveal'),
    path("flappybet.claim-reward/", views.claim_reward, name="claim_reward"),  # Add this if required
    path('submit_minesweeper_result', views.submit_minesweeper_result, name='minesweeper_result'),


    # urls for minislot
    path('minislot/', views.minislot, name='minislot'),
    path('submit_minislot_result/', views.minislotresult, name='minislotresult'),


    # urls for head & tail 
    path('head_tail/', views.flipcoin, name='flipcoin'),
    path('submit_head_or_tail_result/', views.submit_head_or_tail_result, name='head_or_tail_result'),



    #urls for rock paper scissor
    path('rock_paper_sissors/', views.rockpaper, name='rockpaper'),
    path('submit_rock_paper_sissors_result/', views.submit_rock_paper_scissors_result, name='rockpaper_result'),


    #urls for bottle_spin
    path('bottle_spin/', views.bottlespin, name='bottlespin'),
    path('submit_bottlespin_result/', views.submit_bottle_spin_result, name='bottlespin_result'),

]
