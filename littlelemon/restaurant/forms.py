from django.forms import ModelForm
from .models import Booking, Menu

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

class AgregarMenu(ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"