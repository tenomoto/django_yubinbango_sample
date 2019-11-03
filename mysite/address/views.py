from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .models import Address
from .forms import AddressForm

class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('index')

class AddressListView(ListView):
    model = Address