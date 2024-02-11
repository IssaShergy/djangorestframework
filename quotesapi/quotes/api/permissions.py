from rest_framework import permissions
class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self,request,view):
        is_adimin=super().has_permission(request,view)
        return request.method in permissions.SAFE_METHODS or is_adimin
          
