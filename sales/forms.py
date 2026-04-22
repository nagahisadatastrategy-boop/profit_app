from django import forms
from .models import Sales

class SalesForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Sales
        fields = ['store_name', 'date', 'sales_amount', 'cost']