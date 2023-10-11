from django import forms
from .models import userSignup,notes,contact

class userSignupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'

    
class notesForm(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields=['firstname','lastname','email','password','mobile','country']


class contactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'