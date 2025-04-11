from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegisterView, UserDetailView, UserUpdateView, UserProfileView, UserProfileUpdateView

# URLs related to user management and authentication
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),  # Register a new user
    path('me/', UserDetailView.as_view(), name='user-detail'),  # View the details of the currently logged-in user
    path('me/update/', UserUpdateView.as_view(), name='user-update'),  # Update the details of the current user
    path('api/token/', obtain_auth_token, name='api_token_auth'),  # Login via token (Obtain token for API access)
    
    # Optionally, you can add paths for profile views if needed
    path('profile/', UserProfileView.as_view(), name='user-profile'),  # View the profile of the user
    path('profile/update/', UserProfileUpdateView.as_view(), name='user-profile-update'),  # Update the user's profile
]
