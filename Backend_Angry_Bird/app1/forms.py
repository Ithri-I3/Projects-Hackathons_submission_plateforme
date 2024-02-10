from django.db.models import fields
from django import forms
from .models import Critic
from .models import Critic
class CriticForm(forms.ModelForm):
    class Meta:
        model = Critic
        #exclude = ['cri_judge']
        fields = "__all__"
