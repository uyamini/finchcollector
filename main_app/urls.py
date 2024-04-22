from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # new path to 'about/' that goes to views.about
    path('about/', views.about, name='about'),
    # route for finches index
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),

]