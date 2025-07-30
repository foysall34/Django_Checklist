from rest_framework.response import Response
from rest_framework import status
from functools import wraps

def email_domain_required(domain='example.com'):
    """
    Only allow users with email from the specified domain.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

            if not request.user.email.endswith(f'@{domain}'):
                return Response({"detail": f"Only users with {domain} domain are allowed."}, status=status.HTTP_403_FORBIDDEN)

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
