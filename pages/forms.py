from django import forms
from django.forms import ValidationError
from .models import complaint,witness

class complaintform(forms.ModelForm):
    name    = forms.CharField(label='Name',widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    email = forms.EmailField(required=False,widget=forms.EmailInput(attrs={"placeholder":"your Email ID"}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"your Mobile Number"}))
    adhaar = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"your Adhaar Number"}))
    address = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Your Address", "rows": 6,'cols': 50}))
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"crime description", "rows": 15,
                                    'cols': 70}))
    
    class Meta:
        model = complaint
        fields = [
            'name',
            'email',
            'phone',
            'adhaar',
            'address',
            'description',
            

        ]

class witnessform(forms.ModelForm):
    name    = forms.CharField(label='Name',widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"your Email ID"}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"your Mobile Number"}))
    adhaar = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"your Adhaar Number"}))
    address = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Your Address", "rows": 6,'cols': 50}))
    crime_description = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"witnessed crime", "rows": 15,
                                    'cols': 70}))
    class Meta:
        model = witness
        fields = [
            'name',
            'email',
            'phone',
            'adhaar',
            'address',
            'crime_description',
        ]



