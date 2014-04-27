from django.forms import ModelForm, fields

from offers.models import Offer


class OfferForm(ModelForm):

    class Meta:
        model = Offer
        fields = ['job', 'price',]