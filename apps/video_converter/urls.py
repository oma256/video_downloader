from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_page, name='redirect'),
    path('index/', views.index, name='index'),
    path('download/', views.download, name='download'),
]
