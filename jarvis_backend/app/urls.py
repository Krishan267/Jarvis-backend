from .views import LoginPage, Dashboard
from django.urls import path


urlpatterns = [
    path('login/', LoginPage.as_view(), name='login'),
    path('dashboard/', Dashboard.as_view(), name='user-dashboard-page'),
]