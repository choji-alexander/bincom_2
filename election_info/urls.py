from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('question1/', views.display_result, name='display_results'),
    path('question2/', views.sum_pu_lga, name='sum_pu_lga'),
    path('question3/', views.store_results, name='store_results'),
]

