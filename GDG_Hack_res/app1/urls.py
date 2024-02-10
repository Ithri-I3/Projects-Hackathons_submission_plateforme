from django.urls import path
from . import views
from .views import submission_marks

urlpatterns = [
    path('list_Sub/', views.display_sub, name="listSub"),
    path('list_Criti/', views.display_criti, name="listCriti"),
    path('add_critic/', views.add_critic, name='addCritic'),
    path('submission_marks/', submission_marks, name='submission_marks'),



]

