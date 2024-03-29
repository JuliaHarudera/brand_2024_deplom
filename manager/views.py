from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView
from brand.models import ContactUS
from .forms import ReservationEditForm
from django.urls import reverse_lazy, reverse


class ManagerAccessMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()


class ManagerIndex(LoginRequiredMixin, ManagerAccessMixin, ListView):
    template_name = 'manager_index.html'
    login_url = '/login/'
    model = ContactUS
    context_object_name = 'reservations'

    def get_queryset(self):
        return ContactUS.objects.filter(is_precessed=False).order_by('date', 'time')


class EditReservation(LoginRequiredMixin, ManagerAccessMixin, UpdateView):
    template_name = 'edit_reservation.html'
    login_url = '/login/'
    model = ContactUS
    form_class = ReservationEditForm
    success_url = reverse_lazy('manager:index')