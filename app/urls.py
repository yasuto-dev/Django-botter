from django.urls import path

from . import views
app_name = "app"


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bot_response/', views.bot_response, name='bot_response'), 
  ]