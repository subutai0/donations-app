from django import forms

class DonationForm(forms.Form):
    amount = forms.DecimalField(label='Amount', max_digits=10, decimal_places=2)
    frequency = forms.ChoiceField(label='Frequency', choices=[('one-time', 'One-time'), ('monthly', 'Monthly'), ('yearly', 'Yearly')])