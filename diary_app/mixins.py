from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import redirect


class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user:
            prev_page = request.META.get('HTTP_REFERER')
            if prev_page:
                return HttpResponseRedirect(prev_page)
            else:
                return redirect('/')
        return super().dispatch(request, *args, **kwargs)

class StaffRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("Доступ разрешен только для стаффа!")
        return super().dispatch(request, *args, **kwargs)