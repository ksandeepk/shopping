from django import forms
from .models import Registration,Category,Product

class ContactForm(forms.Form):
    yourname = forms.CharField(required=True)
    mobile_number = forms.CharField(max_length=10)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
class RegistrationForm(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField()
  
class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

Product_Quantity_Choices=[ (i,str(i)) for i in range(1,21)]
class CartAddProductForm(forms.Form):
    quantity=forms.TypedChoiceField(choices=Product_Quantity_Choices,coerce=int)
    update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)

class CartForm(forms.Form):
    name=forms.CharField(max_length=30)
    price=forms.CharField(max_length=30)
    img=forms.ImageField()
