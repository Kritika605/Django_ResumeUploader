from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view() , name='index'),
    path('<int:pk>', views.CandidateView.as_view() , name='candidate'),
]