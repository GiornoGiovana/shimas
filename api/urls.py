from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('activity/', views.ActivityDetail.as_view()),
    path('users/login/', views.UserLogin.as_view()),
    path('recommendation/<int:user_id>/', views.RecommendationList.as_view()),
    path('recommendation/<int:pk>/<str:movie>/', views.RecommendationDetail.as_view()),
    path('recommendation/filter/<int:pk>/<int:runtime>/', views.RecommendationFilter.as_view()),
    path('recommendation/discover/', views.DiscoverRecommendation.as_view()),
]