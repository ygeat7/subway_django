from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index),
    path('<str:역이름>/', views.sub_render)
]