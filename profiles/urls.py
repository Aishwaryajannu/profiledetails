from django.urls import path
from . import views
from profiles import views as profile_views

urlpatterns = [
    path('profile/<str:username>/', views.profile_page, name='profile_page'),
    path('api/profile/<str:username>/', views.get_profile_api, name='get_profile_api'),
    path('api/profile/create/', profile_views.create_profile_api),
]
