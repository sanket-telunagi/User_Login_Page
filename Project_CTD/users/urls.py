"""Define URL patterns for the user"""

from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
    # Landing page
    path('',views.HomePage,name='homepage'),

    # Login Page
    path('login/',views.loginPage,name='login'),

    # Resistration page
    path('register',views.register,name='register'),

    # Logout
    path('logout/',views.logoutpage,name='logout')
]