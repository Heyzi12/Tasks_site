from django.core.exceptions import PermissionDenied


class UserIsOgnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.cteator == self.request.user:
            raise PermissionDenied
        return super.dispatch(request, *args, **kwargs)