from django.urls import path
from . import views

urlpatterns = [
    path('list_Sub/', views.display_sub, name="listSub"),
    path('list_Criti/', views.display_criti, name="listCriti"),
    path('add_critic/', views.add_critic, name='addCritic'),



]

