from django import forms  
from abb.models import visitors


class visitorform(forms.ModelForm):
    class Meta:
        model=visitors
        fields='__all__'