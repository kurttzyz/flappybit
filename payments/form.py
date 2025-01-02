from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'reference_number', 'payment_method']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'reference_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter reference number'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'amount': 'Payment Amount',
            'reference_number': 'Reference Number',
            'payment_method': 'Payment Method',
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount