from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    def has_permission(self, request, view) -> bool:
        # write any logic applicable
        return True