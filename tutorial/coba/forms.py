from django.db.models import fields
from django.forms import ModelForm
from coba.models import bukutamu

class BuatPesan(ModelForm):
    class Meta:
        model = bukutamu
        fields = '__all__'