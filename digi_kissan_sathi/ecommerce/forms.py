from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Create_Seller_Account

class Signupforms(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        
class Seller_Account_Form(forms.ModelForm):
    class Meta:
        model=Create_Seller_Account
        fields = [
            'busines_name',
            'business_name_nepali',
            'business_address',
            'busines_contact_number',
            'business_email',
            'citizenship_number',
            'pan_number',
            'goverment_id',
            'bank_account_number',
            'bank_name',
            'ifcs_code',
            'payment_gateway_id',
            'categories',
            'profile_picture',
        ]
        
        
    def save(self, user, commit=True):
        instance = super().save(commit=False)
        instance.user = user  # Assign the logged-in user
        instance.is_active = True
        instance.total_sales = 0
        instance.rating = 0.0
        instance.reviews_count = 0
        if commit:
            instance.save()
        return instance

        
    
    def clean_business_number(self):
        contact_number=self.cleaned_data.get('business_contact_number')
        if len(contact_number)>15:
            raise forms.ValidationError("Invalid Business Contact Number")
        return contact_number
    
    

