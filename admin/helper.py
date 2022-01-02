from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def superuser_only(function):
    """
    Limit view to superusers only.
    
    Usage:
    --------------------------------------------------------------------------
    @superuser_only
    def my_view(request):
        ...
    --------------------------------------------------------------------------
    
    or in urls:
    
    --------------------------------------------------------------------------
    urlpatterns = patterns('',
        (r'^foobar/(.*)', is_staff(my_view)),
    )
    --------------------------------------------------------------------------    
    """
    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('main_index')           
        return function(request, *args, **kwargs)
    return _inner