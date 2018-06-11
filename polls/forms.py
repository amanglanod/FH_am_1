from django import forms



class RateForm(forms.Form):
    rate = forms.ChoiceField()
