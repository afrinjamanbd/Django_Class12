from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "app"
urlpatterns = [
    # path('app/newuser', views.newuser, name='newuser'),
    path('app/home', views.home, name='home'),
    # path('team_name_url/', views.home, name='home'),
    # path('app/profile',views.Profile, name='profile'),
] 