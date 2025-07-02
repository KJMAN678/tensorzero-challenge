from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inference/', views.inference_demo, name='inference_demo'),
    path('inference/<int:pk>/', views.inference_detail, name='inference_detail'),
    path('comparison/', views.model_comparison, name='model_comparison'),
    path('comparison/<int:pk>/', views.comparison_detail, name='comparison_detail'),
    path('analytics/', views.analytics, name='analytics'),
    path('api/feedback/<int:inference_id>/', views.feedback_api, name='feedback_api'),
]