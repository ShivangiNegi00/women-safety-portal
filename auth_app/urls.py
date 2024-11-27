from django.urls import path #type:ignore
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView

urlpatterns=[
    path('home/', views.home_view, name='home'),
    path('register/', views.register_view,name='register'),
    path('login/', views.login_view,name='login'),
    path('dashboard/', views.dashboard_view,name='dashboard'),
    path('logout/', views.logout_view,name='logout'),
    path('story/', views.story_view, name='story'),
    path('story/submit/', views.submit_story, name='submit_story'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('memorialwall/', views.memorialwall_view, name='memorialwall'),
   
]