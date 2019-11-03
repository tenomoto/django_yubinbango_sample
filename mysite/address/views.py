from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Address
from .forms import AddressForm

class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('index')