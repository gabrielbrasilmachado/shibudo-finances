from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Finance


class IsFinanceOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Finance):
        return request.user.is_superuser or request.user == obj.list.user
