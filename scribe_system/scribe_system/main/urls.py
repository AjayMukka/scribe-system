from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('scribe_register/', views.scribe_register, name='scribe_register'),
    path('book_login/', views.book_login, name='book_login'),
    path('scribe_login/', views.scribe_login, name='scribe_login'),
    path('register_login/', views.register_login, name='register_login'),
    path('', views.home, name='home'),
    
    path('home/', views.home, name='home'),
    # path('logout/', views.user_logout, name='logout'),
    path('request_scribe/', views.request_scribe, name='request_scribe'),
    path('welcome/', views.welcome, name='welcome'),
    path('scribe_requests/', views.scribe_requests, name='scribe_requests'),
    path('scribe_profile/', views.scribe_profile, name='scribe_profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accept_request/<int:request_id>/', views.accept_request, name='accept_request'),  # New URL for accepting the request
]

