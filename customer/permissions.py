from rest_framework import permissions
from .models import CustomUser

# Custom permission class based on user_type
class UserTypePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Check the user's user_type for authorization
            user_type = request.user.customuser.user_type
            if user_type == 'admin':
                return True  # Admin users can access
            elif user_type == 'customer':
                return True  # Customer users can access
        return False
