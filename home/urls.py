from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('user_profile', views.user_profile, name="user_profile"),
    path('set_links', views.set_links, name="set_links"),
    path('set_profile_image', views.set_profile_image, name="set_profile_image"),
    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('leaderboard', views.leaderboard, name="leaderboard"),
]

