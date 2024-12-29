from django.http import HttpResponseForbidden

class StaffRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("Доступ разрешен только для стаффа!")
        return super().dispatch(request, *args, **kwargs)