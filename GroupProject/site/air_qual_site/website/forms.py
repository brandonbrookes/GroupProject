from django import forms

class PostCodeForm(forms.Form):
    postcode = forms.CharField(label='Enter Postcode',max_length=10,widget=forms.TextInput(attrs={'placeholder': 'e.g. LS5'}))