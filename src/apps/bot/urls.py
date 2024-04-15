from django.urls import path
from .views import *

urlpatterns = [
    path('', AdminDashboard.as_view(), name='dashboard'),
    path('overview/', AdminDashboardOverview.as_view(), name='dashboard-overview'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ResetPasswordView.as_view(), name='change-password'),
    path('verify-account/', VerifyEmailView.as_view(), name='verify-account'),
]
