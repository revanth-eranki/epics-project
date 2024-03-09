from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-field'
        self.fields['password'].widget.attrs['class']='form-field'

        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['password'].widget.attrs['placeholder']='Password'


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-field','id':'input-first_name', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-field', 'id':'input-last_name', 'placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-field', 'id':'input-email', 'placeholder':'Email'}))
    
    class Meta:
        model=User
        fields = ['first_name','last_name','username','email','password1','password2'] 
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-field'
        self.fields['password1'].widget.attrs['class']='form-field'
        self.fields['password2'].widget.attrs['class']='form-field'

        self.fields['username'].widget.attrs['id']='input-username'
        self.fields['password1'].widget.attrs['id']='input-password1'
        self.fields['password2'].widget.attrs['id']='input-password2'

        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password2'].widget.attrs['placeholder']='Re-enter Password'