from django import forms
# from .models import Contact

class Contactus(forms.Form):
	name=forms.CharField(label='name')
	subject=forms.CharField(label='subject')
	message=forms.CharField(widget=forms.Textarea, label='message')
	email=forms.EmailField(label='email')

class Articleposts(forms.Form):
	article=forms.CharField(label='article', widget=forms.Textarea)
	
class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())