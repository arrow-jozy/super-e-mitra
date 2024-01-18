from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.formfill,name='formfill'),
    path('userform',views.userform,name='userform'),
    path('<str:slug>/',views.formpost,name='formpost'),
]