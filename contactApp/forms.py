from django import forms
from django.core.exceptions import ValidationError
from .models import Contact
import re
class ContactForm(forms.ModelForm):
    
    # name = forms.CharField(label="Votre Nom", max_length=100, required=True, widget=forms.TextInput())
    # email = forms.EmailField(label="votre email", required=True, max_length=100, widget=forms.TextInput())
    # phone_number = forms.CharField(label="Votre numero", required=True, max_length=100, widget=forms.TextInput())

    class Meta:
        model = Contact
        fields = ["name", "email", "phone_number", "face_id"]
        widgets = {
            "name": forms.TextInput(),
            "email": forms.TextInput(),
            "phone_number": forms.TextInput(),
            "face_id": forms.FileInput
        }

        labels ={
            "name": "your name",
            "email": "your email",
            "phone_number": "your phone_here",
            "face_id" : "profile image"
            
        }


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(str(name)) < 2:
            raise ValidationError(message="Name is too short")
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(pattern, str(email)):
            raise ValidationError(message="Invalid email")
        
        return email
        
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')

        if len(str(phone)) < 2:
            raise ValidationError(message="phone number should be greater than 2")
        
        return phone

