from django import forms

from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ("postal_code", "region", "locality", "street", "extended")
        widgets = {
            "postal_code": forms.TextInput(
                attrs = {'class': 'p-postal-code', 'placeholder': '0000000',},
            ),
            "region": forms.TextInput(
                attrs = {'class': 'p-region',},
            ),    
            "locality": forms.TextInput(
                attrs = {'class': 'p-locality',},
            ),
            "street": forms.TextInput(
                attrs = {'class': 'p-street-address',},
            ),
            "extended": forms.TextInput(
                attrs = {'class': 'p-extended-address',},
            ),
        }