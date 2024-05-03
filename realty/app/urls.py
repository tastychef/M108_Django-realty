from django.urls import path
from . import views

urlpatterns = [
    path('', views.ZhkView.as_view()),
    path('<int:pk>/', views.ZhkDetail.as_view()),
]
