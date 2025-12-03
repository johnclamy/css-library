from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='root_app.index'),
    path('about', views.about_page, name='root_app.about'),
]

