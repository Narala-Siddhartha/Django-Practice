from django import forms
class UserForm(forms.Form):
    n1 = forms.CharField(label="value 1", required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    n2 = forms.CharField(label="value 2", required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

